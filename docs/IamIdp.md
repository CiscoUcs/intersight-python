# IamIdp

The SAML identity provider such as Cisco, that has been used to log in to Intersight. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Email domain name of the user for this IdP. When a user enters an email during login in the Intersight home page, the IdP is picked by matching this domain name with the email domain name for authentication.   | [optional] 
**idp_entity_id** | **str** | The Entity ID of the IdP. In SAML, the entity ID uniquely identifies the IdP or Service Provider.   | [optional] [readonly] 
**metadata** | **str** | SAML metadata of the IdP.   | [optional] 
**name** | **str** | The name of the Identity Provider, for example Cisco, Okta, or OneID.   | [optional] 
**type** | **str** | Authentication protocol used by the IdP.    | [optional] [default to 'saml']
**account** | [**IamAccount**](.md) |  | [optional] 
**system** | [**IamSystem**](.md) |  | [optional] 
**user_preferences** | [**list[IamUserPreference]**](IamUserPreference.md) | A reference to a iamUserPreference resource. When the $expand query parameter is specified, the referenced resource is returned inline. The UI preference object for each user logged in through this IdP.  | [optional] [readonly] 
**usergroups** | [**list[IamUserGroup]**](IamUserGroup.md) | A reference to a iamUserGroup resource. When the $expand query parameter is specified, the referenced resource is returned inline. User groups added in an IdP. User group provides a way to configure permission assignment for a group of users based on the IdP attributes received after authentication.  | [optional] 
**users** | [**list[IamUser]**](IamUser.md) | A reference to a iamUser resource. When the $expand query parameter is specified, the referenced resource is returned inline. Added or logged in users of an IdP who can access an Intersight account.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


