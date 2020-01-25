# IamUserGroup

User Group provides a way to assign permissions to a group of users based on the IdP attributes received after authentication. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the user group which the dynamic user belongs to.    | [optional] 
**idp** | [**IamIdp**](.md) |  | [optional] 
**idpreference** | [**IamIdpReference**](.md) |  | [optional] 
**permissions** | [**list[IamPermission]**](IamPermission.md) | A reference to a iamPermission resource. When the $expand query parameter is specified, the referenced resource is returned inline. Permissions assigned to the user group. Permission provides a way to assign roles to a user or user group to perform operations on object hierarchy.  | [optional] 
**qualifier** | [**IamQualifier**](.md) |  | [optional] 
**users** | [**list[IamUser]**](IamUser.md) | A reference to a iamUser resource. When the $expand query parameter is specified, the referenced resource is returned inline. Users logged in using this user group.  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


