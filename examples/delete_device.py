#!/usr/bin/env python
"""Delete an Intersight device via the Intersight API."""
import sys
import json
import argparse
from intersight.intersight_api_client import IntersightApiClient
from intersight.apis import asset_device_registration_api
from intersight.apis import asset_device_claim_api

if __name__ == "__main__":
    result = dict(changed=False)

    try:
        # settings are pulled from the json string or JSON file passed as an arg
        parser = argparse.ArgumentParser()
        help_str = 'JSON file with Intersight API parameters.  Default: intersight_api_params.json'
        parser.add_argument('-a', '--api_params', default='intersight_api_params.json', help=help_str)
        help_str = 'Target host ip to delete.  Deletes 1st device found with the specified IP (does not handle multiple devices with same IPs in an account)'
        parser.add_argument('-t', '--target_host', dest='hostname', required=True, help=help_str)
        args = parser.parse_args()
        with open(args.api_params, 'r') as api_file:
            intersight_api_params = json.load(api_file)

        # Create Intersight API instance
        # ----------------------
        api_instance = IntersightApiClient(
            host=intersight_api_params['api_base_uri'],
            private_key=intersight_api_params['api_private_key_file'],
            api_key_id=intersight_api_params['api_key_id'],
        )

        # create API handle
        api_handle = asset_device_registration_api.AssetDeviceRegistrationApi(api_instance)

        kwargs = dict(filter="ConnectionStatus eq 'Connected'")
        api_result = api_handle.asset_device_registrations_get(**kwargs)
        for device in api_result.results:
            if device.device_ip_address[0] == args.hostname:
                api_handle = asset_device_claim_api.AssetDeviceClaimApi(api_instance)
                api_handle.asset_device_claims_moid_delete(moid=device.device_claim.moid)
                print("Device deleted:", args.hostname)
                result['changed'] = True
                break
        else:
            # for loop completed without finding the device
            print("Device not found or not connected:", args.hostname)

        print(json.dumps(result))

    except Exception as err:
        print("Exception:", str(err))
        import traceback
        print('-' * 60)
        traceback.print_exc(file=sys.stdout)
        print('-' * 60)
        sys.exit(1)

    sys.exit(0)
