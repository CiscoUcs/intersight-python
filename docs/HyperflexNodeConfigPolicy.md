# HyperflexNodeConfigPolicy

A policy specifying node details such as management and storage data IP ranges. For HyperFlex Edge, storage data IP range is pre-defined. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_ip_range** | [**HyperflexIpAddrRange**](HyperflexIpAddrRange.md) |  | [optional] 
**hxdp_ip_range** | [**HyperflexIpAddrRange**](HyperflexIpAddrRange.md) |  | [optional] 
**mgmt_ip_range** | [**HyperflexIpAddrRange**](HyperflexIpAddrRange.md) |  | [optional] 
**node_name_prefix** | **str** | The node name prefix that is used to automatically generate the default hostname for each server.  A dash (-) will be appended to the prefix followed by the node number to form a hostname. This default naming scheme can be manually overridden in the node configuration. The maximum length of a prefix is 60, must only contain alphanumeric characters or dash (-), and must start with an alphanumeric character.     | [optional] 
**cluster_profiles** | [**list[HyperflexClusterProfile]**](HyperflexClusterProfile.md) | A reference to a hyperflexClusterProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of cluster profiles using this policy.  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


