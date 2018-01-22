#!/usr/bin/env python

import sys
import json
import argparse
import os.path
from intersight.intersight_api_client import IntersightApiClient
from intersight.apis import iam_user_api
from intersight.apis import iam_permission_api

if __name__ == "__main__":
    result = dict(changed=False)

    try:
        # settings are pulled from the json string or JSON file passed as an arg
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--id', required=True, help='Cisco ID of the user to add')
        parser.add_argument('-f', '--file', default='settings.json', help='JSON settings file (settings.json used by default)')
        args = parser.parse_args()
        if os.path.isfile(args.file):
            settings = json.load(open(args.file, 'r'))
        else:
            settings = json.loads(args.file)

        # Create Intersight API instance
        # ----------------------
        api_instance = IntersightApiClient(host=settings['api_host'], private_key=settings['api_private_key'], api_key_id=settings['api_key_id'])

        # GET Users
        users_handle = iam_user_api.IamUserApi(api_instance)
        kwargs = dict(filter="Name eq '%s'" % args.id)
        users_result = users_handle.iam_users_get(**kwargs)

        # GET Permissions
        permissions_handle = iam_permission_api.IamPermissionApi(api_instance)
        kwargs = dict(filter="Subject eq '%s'" % users_result.results[0].moid)
        permissions_result = permissions_handle.iam_permissions_get(**kwargs)

        # DELETE Permissions
        permissions_delete_result = permissions_handle.iam_permissions_moid_delete(moid=permissions_result.results[0].moid)
        result['changed'] = True

        # DELETE Users
        users_delete_result = users_handle.iam_users_moid_delete(moid=users_result.results[0].moid)

    except Exception, err:
        print "Exception:", str(err)
        import traceback
        print '-' * 60
        traceback.print_exc(file=sys.stdout)
        print '-' * 60
        sys.exit(1)

    print json.dumps(result)
    sys.exit(0)
