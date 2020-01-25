# IamAccountAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Intersight account. By default, name is same as the MoID of the account.   | [optional] 
**status** | **str** | Status of the account. To activate the Intersight account, claim a device to the account.    | [optional] [readonly] 
**app_registrations** | [**list[IamAppRegistration]**](IamAppRegistration.md) | A reference to a iamAppRegistration resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of registered OAuth2 applications created from the account.  | [optional] [readonly] 
**domain_groups** | [**list[IamDomainGroup]**](IamDomainGroup.md) | A reference to a iamDomainGroup resource. When the $expand query parameter is specified, the referenced resource is returned inline. The domain Groups are configured in an account for scaling purpose. Currently, only onboarding-device account has multiple domain groups and other accounts have only one domain group per account.  | [optional] [readonly] 
**end_point_roles** | [**list[IamEndPointRole]**](IamEndPointRole.md) | A reference to a iamEndPointRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. User defined end point roles. These roles are assigned to Intersight users to perform end point operations such as GUI/CLI cross launch.  | [optional] [readonly] 
**idpreferences** | [**list[IamIdpReference]**](IamIdpReference.md) | A reference to a iamIdpReference resource. When the $expand query parameter is specified, the referenced resource is returned inline. System created IdPs configured for authentication in an account. By default Cisco IdP is created upon account creation.  | [optional] [readonly] 
**idps** | [**list[IamIdp]**](IamIdp.md) | A reference to a iamIdp resource. When the $expand query parameter is specified, the referenced resource is returned inline. IdPs configured for authentication in an account. IdP object handles the third-party IdP details.  | [optional] [readonly] 
**permissions** | [**list[IamPermission]**](IamPermission.md) | A reference to a iamPermission resource. When the $expand query parameter is specified, the referenced resource is returned inline. System defined permissions within an account. Permission provides a way to assign roles to a user or user group to perform operations on object hierarchy.  | [optional] [readonly] 
**privilege_sets** | [**list[IamPrivilegeSet]**](IamPrivilegeSet.md) | A reference to a iamPrivilegeSet resource. When the $expand query parameter is specified, the referenced resource is returned inline. User defined privilege sets. Privilege set is a collection of privileges. Privilege sets are assigned to a user using roles.  | [optional] [readonly] 
**privileges** | [**list[IamPrivilege]**](IamPrivilege.md) | A reference to a iamPrivilege resource. When the $expand query parameter is specified, the referenced resource is returned inline. Privileges are assigned to a user using privilege sets and roles. Privileges define user permissions and the actions a user can perform in Intersight.  | [optional] [readonly] 
**resource_limits** | [**IamResourceLimits**](.md) |  | [optional] 
**roles** | [**list[IamRole]**](IamRole.md) | A reference to a iamRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. User defined roles created within an account. Role is a collection of privilege sets. Roles are assigned to user using permission object.  | [optional] [readonly] 
**security_holder** | [**IamSecurityHolder**](.md) |  | [optional] 
**session_limits** | [**IamSessionLimits**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


