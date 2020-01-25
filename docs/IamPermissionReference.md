# IamPermissionReference

Users can log in through the base URL (https://intersight.com) or account-specific URLs. When the Intersight user logs in through the base URL, Intersight identifies the accounts and permissions within each account which the user has access to. In case multiple permissions are identified, the user and session objects are created in the onboarding-user account, and the session object is updated with account and permission information. Intersight GUI uses this information to show available accounts and permissions for the user to select. PermissionReference type is used to store permission information of an account. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission_identifier** | **str** | MOID of the permission which user has access to.   | [optional] [readonly] 
**permission_name** | **str** | Name of the permission which user has access to.    | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


