#!/usr/bin/env python

import sys
import json
import argparse
import os.path
from intersight.intersight_api_client import IntersightApiClient
from intersight.apis import iam_account_api
from intersight.apis import iam_user_api
from intersight.apis import iam_role_api
from intersight.apis import iam_end_point_role_api
from intersight.apis import iam_permission_api

if __name__ == "__main__":
    result = dict(changed=False)

    try:
        # settings are pulled from the json string or JSON file passed as an arg
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--id', required=True, help='Cisco ID of the user to add')
        roles = ['Account Administrator', 'Read-Only']
        parser.add_argument('-r', '--role', choices=roles, required=True, help='Role of the user to add')
        parser.add_argument('-f', '--file', default='settings.json', help='JSON settings file (settings.json used by default)')
        args = parser.parse_args()
        if os.path.isfile(args.file):
            settings = json.load(open(args.file, 'r'))
        else:
            settings = json.loads(args.file)

        # Create Intersight API instance
        # ----------------------
        api_instance = IntersightApiClient(host=settings['api_host'], private_key=settings['api_private_key'], api_key_id=settings['api_key_id'])

        # GET Accounts
        accounts_handle = iam_account_api.IamAccountApi(api_instance)
        accounts_result = accounts_handle.iam_accounts_get()

        # POST Users with Idpreference
        users_handle = iam_user_api.IamUserApi(api_instance)
        users_body = {
            'Name': args.id,
            'Idpreference': accounts_result.results[0].idpreferences[0],
        }
        users_result = users_handle.iam_users_post(users_body)
        result['changed'] = True

        # GET Users
        kwargs = dict(filter="Name eq '%s'" % args.id)
        users_result = users_handle.iam_users_get(**kwargs)

        # GET Roles
        roles_handle = iam_role_api.IamRoleApi(api_instance)
        roles_result = roles_handle.iam_roles_get()
        for role in roles_result.results:
            if role.name == args.role:
                break

        # GET EndPointRoles
        end_point_roles_handle = iam_end_point_role_api.IamEndPointRoleApi(api_instance)
        endpoint_roles = {}
        endpoint_roles['Read-Only'] = 'endpoint-readonly'
        endpoint_roles['Account Administrator'] = 'endpoint-admin'
        kwargs = dict(filter="RoleType eq '%s'" % endpoint_roles[args.role])
        end_point_roles_result = end_point_roles_handle.iam_end_point_roles_get(**kwargs)

        # POST Permissions with EndPointRoles
        permissions_handle = iam_permission_api.IamPermissionApi(api_instance)
        permissions_body = {
            'Subject': users_result.results[0].moid,
            'Type': 'User',
            'Account': accounts_result.results[0].account_moid,
            'EndPointRoles': end_point_roles_result.results,
            'Roles': [role],
        }
        permissions_result = permissions_handle.iam_permissions_post(permissions_body)

    except Exception, err:
        print "Exception:", str(err)
        import traceback
        print '-' * 60
        traceback.print_exc(file=sys.stdout)
        print '-' * 60
        sys.exit(1)

    print json.dumps(result)
    sys.exit(0)
