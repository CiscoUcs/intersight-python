#!/usr/bin/env python
"""Add an Intersight user by providing Cisco.com user ID and role via the Intersight API."""
import sys
import json
import argparse
from intersight.intersight_api_client import IntersightApiClient
from intersight.apis import iam_permission_api
from intersight.apis import iam_idp_reference_api
from intersight.apis import iam_user_api


def add_user(intersight_api_params, username, user_role='Account Administrator'):
    # Create Intersight API instance
    # ----------------------
    api_instance = IntersightApiClient(
        host=intersight_api_params['api_base_uri'],
        private_key=intersight_api_params['api_private_key_file'],
        api_key_id=intersight_api_params['api_key_id'],
    )

    # GET Permissions
    permissions_handle = iam_permission_api.IamPermissionApi(api_instance)
    kwargs = dict(filter="Name eq '%s'" % user_role)
    permissions_result = permissions_handle.iam_permissions_get(**kwargs)

    if permissions_result.results:
        # GET IdpReference
        idp_reference_handle = iam_idp_reference_api.IamIdpReferenceApi(api_instance)
        idp_reference_name = 'Cisco'
        kwargs = dict(filter="Name eq '%s'" % idp_reference_name)
        idp_reference_result = idp_reference_handle.iam_idp_references_get(**kwargs)
        if idp_reference_result.results:
            user_matches = False
            # GET Users
            users_handle = iam_user_api.IamUserApi(api_instance)
            kwargs = dict(filter="Email eq '%s'" % username)
            users_result = users_handle.iam_users_get(**kwargs)
            if (
                    users_result.results and
                    users_result.results[0].permissions[0].moid == permissions_result.results[0].moid and
                    users_result.results[0].idpreference.moid == idp_reference_result.results[0].moid
               ):
                user_matches = True

            if not user_matches:
                # POST Users with Permissions and IdpReference
                users_body = {
                    'Email': username,
                    'Idpreference': idp_reference_result.results[0].moid,
                    'Permissions': [permissions_result.results[0].moid],
                }
                users_result = users_handle.iam_users_post(users_body)
                result['changed'] = True
            else:   # user exists and IdP/Permissions match
                print('User exists with requested role:', username)
        else:
            print('Could not find IdP', idp_reference_name)
    else:
        print('Invalid user role', user_role)


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
