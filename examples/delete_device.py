#!/usr/bin/env python

import sys
import json
import argparse
import os.path
from intersight.intersight_api_client import IntersightApiClient
from intersight.apis import asset_device_registration_api
from intersight.apis import asset_device_claim_api

if __name__ == "__main__":
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
            # Create Intersight API instance
            # ----------------------
            api_instance = IntersightApiClient(host=settings['api_host'], private_key=settings['api_private_key'], api_key_id=settings['api_key_id'])

            # create API handle
            api_handle = asset_device_registration_api.AssetDeviceRegistrationApi(api_instance)

            kwargs = dict(filter="ConnectionStatus eq 'Connected'")
            api_result = api_handle.asset_device_registrations_get(**kwargs)
            for device in api_result.results:
                if device.device_ip_address[0] == host['hostname']:
                    api_handle = asset_device_claim_api.AssetDeviceClaimApi(api_instance)
                    api_handle.asset_device_claims_moid_delete(moid=device.device_claim.moid)
                    result['changed'] = True

            print json.dumps(result)

    except Exception, err:
        print "Exception:", str(err)
        import traceback
        print '-' * 60
        traceback.print_exc(file=sys.stdout)
        print '-' * 60
        sys.exit(1)

    sys.exit(0)
