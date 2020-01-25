# IamLdapBasePropertiesAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | Role and locale information of the user.   | [optional] 
**base_dn** | **str** | Base Distinguished Name (DN). Starting point from where server will search for users and groups.   | [optional] 
**bind_dn** | **str** | Distinguished Name (DN) of the user, that is used to authenticate against LDAP servers.   | [optional] 
**bind_method** | **str** | Authentication method to access LDAP servers.   | [optional] [default to 'LoginCredentials']
**domain** | **str** | The IPv4 domain that all users must be in.   | [optional] 
**enable_encryption** | **bool** | If enabled, the endpoint encrypts all information it sends to the LDAP server.   | [optional] 
**enable_group_authorization** | **bool** | If enabled, user authorization is also done at the group level for LDAP users not in the local user database.   | [optional] 
**filter** | **str** | Criteria to identify entries in search requests.   | [optional] 
**group_attribute** | **str** | Groups to which an LDAP entry belongs.   | [optional] 
**is_password_set** | **bool** |  | [optional] 
**nested_group_search_depth** | **int** | Search depth to look for a nested LDAP group in an LDAP group map.   | [optional] 
**password** | **str** | Password of the user, that is used to authenticate.   | [optional] 
**timeout** | **int** | LDAP authentication timeout duration, in seconds.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


