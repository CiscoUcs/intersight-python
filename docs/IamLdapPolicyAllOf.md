# IamLdapPolicyAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_properties** | [**IamLdapBaseProperties**](IamLdapBaseProperties.md) |  | [optional] 
**dns_parameters** | [**IamLdapDnsParameters**](IamLdapDnsParameters.md) |  | [optional] 
**enable_dns** | **bool** | Enables DNS to access LDAP servers.   | [optional] 
**enabled** | **bool** | LDAP server performs authentication.   | [optional] 
**user_search_precedence** | **str** | Search precedence between local user database and LDAP user database.    | [optional] [default to 'LocalUserDb']
**appliance_account** | [**IamAccount**](.md) |  | [optional] 
**groups** | [**list[IamLdapGroup]**](IamLdapGroup.md) | A reference to a iamLdapGroup resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to collection of LDAP Groups.  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 
**profiles** | [**list[PolicyAbstractConfigProfile]**](PolicyAbstractConfigProfile.md) | A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the profile object.  | [optional] 
**providers** | [**list[IamLdapProvider]**](IamLdapProvider.md) | A reference to a iamLdapProvider resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to collection of LDAP Providers.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


