# IamResourceRolesAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_point_roles** | [**list[IamEndPointRole]**](IamEndPointRole.md) | A reference to a iamEndPointRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. The end point roles assigned to this permission. The user can perform end point operations like GUI/CLI cross launch.  | [optional] [readonly] 
**permission** | [**IamPermission**](.md) |  | [optional] 
**resource** | [**MoBaseMo**](.md) |  | [optional] 
**roles** | [**list[IamRole]**](IamRole.md) | A reference to a iamRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. The roles assigned to this resource. Role is a collection of privilege sets. Roles are assigned to a user or group using the permission object.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


