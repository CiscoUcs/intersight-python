# HyperflexProxySettingPolicyAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | HTTP Proxy server FQDN or IP.   | [optional] 
**is_password_set** | **bool** |  | [optional] 
**password** | **str** | The password for the HTTP Proxy.   | [optional] 
**port** | **int** | The HTTP Proxy port number.  The port number of the HTTP proxy must be between 1 and 65535, inclusive.    | [optional] 
**username** | **str** | The username for the HTTP Proxy.    | [optional] 
**cluster_profiles** | [**list[HyperflexClusterProfile]**](HyperflexClusterProfile.md) | A reference to a hyperflexClusterProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of cluster profiles using this policy.  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


