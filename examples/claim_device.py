#!/usr/bin/env python

import sys
import json
import requests
import argparse
import os.path
from xml.etree import ElementTree
from intersight.intersight_api_client import IntersightApiClient
from intersight.apis import asset_device_claim_api

if __name__ == "__main__":
    xml_uri = ''
    cookie = ''
    result = dict(changed=False)

    try:
        # settings are pulled from the json string or JSON file passed as an arg
        parser = argparse.ArgumentParser()
        parser.add_argument('json_arg', help='JSON settings file or JSON object as a string')
        args = parser.parse_args()
        if os.path.isfile(args.json_arg):
            settings = json.load(open(args.json_arg, 'r'))
        else:
            settings = json.loads(args.json_arg)

        if settings.get('hosts'):
            hosts_list = settings['hosts']
        else:
            hosts_list = [settings]
        for host in hosts_list:
            if host['device_type'] == 'ucsm':
                # XML API login and create session cookie
                # --------------------------------
                xml_uri = "https://%s/nuova" % host['hostname']
                xml = "<aaaLogin inName=\"%s\" inPassword=\"%s\" />" % (host['username'], host['password'])
                ro = requests.post(xml_uri, verify=False, data=xml)
                xml_tree = ElementTree.fromstring(ro.content)
                cookie = xml_tree.attrib['outCookie']
                header = {'ucsmcookie': "ucsm-cookie=%s" % cookie}
            elif host['device_type'] == 'hx':
                # create HX REST API session
                # --------------------------------
                hx_rest_uri = "https://%s/aaa/v1/auth?grant_type=password" % host['hostname']
                hx_rest_header = {'Content-Type': 'application/json', 'Accept': 'application/json'}
                hx_rest_data = {
                    'username': host['username'],
                    'password': host['password'],
                    'client_id': 'HxGuiClient',
                    'client_secret': 'Sunnyvale',
                    'redirect_uri': 'http://localhost:8080/aaa/redirect'
                }
                ro = requests.post(hx_rest_uri, verify=False, headers=hx_rest_header, json=hx_rest_data)
                ro_json = ro.json()
                cookie_str = "test; tokenType=Basic; locale=en; refreshToken=%s; token=%s" % (ro_json['refresh_token'], ro_json['access_token'])
                header = {'Cookie': cookie_str}
            else:
                # create IMC browser session (requires encrypted password)
                # --------------------------------
                # encrypted_password = raw_input('Enter encrypted password: ')
                # imc_login_uri = "https://%s/data/login" % host['hostname']
                # imc_login_header = {'Origin': 'https://ucs-starship.com', 'Referer': 'https://ucs-starship.com/an/aurora/deviceclaim/'}
                # imc_login_str = "user=%s&password=%s" % (host['username'], encrypted_password)
                # ro = requests.post(imc_login_uri, verify=False, headers=imc_login_header, data=imc_login_str)
                # ro_json = ro.json()
                # session_cookie = ro_json['sessionCookie']
                session_cookie = raw_input('Enter session cookie: ')
                header = {
                    'Cookie': "sessionCookie=%s" % session_cookie,
                    'Origin': 'https://ucs-starship.com',
                    'Referer': 'https://ucs-starship.com/an/aurora/deviceclaim/'
                }

            # Use session cookie for Device Connector API session
            # ----------------------
            connector_uri = "https://%s/connector" % host['hostname']
            systems_uri = "%s/Systems" % connector_uri

            retries = 0
            while True and retries <= 3:
                # get admin, connection, and claim state
                ro = requests.get(systems_uri, verify=False, headers=header)
                if ro.status_code != 200:
                    raise Exception("Device Connector API Systems status: %s" % ro.status_code)
                ro_json = ro.json()[0]
                if ro_json['AdminState'] is True:
                    break
                else:
                    # enable the device connector
                    ro = requests.put(systems_uri, verify=False, headers=header, json={'AdminState': True})
                    if ro.status_code != 200:
                        raise Exception("Device Connector API enable status: %s" % ro.status_code)
                    retries += 1

            result['msg'] = "  Host: %s" % host['hostname']
            result['msg'] += "  AdminState: %s" % ro_json['AdminState']
            result['msg'] += "  ConnectionState: %s" % ro_json['ConnectionState']
            result['msg'] += "  Claimed state: %s" % ro_json['AccountOwnershipState']

            # if connected and unclaimed, get device id and claim code
            if ro_json['ConnectionState'] == 'Connected' and ro_json['AccountOwnershipState'] != 'Claimed':
                id_uri = "%s/DeviceIdentifiers" % connector_uri
                ro = requests.get(id_uri, verify=False, headers=header)
                if ro.status_code != 200:
                    raise Exception("Device Connector API status: %s" % ro.status_code)
                ro_json = ro.json()[0]
                result['msg'] += "  Id: %s" % ro_json['Id']
                device_id = ro_json['Id']

                claim_uri = "%s/SecurityTokens" % connector_uri
                ro = requests.get(claim_uri, verify=False, headers=header)
                if ro.status_code != 200:
                    raise Exception("Device Connector API status: %s" % ro.status_code)
                ro_json = ro.json()[0]
                result['msg'] += "  Token: %s" % ro_json['Token']
                claim_code = ro_json['Token']

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

    except Exception, err:
        print "Exception:", str(err)
        import traceback
        print '-' * 60
        traceback.print_exc(file=sys.stdout)
        print '-' * 60
        sys.exit(1)

    if cookie and xml_uri:
        # XML API session logout
        # --------------------------------
        xml = "<aaaLogout inCookie=\"%s\" />" % cookie
        ro = requests.post(xml_uri, verify=False, data=xml)

    sys.exit(0)
