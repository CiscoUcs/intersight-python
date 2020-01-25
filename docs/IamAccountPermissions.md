# IamAccountPermissions

Users can log in through the base URL (https://intersight.com) or account-specific URLs. When the Intersight user logs in through the base URL, Intersight identifies the accounts and permissions within each account which the user has access to. In case multiple permissions are identified, the user and session objects are created in the onboarding-user account, and the session object is updated with account and permission information. Intersight GUI uses this information to show available accounts and permissions for the user to select. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_identifier** | **str** | MOID of the account which a user can select after authentication.   | [optional] [readonly] 
**account_name** | **str** | Name of the account which a user can select after authentication.   | [optional] [readonly] 
**account_status** | **str** | Status of the account. Account remains inactive until a device is claimed to the account.   | [optional] [readonly] 
**permissions** | [**list[IamPermissionReference]**](IamPermissionReference.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


