# IamLdapGroupAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | LDAP server domain the Group resides in.   | [optional] 
**name** | **str** | LDAP Group name in the LDAP server database.    | [optional] 
**end_point_role** | [**list[IamEndPointRole]**](IamEndPointRole.md) | A reference to a iamEndPointRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. Role assigned to all users in this LDAP server group. This can be one of read-only, user, admin.  | [optional] 
**ldap_policy** | [**IamLdapPolicy**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


