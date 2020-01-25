# HclHyperflexSoftwareCompatibilityInfo

Lists software compatibility information between different HperFlex component versions like HyperFlex Data Platform, Hypervisor, Drive Firmware, etc. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraints** | [**list[HclConstraint]**](HclConstraint.md) |  | [optional] 
**hxdp_version** | **str** | HXDP component software version.   | [optional] 
**hypervisor_type** | **str** | Type fo Hypervisor the HyperFlex components versions are compatible with. For example ESX, Hyperv or KVM.   | [optional] [default to 'Unknown']
**hypervisor_version** | **str** | Hypervisor component software version.   | [optional] 
**server_fw_version** | **str** | UCS Server Firmware component software version.    | [optional] 
**app_catalog** | [**HyperflexAppCatalog**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


