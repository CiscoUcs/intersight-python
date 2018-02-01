#!/usr/bin/env python

import sys
if sys.version_info[0] == 3:
    import urllib.parse as URL
elif sys.version_info[0] == 2:
    import urllib as URL
import subprocess
import requests
import json
import re
from xml.etree import ElementTree
import argparse
import os.path
from intersight.intersight_api_client import IntersightApiClient
from intersight.apis import asset_device_claim_api


class DeviceConnector(object):
    def __init__(self, host):
        self.logged_in = False
        self.auth_header = ''
        self.host = host
        if self.host['device_type'] == 'ucspe':
            self.connector_uri = "http://%s/connector" % self.host['hostname']
        else:
            self.connector_uri = "https://%s/connector" % self.host['hostname']
        self.systems_uri = "%s/Systems" % self.connector_uri

    def enable_connector(self):
        retries = 0
        while retries <= 3:
            # get admin, connection, and claim state
            ro = requests.get(self.systems_uri, verify=False, headers=self.auth_header)
            if not re.match(r"2..", str(ro.status_code)):
                raise Exception("Device Connector API Systems status: %s" % ro.status_code)
            ro_json = ro.json()[0]
            if ro_json['AdminState'] is True:
                break
            else:
                # enable the device connector
                ro = requests.put(self.systems_uri, verify=False, headers=self.auth_header, json={'AdminState': True})
                if not re.match(r"2..", str(ro.status_code)):
                    raise Exception("Device Connector API enable status: %s" % ro.status_code)
                retries += 1
        return ro_json

    def configure_proxy(self, ro_json):
        # if not connected, put proxy settings
        if ro_json['ConnectionState'] != 'Connected' and self.host.get('proxy_host') and self.host.get('proxy_port'):
            # setup defaults for proxy settings
            if not self.host.get('proxy_password'):
                self.host['proxy_password'] = ''
            if not self.host.get('proxy_username'):
                self.host['proxy_username'] = ''
            proxy_payload = {
                'ProxyHost': self.host['proxy_host'],
                'ProxyPassword': self.host['proxy_password'],
                'ProxyPort': int(self.host['proxy_port']),
                'ProxyType': 'Manual',
                'ProxyUsername': self.host['proxy_username'],
            }
            proxy_uri = "%s/HttpProxies" % self.connector_uri
            retries = 0
            while retries <= 10:
                # wait for state to report connected
                ro = requests.get(self.systems_uri, verify=False, headers=self.auth_header)
                if not re.match(r"2..", str(ro.status_code)):
                    raise Exception("Device Connector API Systems status: %s" % ro.status_code)
                ro_json = ro.json()[0]
                if ro_json['ConnectionState'] == 'Connected':
                    break
                else:
                    retries += 1
            return ro_json

    def get_claim_info(self, ro_json):
        device_id = ''
        claim_code = ''
        # if connected and unclaimed, get device id and claim code
        if ro_json['ConnectionState'] == 'Connected' and ro_json['AccountOwnershipState'] != 'Claimed':
            id_uri = "%s/DeviceIdentifiers" % self.connector_uri
            ro = requests.get(id_uri, verify=False, headers=self.auth_header)
            if not re.match(r"2..", str(ro.status_code)):
                raise Exception("Device Connector API status: %s" % ro.status_code)
            ro_json = ro.json()[0]
            device_id = ro_json['Id']

            claim_uri = "%s/SecurityTokens" % self.connector_uri
            ro = requests.get(claim_uri, verify=False, headers=header)
            if not re.match(r"2..", str(ro.status_code)):
                raise Exception("Device Connector API status: %s" % ro.status_code)
            ro_json = ro.json()[0]
            claim_code = ro_json['Token']
        return(device_id, claim_code)


class HxDeviceConnector(DeviceConnector, object):
    def __init__(self, host):
        super(HxDeviceConnector, self).__init__(host)
        # create HX REST API session
        # --------------------------------
        self.hx_rest_uri = "https://%s/aaa/v1/auth?grant_type=password" % self.host['hostname']
        hx_rest_header = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        hx_rest_body = {
            'username': self.host['username'],
            'password': self.host['password'],
            'client_id': 'HxGuiClient',
            'client_secret': 'Sunnyvale',
            'redirect_uri': 'http://localhost:8080/aaa/redirect'
        }
        ro = requests.post(hx_rest_uri, verify=False, headers=hx_rest_header, json=hx_rest_body)
        if not re.match(r"2..", str(ro.status_code)):
            raise Exception("Device Connector API status: %s" % ro.status_code)
        ro_json = ro.json()
        hx_cookie_str = "test; tokenType=Basic; locale=en; refreshToken=%s; token=%s" % (ro_json['refresh_token'], ro_json['access_token'])
        self.auth_header = {'Cookie': hx_cookie_str}
        self.logged_in = True

    def logout(self):
        if self.logged_in:
            # logout TBD
            self.logged_in = False


class UcsDeviceConnector(DeviceConnector, object):
    def __init__(self, host):
        super(UcsDeviceConnector, self).__init__(host)
        # XML API login and create session cookie
        # --------------------------------
        self.xml_uri = "https://%s/nuova" % self.host['hostname']
        xml_body = "<aaaLogin inName=\"%s\" inPassword=\"%s\" />" % (self.host['username'], self.host['password'])
        ro = requests.post(self.xml_uri, verify=False, data=xml_body)
        if not re.match(r"2..", str(ro.status_code)):
            raise Exception("Device Connector API status: %s" % ro.status_code)
        xml_tree = ElementTree.fromstring(ro.content)
        self.xml_cookie = xml_tree.attrib['outCookie']
        self.auth_header = {'ucsmcookie': "ucsm-cookie=%s" % self.xml_cookie}
        self.logged_in = True

    def logout(self):
        if self.logged_in:
            # XML API logout
            # --------------------------------
            xml_body = "<aaaLogout inCookie=\"%s\" />" % self.xml_cookie
            self.logged_in = False


class ImcDeviceConnector(DeviceConnector, object):
    def __init__(self, host):
        super(ImcDeviceConnector, self).__init__(host)
        # create IMC browser session (requires encrypted password)
        # --------------------------------
        encrypted_password = subprocess.check_output(['EncryptPassword/Mac/EncryptPassword_v2', self.host['hostname'], self.host['password']]).rstrip()
        imc_login_uri = "https://%s/data/login" % self.host['hostname']
        self.imc_header = {
            'Origin': 'https://ucs-starship.com',
            'Referer': 'https://ucs-starship.com/an/aurora/deviceclaim/',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        imc_login_str = "user=%s&password=%s" % (URL.quote_plus(self.host['username']), URL.quote_plus(encrypted_password))
        ro = requests.post(imc_login_uri, verify=False, headers=self.imc_header, data=imc_login_str)
        if not re.match(r"2..", str(ro.status_code)):
            raise Exception("IMC session status: %s" % ro.status_code)
        self.imc_session_cookie = ro.cookies.values()[0]
        xml_tree = ElementTree.fromstring(ro.content)
        self.imc_session_id = xml_tree.find('sidValue').text
        self.auth_header = {
            'Cookie': "sessionCookie=%s" % self.imc_session_cookie,
            'Origin': 'https://ucs-starship.com',
            'Referer': 'https://ucs-starship.com/an/aurora/deviceclaim/'
        }
        self.logged_in = True

    def logout(self):
        if self.logged_in:
            # IMC webgui session logout
            # --------------------------------
            self.imc_header['Cookie'] = "sessionCookie=%s" % self.imc_session_cookie
            imc_logout_str = "sessionID=%s" % self.imc_session_id
            imc_logout_uri = "https://%s/data/logout" % self.host['hostname']
            ro = requests.post(imc_logout_uri, verify=False, headers=self.imc_header, data=imc_logout_str)
            self.logged_in = False

if __name__ == "__main__":
    result = dict(changed=False)

    try:
        # settings are pulled from the json string or JSON file passed as an arg
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', '--file', default='settings.json', help='JSON settings file (settings.json used by default)')
        parser.add_argument('-j', '--json_str', help='JSON string with host access information')
        args = parser.parse_args()
        if os.path.isfile(args.file):
            settings = json.load(open(args.file, 'r'))
        else:
            settings = json.loads(args.file)

        if settings.get('hosts'):
            # if a hosts list was included with settings, code will loop over the hosts
            hosts_list = settings['hosts']
        else:
            # if there was not a hosts list, use the json_str to load host information
            hosts_list = [json.loads(args.json_str)]
        for host in hosts_list:
            if host['device_type'] == 'ucsm' or host['device_type'] == 'ucspe':
                dc_obj = UcsDeviceConnector(host)
            elif host['device_type'] == 'hx':
                dc_obj = HxDeviceConnector(host)
            elif host['device_type'] == 'imc':
                dc_obj = ImcDeviceConnector(host)
            else:
                raise Exception("Unknown device_type %s" % host['device_type'])

            ro_json = dc_obj.enable_connector()
            # if not connected, configure proxy settings if proxy settings were provided
            if ro_json['ConnectionState'] != 'Connected' and host.get('proxy_host') and host.get('proxy_port'):
                ro_json = dc_obj.configure_proxy(ro_json)

            result['msg'] = "  Host: %s" % host['hostname']
            result['msg'] += "  AdminState: %s" % ro_json['AdminState']
            result['msg'] += "  ConnectionState: %s" % ro_json['ConnectionState']
            result['msg'] += "  Claimed state: %s" % ro_json['AccountOwnershipState']

            # if connected and unclaimed, get device id and claim code
            if ro_json['ConnectionState'] == 'Connected' and ro_json['AccountOwnershipState'] != 'Claimed':
                (device_id, claim_code) = dc_obj.get_claim_info(ro_json)
                result['msg'] += "  Id: %s" % device_id
                result['msg'] += "  Token: %s" % claim_code

                # Create Intersight API instance and post ID/claim code
                # ----------------------
                api_instance = IntersightApiClient(host=settings['api_host'], private_key=settings['api_private_key'], api_key_id=settings['api_key_id'])

                # create device claim API handle
                api_handle = asset_device_claim_api.AssetDeviceClaimApi(api_instance)

                # post ID/Claim Code
                claim_body = {'SecurityToken': claim_code, 'SerialNumber': device_id}
                claim_result = api_handle.asset_device_claims_post(claim_body)
                result['changed'] = True

            print json.dumps(result)

            # logout of any open sessions
            dc_obj.logout()

    except Exception, err:
        print "Exception:", str(err)
        import traceback
        print '-' * 60
        traceback.print_exc(file=sys.stdout)
        print '-' * 60
        sys.exit(1)

    finally:
        # logout of any sessions active after exception handling
        if ('dc_obj' in locals() or 'dc_obj' in globals()):
            dc_obj.logout()

    sys.exit(0)
