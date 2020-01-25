# IamPermission

Permission provides a way to assign roles to a user or user group to perform operations on object hierarchy. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The informative description about each permission.   | [optional] 
**name** | **str** | The name of the permission which has to be granted to user.      | [optional] 
**account** | [**IamAccount**](.md) |  | [optional] 
**end_point_roles** | [**list[IamEndPointRole]**](IamEndPointRole.md) | A reference to a iamEndPointRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. The end point roles assigned to this permission. The user can perform end point operations like GUI/CLI cross launch.  | [optional] [readonly] 
**resource_roles** | [**list[IamResourceRoles]**](IamResourceRoles.md) | A reference to a iamResourceRoles resource. When the $expand query parameter is specified, the referenced resource is returned inline. The resource and roles assigned to this permission. Resource role specifies the organization and the collection of roles the permission has on the organization.  | [optional] 
**roles** | [**list[IamRole]**](IamRole.md) | A reference to a iamRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. The roles assigned to this permission. Role is a collection of privilege sets. Roles are assigned to a user using the permission object.  | [optional] 
**user_groups** | [**list[IamUserGroup]**](IamUserGroup.md) | A reference to a iamUserGroup resource. When the $expand query parameter is specified, the referenced resource is returned inline. A collection of references to the [iam.UserGroup](mo://iam.UserGroup) Managed Object.  When this managed object is deleted, the referenced [iam.UserGroup](mo://iam.UserGroup) MOs unset their reference to this deleted MO.  | [optional] 
**users** | [**list[IamUser]**](IamUser.md) | A reference to a iamUser resource. When the $expand query parameter is specified, the referenced resource is returned inline. A collection of references to the [iam.User](mo://iam.User) Managed Object.  When this managed object is deleted, the referenced [iam.User](mo://iam.User) MOs unset their reference to this deleted MO.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


