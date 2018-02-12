#!/usr/bin/env python
"""Intersight Device Connector API configuration and device claim via the Intersight API."""
import sys
import argparse
import os.path
import json
from intersight.intersight_api_client import IntersightApiClient
from intersight.apis import asset_device_claim_api
import device_connector


if __name__ == "__main__":
    return_code = 0

    try:
        parser = argparse.ArgumentParser()
        help_str = 'JSON file with Intersight API parameters.  Default: intersight_api_params.json'
        parser.add_argument('-a', '--api_params', default='intersight_api_params.json', help=help_str)
        help_str = 'JSON file with device access information (device hostname, username, password, and proxy settings if requred)'
        parser.add_argument('-d', '--devices', required=True, help=help_str)
        args = parser.parse_args()
        with open(args.api_params, 'r') as api_file:
            intersight_api_params = json.load(api_file)
        if os.path.isfile(args.devices):
            with open(args.devices, 'r') as devices_file:
                devices_list = json.load(devices_file)
        else:
            # Argument devices can be a JSON string instead of file.
            # JSON string input can be used with Ansible to directly pass all info on the command line.
            devices_list = json.loads(args.devices)

        for device in devices_list:
            result = dict(changed=False)
            result['msg'] = "  Host: %s" % device['hostname']
            # default access mode to allow control (Read-only False) and set to a boolean value if a string
            if device.get('read_only') == None:
                device['read_only'] = False
            else:
                if device['read_only'] == 'True':
                    device['read_only'] = True
                elif device['read_only'] == 'False':
                    device['read_only'] = False
            # create device connector object based on device type
            if device['device_type'] == 'ucsm' or device['device_type'] == 'ucspe':
                dc_obj = device_connector.UcsDeviceConnector(device)
            elif device['device_type'] == 'hx':
                dc_obj = device_connector.HxDeviceConnector(device)
            elif device['device_type'] == 'imc':
                dc_obj = device_connector.ImcDeviceConnector(device)
            else:
                result['msg'] += "  Unknown device_type %s" % device['device_type']
                return_code = 1
                print(json.dumps(result))
                continue

            if not dc_obj.logged_in:
                result['msg'] += "  Login error"
                return_code = 1
                print(json.dumps(result))
                continue

            ro_json = dc_obj.enable_connector()
            if ro_json['AdminState'] is False:
                return_code = 1
                if ro_json.get('ApiError'):
                    result['msg'] += ro_json['ApiError']
                print(json.dumps(result))
                continue

            # set access mode (ReadOnlyMode True/False) to desired state
            if (ro_json.get('ReadOnlyMode') != None) and (ro_json['ReadOnlyMode'] != device['read_only']):
                ro_json = dc_obj.configure_access_mode(ro_json)
                if ro_json.get('ApiError'):
                    result['msg'] += ro_json['ApiError']
                    return_code = 1
                    print(json.dumps(result))
                    continue
                result['changed'] = True

            # if not connected, configure proxy settings if proxy settings were provided
            if ro_json['ConnectionState'] != 'Connected' and device.get('proxy_host') and device.get('proxy_port'):
                ro_json = dc_obj.configure_proxy(ro_json)
                if ro_json.get('ApiError'):
                    result['msg'] += ro_json['ApiError']
                    return_code = 1
                    print(json.dumps(result))
                    continue
                result['changed'] = True

            result['msg'] += "  AdminState: %s" % ro_json['AdminState']
            result['msg'] += "  ConnectionState: %s" % ro_json['ConnectionState']
            result['msg'] += "  Claimed state: %s" % ro_json['AccountOwnershipState']

            # if connected and unclaimed, get device id and claim code
            if ro_json['ConnectionState'] == 'Connected' and ro_json['AccountOwnershipState'] != 'Claimed':
                (claim_resp, device_id, claim_code) = dc_obj.get_claim_info()
                if claim_resp.get('ApiError'):
                    result['msg'] += claim_resp['ApiError']
                    return_code = 1
                    print(json.dumps(result))
                    continue

                result['msg'] += "  Id: %s" % device_id
                result['msg'] += "  Token: %s" % claim_code

                # Create Intersight API instance and post ID/claim code
                # ----------------------
                api_instance = IntersightApiClient(
                    host=intersight_api_params['api_base_uri'],
                    private_key=intersight_api_params['api_private_key_file'],
                    api_key_id=intersight_api_params['api_key_id'],
                )

                # create device claim API handle
                api_handle = asset_device_claim_api.AssetDeviceClaimApi(api_instance)

                # post ID/Claim Code
                claim_body = {'SecurityToken': claim_code, 'SerialNumber': device_id}
                claim_result = api_handle.asset_device_claims_post(claim_body)
                result['changed'] = True

            print(json.dumps(result))

            # logout of any open sessions
            dc_obj.logout()

    except Exception as err:
        print("Exception:", str(err))
        import traceback
        print('-' * 60)
        traceback.print_exc(file=sys.stdout)
        print('-' * 60)
        sys.exit(1)

    finally:
        # logout of any sessions active after exception handling
        if ('dc_obj' in locals() or 'dc_obj' in globals()):
            dc_obj.logout()

    sys.exit(return_code)
