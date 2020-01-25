# IamEndPointUserRoleAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_password** | **bool** | Denotes whether password has changed.   | [optional] [readonly] 
**enabled** | **bool** | Enables the user account on the endpoint.   | [optional] 
**is_password_set** | **bool** |  | [optional] 
**password** | **str** | Valid login password of the user.    | [optional] 
**end_point_role** | [**list[IamEndPointRole]**](IamEndPointRole.md) | A reference to a iamEndPointRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. Roles.  | [optional] 
**end_point_user** | [**IamEndPointUser**](.md) |  | [optional] 
**end_point_user_policy** | [**IamEndPointUserPolicy**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


