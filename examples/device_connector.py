#!/usr/bin/env python
"""Intersight Device Connector API access classes."""
import sys
import subprocess
import re
from xml.etree import ElementTree
import platform
import requests


class DeviceConnector(object):
    """Intersight Device Connector API superclass.
    Managed endpoint access information (hostname, username) and configuration data should be provided in the device dictionary parameter.
    """
    def __init__(self, device):
        self.logged_in = False
        self.auth_header = ''
        self.device = device
        if self.device['device_type'] == 'ucspe':
            self.connector_uri = "http://%s/connector" % self.device['hostname']
        else:
            self.connector_uri = "https://%s/connector" % self.device['hostname']
        self.systems_uri = "%s/Systems" % self.connector_uri

    def enable_connector(self):
        """Check current Admin state and enable the Device Connector if not currently enabled."""
        ro_json = dict(AdminState=False)
        for _ in range(4):
            # get admin, connection, and claim state
            resp = requests.get(self.systems_uri, verify=False, headers=self.auth_header)
            if re.match(r'2..', str(resp.status_code)):
                ro_json = resp.json()[0]
                if ro_json['AdminState'] is True:
                    break
                else:
                    # enable the device connector
                    resp = requests.put(self.systems_uri, verify=False, headers=self.auth_header, json={'AdminState': True})
                    if not re.match(r'2..', str(resp.status_code)):
                        ro_json['ApiError'] = "PUT %s %s" % (self.systems_uri, resp.status_code)
                        break
            else:
                ro_json['ApiError'] = "GET %s %s" % (self.systems_uri, resp.status_code)
                break
        return ro_json

    def configure_access_mode(self, ro_json):
        """Configure the Device Connector access mode (ReadOnlyMode True/False)."""
        # device read_only setting is a bool (True/False)
        resp = requests.put(self.systems_uri, verify=False, headers=self.auth_header, json={'ReadOnlyMode': self.device['read_only']})
        if not re.match(r'2..', str(resp.status_code)):
            ro_json['ApiError'] = "PUT %s %s" % (self.systems_uri, resp.status_code)
        return ro_json

    def configure_proxy(self, ro_json):
        """Configure the Device Connector proxy if proxy settings (hostname, port) were provided)."""
        # if not connected, put proxy settings
        if ro_json['ConnectionState'] != 'Connected' and self.device.get('proxy_host') and self.device.get('proxy_port'):
            # setup defaults for proxy settings
            if not self.device.get('proxy_password'):
                self.device['proxy_password'] = ''
            if not self.device.get('proxy_username'):
                self.device['proxy_username'] = ''
            proxy_payload = {
                'ProxyHost': self.device['proxy_host'],
                'ProxyPassword': self.device['proxy_password'],
                'ProxyPort': int(self.device['proxy_port']),
                'ProxyType': 'Manual',
                'ProxyUsername': self.device['proxy_username'],
            }
            proxy_uri = "%s/HttpProxies" % self.connector_uri
            resp = requests.put(proxy_uri, verify=False, headers=self.auth_header, json=proxy_payload)
            if re.match(r'2..', str(resp.status_code)):
                for _ in range(10):
                    # wait for state to report connected
                    resp = requests.get(self.systems_uri, verify=False, headers=self.auth_header)
                    if re.match(r'2..', str(resp.status_code)):
                        ro_json = resp.json()[0]
                        if ro_json['ConnectionState'] == 'Connected':
                            break
                    else:
                        ro_json['ApiError'] = "GET %s %s" % (self.systems_uri, resp.status_code)
                        break
            else:
                ro_json['ApiError'] = "PUT %s %s" % (proxy_uri, resp.status_code)
        return ro_json

    def get_claim_info(self):
        """Get the Device ID and Claim Code from the Device Connector."""
        claim_resp = {}
        device_id = ''
        claim_code = ''
        # get device id and claim code
        id_uri = "%s/DeviceIdentifiers" % self.connector_uri
        resp = requests.get(id_uri, verify=False, headers=self.auth_header)
        if re.match(r'2..', str(resp.status_code)):
            ro_json = resp.json()[0]
            device_id = ro_json['Id']

            claim_uri = "%s/SecurityTokens" % self.connector_uri
            resp = requests.get(claim_uri, verify=False, headers=self.auth_header)
            if re.match(r'2..', str(resp.status_code)):
                ro_json = resp.json()[0]
                claim_code = ro_json['Token']
            else:
                claim_resp['ApiError'] = "GET %s %s" % (claim_uri, resp.status_code)
        else:
            claim_resp['ApiError'] = "GET %s %s" % (id_uri, resp.status_code)
        return(claim_resp, device_id, claim_code)


class HxDeviceConnector(DeviceConnector, object):
    """HyperFlex (HX) Device Connector subclass.
    HX REST API session cookie is used to authenticate Device Connector API access.
    """
    def __init__(self, device):
        super(HxDeviceConnector, self).__init__(device)
        # create HX REST API session
        # --------------------------------
        self.hx_rest_uri = "https://%s/aaa/v1/auth?grant_type=password" % self.device['hostname']
        hx_rest_header = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        hx_rest_body = {
            'username': self.device['username'],
            'password': self.device['password'],
            'client_id': 'HxGuiClient',
            'client_secret': 'Sunnyvale',
            'redirect_uri': 'http://localhost:8080/aaa/redirect'
        }
        resp = requests.post(self.hx_rest_uri, verify=False, headers=hx_rest_header, json=hx_rest_body)
        if re.match(r'2..', str(resp.status_code)):
            ro_json = resp.json()
            hx_cookie_str = "test; tokenType=Basic; locale=en; refreshToken=%s; token=%s" % (ro_json['refresh_token'], ro_json['access_token'])
            self.auth_header = {'Cookie': hx_cookie_str}
            self.logged_in = True

    def logout(self):
        """Logout of HX REST API session if currently logged in."""
        if self.logged_in:
            # logout TBD
            self.logged_in = False


class UcsDeviceConnector(DeviceConnector, object):
    """UCS Manager (UCSM) Device Connector subclass.
    UCS XML API session cookie is used to authenticate Device Connector API access.
    """
    def __init__(self, device):
        super(UcsDeviceConnector, self).__init__(device)
        # XML API login and create session cookie
        # --------------------------------
        self.xml_uri = "https://%s/nuova" % self.device['hostname']
        xml_body = "<aaaLogin inName=\"%s\" inPassword=\"%s\" />" % (self.device['username'], self.device['password'])
        resp = requests.post(self.xml_uri, verify=False, data=xml_body)
        if re.match(r'2..', str(resp.status_code)):
            xml_tree = ElementTree.fromstring(resp.content)
            self.xml_cookie = xml_tree.attrib['outCookie']
            self.auth_header = {'ucsmcookie': "ucsm-cookie=%s" % self.xml_cookie}
            self.logged_in = True

    def logout(self):
        """Logout of UCSM API session if currently logged in."""
        if self.logged_in:
            # XML API logout
            # --------------------------------
            xml_body = "<aaaLogout inCookie=\"%s\" />" % self.xml_cookie
            requests.post(self.xml_uri, verify=False, data=xml_body)
            self.logged_in = False


class ImcDeviceConnector(DeviceConnector, object):
    """Integration Management Controller (IMC) Device Connector subclass.
    IMC web GUI (webgui) session cookie is used to authenticate Device Connector API access.
    """
    def __init__(self, device):
        super(ImcDeviceConnector, self).__init__(device)
        # create IMC browser session (requires password generated by a outside utility)
        # imports for utility use are directly below so they are not required in non IMC environments
        # --------------------------------
        if sys.version_info[0] == 3:
            import urllib.parse as URL
            import get_data_3 as get_data
            import six
            password = six.b(self.device['password']) 
        elif sys.version_info[0] == 2:
            import urllib as URL
            import get_data_2 as get_data
            password = str(self.device['password'])
        system_type = platform.system()
        utils_extension = ''
        if system_type == 'Darwin':
            system_type = 'Mac'
        elif system_type == 'Windows':
            utils_extension = '.exe'
        utils_dir = 'GetData'
        utils_exe = "%s/%s/GetData%s" % (utils_dir, system_type, utils_extension)
        try:
            passphrase = subprocess.check_output([utils_exe, self.device['username']])
            utils_password = get_data.E(passphrase, password)
            imc_login_str = "user=%s&password=%s" % (URL.quote_plus(self.device['username']), URL.quote_plus(utils_password.rstrip()))
            imc_login_uri = "https://%s/data/login" % self.device['hostname']
            referer = "https://%s/uiconnector/index.html" % self.device['hostname']
            self.imc_header = {
                'Referer': referer,
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            resp = requests.post(imc_login_uri, verify=False, headers=self.imc_header, data=imc_login_str)
            if re.match(r'2..', str(resp.status_code)):
                cookies = list(resp.cookies.values())
                if cookies:
                    self.imc_session_cookie = cookies[0]
                    xml_tree = ElementTree.fromstring(resp.content)
                    self.imc_session_id = xml_tree.find('sidValue').text
                    self.auth_header = {
                        'Cookie': "sessionCookie=%s" % self.imc_session_cookie,
                        'Referer': referer
                    }
                    self.logged_in = True
                else:
                    print("Unable to login: ", imc_login_uri)
        except subprocess.CalledProcessError as sub_ret:
            print("Utils exe returns ", sub_ret.returncode, sub_ret.output)

    def logout(self):
        """Logout of IMC webgui session if currently logged in."""
        if self.logged_in:
            # IMC webgui session logout
            # --------------------------------
            self.imc_header['Cookie'] = "sessionCookie=%s" % self.imc_session_cookie
            imc_logout_str = "sessionID=%s" % self.imc_session_id
            imc_logout_uri = "https://%s/data/logout" % self.device['hostname']
            requests.post(imc_logout_uri, verify=False, headers=self.imc_header, data=imc_logout_str)
            self.logged_in = False
