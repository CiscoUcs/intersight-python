#!/usr/bin/env python
"""Delete an Intersight user by Cisco.com ID via the Intersight API."""
import sys
import json
import argparse
from intersight.intersight_api_client import IntersightApiClient
from intersight.apis import iam_user_api


def delete_user(intersight_api_params, user_email):
# Create Intersight API instance
    # ----------------------
    api_instance = IntersightApiClient(
        host=intersight_api_params['api_base_uri'],
        private_key=intersight_api_params['api_private_key_file'],
        api_key_id=intersight_api_params['api_key_id'],
    )

    try:
        # GET Users
        users_handle = iam_user_api.IamUserApi(api_instance)
        kwargs = dict(filter="Email eq '%s'" % user_email)
        users_result = users_handle.iam_users_get(**kwargs)
        if users_result.results:
            # DELETE Users
            users_delete_result = users_handle.iam_users_moid_delete(moid=users_result.results[0].moid)
        else:
            print("User not found:", user_email)

    except Exception as err:
        print("Exception:", str(err))
        import traceback
        print('-' * 60)
        traceback.print_exc(file=sys.stdout)
        print('-' * 60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--id', required=True, help='Cisco email ID of the user to delete')
    help_str = 'JSON file with Intersight API parameters.  Default: intersight_api_params.json'
    parser.add_argument('-a', '--api_params', default='intersight_api_params.json', help=help_str)
    args = parser.parse_args()
    with open(args.api_params, 'r') as api_file:
        intersight_api_params = json.load(api_file)

    delete_user(intersight_api_params, args.id)

    sys.exit(0)
