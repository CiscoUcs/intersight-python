# IamEndPointRoleAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the end point role.    | [optional] [readonly] 
**role_type** | **str** | User specified tags to roles like as ep-admin or ep-readonly.   | [optional] [readonly] 
**type** | **str** | The type of the end point like Cisco UCS Fabric Interconnect or Cisco IMC.     | [optional] [readonly] [default to '']
**account** | [**IamAccount**](.md) |  | [optional] 
**end_point_privileges** | [**list[IamEndPointPrivilege]**](IamEndPointPrivilege.md) | A reference to a iamEndPointPrivilege resource. When the $expand query parameter is specified, the referenced resource is returned inline. Privileges assigned to this end point role. These privileges are assigned to users using end point roles to perform operations such as GUI/CLI cross launch.  | [optional] [readonly] 
**system** | [**IamSystem**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


