# HyperflexExtIscsiStoragePolicyAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_state** | **bool** | Enable or disable external FCoE storage configuration.   | [optional] 
**exta_traffic** | [**HyperflexNamedVlan**](HyperflexNamedVlan.md) |  | [optional] 
**extb_traffic** | [**HyperflexNamedVlan**](HyperflexNamedVlan.md) |  | [optional] 
**cluster_profiles** | [**list[HyperflexClusterProfile]**](HyperflexClusterProfile.md) | A reference to a hyperflexClusterProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of cluster profiles using this policy.  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


