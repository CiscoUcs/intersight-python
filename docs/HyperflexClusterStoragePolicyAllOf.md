# HyperflexClusterStoragePolicyAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_partition_cleanup** | **bool** | If enabled, formats existing disk partitions (destroys all user data).   | [optional] 
**logical_avalability_zone_config** | [**HyperflexLogicalAvailabilityZone**](HyperflexLogicalAvailabilityZone.md) |  | [optional] 
**vdi_optimization** | **bool** | Enable or disable VDI optimization (hybrid HyperFlex systems only).    | [optional] 
**cluster_profiles** | [**list[HyperflexClusterProfile]**](HyperflexClusterProfile.md) | A reference to a hyperflexClusterProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of cluster profiles using this policy.  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


