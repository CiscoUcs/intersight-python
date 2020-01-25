# HyperflexAppCatalog

A catalog for managing application settings for HyperFlex cluster configuration service. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The catalog version used in HyperFlex cluster configuration service.    | [optional] 
**feature_limit_external** | [**HyperflexFeatureLimitExternal**](.md) |  | [optional] 
**feature_limit_internal** | [**HyperflexFeatureLimitInternal**](.md) |  | [optional] 
**hxdp_versions** | [**list[HyperflexHxdpVersion]**](HyperflexHxdpVersion.md) | A reference to a hyperflexHxdpVersion resource. When the $expand query parameter is specified, the referenced resource is returned inline. The list of supported HyperFlex Data Platform versions.  | [optional] 
**hyperflex_capability_infos** | [**list[HyperflexCapabilityInfo]**](HyperflexCapabilityInfo.md) | A reference to a hyperflexCapabilityInfo resource. When the $expand query parameter is specified, the referenced resource is returned inline. Lists all supported HyperFlex feature capabilities and limitations.  | [optional] 
**hyperflex_software_compatibility_infos** | [**list[HclHyperflexSoftwareCompatibilityInfo]**](HclHyperflexSoftwareCompatibilityInfo.md) | A reference to a hclHyperflexSoftwareCompatibilityInfo resource. When the $expand query parameter is specified, the referenced resource is returned inline. Lists software compatibility information between different HyperFlex component versions like HXDP, Hypervisor, Drive Firmware, etc.  | [optional] 
**server_firmware_version** | [**HyperflexServerFirmwareVersion**](.md) |  | [optional] 
**server_model** | [**HyperflexServerModel**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


