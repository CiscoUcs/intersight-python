#!/usr/bin/env python

import sys
import json
import requests
from xml.etree import ElementTree
from starship.api_client import ApiClient
from starship.apis import asset_device_claim_api

if __name__ == "__main__":
    xml_uri = ''
    cookie = ''
    result = {}
    result['changed'] = False

    try:
        # settings are pulled from the json string passed in as arg1
        if len(sys.argv) < 2:
            print "Usage: %s <JSON string>" % sys.argv[0]
            print "   Ex: %s \"{ \\\"username\\\": }\"" % sys.argv[0]
            sys.exit(0)
        settings = json.loads(sys.argv[1])

        if settings['device_type'] == 'ucsm':
            # XML API login and create session cookie
            # --------------------------------
            xml_uri = "https://%s/nuova" % settings['hostname']
            xml = "<aaaLogin inName=\"%s\" inPassword=\"%s\" />" % (settings['username'], settings['password'])
            ro = requests.post(xml_uri, verify=False, data=xml)
            xml_tree = ElementTree.fromstring(ro.content)
            cookie = xml_tree.attrib['outCookie']
            header = {'ucsmcookie': "ucsm-cookie=%s" % cookie}
        elif settings['device_type'] == 'hx':
            # create HX REST API session
            # --------------------------------
            hx_rest_uri = "https://%s/aaa/v1/auth?grant_type=password" % settings['hostname']
            hx_rest_header = {'Content-Type': 'application/json', 'Accept': 'application/json'}
            hx_rest_data = {'username': settings['username'],
                            'password': settings['password'],
                            'client_id': 'HxGuiClient',
                            'client_secret': 'Sunnyvale',
                            'redirect_uri': 'http://localhost:8080/aaa/redirect'}
            ro = requests.post(hx_rest_uri, verify=False, headers=hx_rest_header, json=hx_rest_data)
            ro_json = ro.json()
            cookie_str = "test; tokenType=Basic; locale=en; refreshToken=%s; token=%s" % (ro_json['refresh_token'], ro_json['access_token'])
            header = {'Cookie': cookie_str}
        else:
            # create IMC browser session (requires encryped password)
            # --------------------------------
            # encrypted_password = raw_input('Enter encrypted password: ')
            # imc_login_uri = "https://%s/data/login" % settings['hostname']
            # imc_login_header = {'Origin': 'https://ucs-starship.com', 'Referer': 'https://ucs-starship.com/an/aurora/deviceclaim/'}
            # imc_login_str = "user=%s&password=%s" % (settings['username'], encrypted_password)
            # ro = requests.post(imc_login_uri, verify=False, headers=imc_login_header, data=imc_login_str)
            # ro_json = ro.json()
            # session_cookie = ro_json['sessionCookie']
            session_cookie = raw_input('Enter session cookie: ')
            header = {'Cookie': "sessionCookie=%s" % session_cookie,
                      'Origin': 'https://ucs-starship.com',
                      'Referer': 'https://ucs-starship.com/an/aurora/deviceclaim/'}

        # Use session cookie for Device Connector API session
        # ----------------------
        connector_uri = "https://%s/connector" % settings['hostname']
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

        result['msg'] = "  AdminState: %s" % ro_json['AdminState']
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
            api_instance = ApiClient(host=settings['api_host'])
            api_instance.private_key_file = settings['api_private_key']
            api_instance.api_key_id = settings['api_key_id']
            api_instance.digest_algorithm = 'rsa-sha256'

            # create device claim API handle
            claim_handle = asset_device_claim_api.AssetDeviceClaimApi(api_instance)

            # post ID/Claim Code
            claim_body = {'SecurityToken': claim_code, 'SerialNumber': device_id}
            claim_result = claim_handle.asset_device_claims_post(claim_body)
            result['changed'] = True

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

    print json.dumps(result)
    sys.exit(0)
