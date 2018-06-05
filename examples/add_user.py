#!/usr/bin/env python
"""Add an Intersight user by providing Cisco.com user ID and role via the Intersight API."""
import sys
import json
import argparse
from intersight.intersight_api_client import IntersightApiClient
from intersight.apis import iam_account_api
from intersight.apis import iam_user_api
from intersight.apis import iam_role_api
from intersight.apis import iam_end_point_role_api
from intersight.apis import iam_permission_api


def add_user(intersight_api_params, username, user_role='Account Administrator'):
    # Create Intersight API instance
    # ----------------------
    api_instance = IntersightApiClient(
        host=intersight_api_params['api_base_uri'],
        private_key=intersight_api_params['api_private_key_file'],
        api_key_id=intersight_api_params['api_key_id'],
    )

    # GET Users
    users_handle = iam_user_api.IamUserApi(api_instance)
    kwargs = dict(filter="Name eq '%s'" % username)
    users_result = users_handle.iam_users_get(**kwargs)

    # GET Accounts
    accounts_handle = iam_account_api.IamAccountApi(api_instance)
    accounts_result = accounts_handle.iam_accounts_get()

    if not users_result.results:
        # POST Users with Idpreference
        users_body = {
            'Name': username,
            'Idpreference': accounts_result.results[0].idpreferences[0],
        }
        users_result = users_handle.iam_users_post(users_body)
        result['changed'] = True

        # GET Users again
        kwargs = dict(filter="Name eq '%s'" % username)
        users_result = users_handle.iam_users_get(**kwargs)

    # GET Roles
    roles_handle = iam_role_api.IamRoleApi(api_instance)
    roles_result = roles_handle.iam_roles_get()
    for role in roles_result.results:
        if role.name == user_role:
            # GET EndPointRoles
            end_point_roles_handle = iam_end_point_role_api.IamEndPointRoleApi(api_instance)
            endpoint_roles = {}
            endpoint_roles['Read-Only'] = 'endpoint-readonly'
            endpoint_roles['Account Administrator'] = 'endpoint-admin'
            kwargs = dict(filter="RoleType eq '%s'" % endpoint_roles[user_role])
            end_point_roles_result = end_point_roles_handle.iam_end_point_roles_get(**kwargs)

            permissions_handle = iam_permission_api.IamPermissionApi(api_instance)
            kwargs = dict(filter="Subject eq '%s'" % users_result.results[0].moid)
            permissions_result = permissions_handle.iam_permissions_get(**kwargs)
            
            permissions_body = {
                'Subject': users_result.results[0].moid,
                'Type': 'User',
                'Account': accounts_result.results[0].account_moid,
                'EndPointRoles': end_point_roles_result.results,
                'Roles': [role],
            }
            if permissions_result.results:
                # PATCH Permissions with EndPointRoles
                permissions_result = permissions_handle.iam_permissions_moid_patch(permissions_result.results[0].moid, permissions_body)
            else:
                # POST Permissions with EndPointRoles
                permissions_result = permissions_handle.iam_permissions_post(permissions_body)
            break
    else:
        # for loop completed without finding a role
        print("Role not found:", user_role)


if __name__ == "__main__":
    result = dict(changed=False)

    try:
        # settings are pulled from the json string or JSON file passed as an arg
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--id', required=True, help='Cisco ID of the user to add')
        roles = ['Account Administrator', 'Read-Only']
        parser.add_argument('-r', '--role', choices=roles, required=True, help='Role of the user to add')
        help_str = 'JSON file with Intersight API parameters.  Default: intersight_api_params.json'
        parser.add_argument('-a', '--api_params', default='intersight_api_params.json', help=help_str)
        args = parser.parse_args()
        with open(args.api_params, 'r') as api_file:
            intersight_api_params = json.load(api_file)

        add_user(intersight_api_params, args.id, args.role)
        
    except Exception as err:
        print("Exception:", str(err))
        import traceback
        print('-' * 60)
        traceback.print_exc(file=sys.stdout)
        print('-' * 60)
        sys.exit(1)

    print(json.dumps(result))
    sys.exit(0)
