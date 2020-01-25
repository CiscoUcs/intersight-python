# HyperflexExtFcStoragePolicyAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_state** | **bool** | Enables or disables external FC storage configuration.   | [optional] 
**exta_traffic** | [**HyperflexNamedVsan**](HyperflexNamedVsan.md) |  | [optional] 
**extb_traffic** | [**HyperflexNamedVsan**](HyperflexNamedVsan.md) |  | [optional] 
**wwxn_prefix_range** | [**HyperflexWwxnPrefixRange**](HyperflexWwxnPrefixRange.md) |  | [optional] 
**cluster_profiles** | [**list[HyperflexClusterProfile]**](HyperflexClusterProfile.md) | A reference to a hyperflexClusterProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of cluster profiles using this policy.  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


