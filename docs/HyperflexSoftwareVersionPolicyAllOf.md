# HyperflexSoftwareVersionPolicyAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hxdp_version** | **str** | Desired HyperFlex Data Platform software version to apply on the HyperFlex cluster.   | [optional] 
**server_firmware_version** | **str** | Desired server firmware version to apply on the HyperFlex Cluster.    | [optional] 
**cluster_profiles** | [**list[HyperflexClusterProfile]**](HyperflexClusterProfile.md) | A reference to a hyperflexClusterProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of cluster profiles using this policy.  | [optional] 
**hxdp_version_info** | [**SoftwareHyperflexDistributable**](.md) |  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 
**server_firmware_version_info** | [**FirmwareDistributable**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


