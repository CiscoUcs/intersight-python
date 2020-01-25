# IamSystem

System is the top level object in the Intersight. All other objects which can be accessed globally are added to system object, like privilege sets and privileges can be shared by multiple roles and privilege sets. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_point_privileges** | [**list[IamEndPointPrivilege]**](IamEndPointPrivilege.md) | A reference to a iamEndPointPrivilege resource. When the $expand query parameter is specified, the referenced resource is returned inline. Privileges defined in end point devices such as UCS Fabric Interconnect, IMC, and HyperFlex managed by Intersight. These privileges are assigned to Intersight users using end point roles to perform operations such as GUI/CLI cross launch.  | [optional] [readonly] 
**end_point_roles** | [**list[IamEndPointRole]**](IamEndPointRole.md) | A reference to a iamEndPointRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. Roles defined in end point devices such as UCS Fabric Interconnect, IMC, HyperFlex managed by Intersight. These roles are assigned to Intersight users to perform end point operations such as GUI/CLI cross launch.  | [optional] [readonly] 
**idp** | [**IamIdp**](.md) |  | [optional] 
**privilege_sets** | [**list[IamPrivilegeSet]**](IamPrivilegeSet.md) | A reference to a iamPrivilegeSet resource. When the $expand query parameter is specified, the referenced resource is returned inline. Privilege set is a collection of privileges. Privilege sets are assigned to a user using roles.  | [optional] [readonly] 
**privileges** | [**list[IamPrivilege]**](IamPrivilege.md) | A reference to a iamPrivilege resource. When the $expand query parameter is specified, the referenced resource is returned inline. Privileges are assigned to a user using privilege sets and roles. Privileges define user permissions and the actions a user can perform in Intersight.  | [optional] [readonly] 
**roles** | [**list[IamRole]**](IamRole.md) | A reference to a iamRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. A role is a collection of privilege sets that are assigned to a user using a permission object.  | [optional] [readonly] 
**service_provider** | [**IamServiceProvider**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


