# NetworkElement

Fabric Interconnect of a UCS. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_inband_interface_state** | **str** |  | [optional] [readonly] 
**fault_summary** | **int** |  | [optional] 
**inband_ip_address** | **str** | The Inband IP address of the network Element.   | [optional] [readonly] 
**inband_ip_gateway** | **str** | The Inband IP Gateway of the network Element.   | [optional] [readonly] 
**inband_ip_mask** | **str** |  | [optional] [readonly] 
**inband_vlan** | **int** |  | [optional] [readonly] 
**out_of_band_ip_address** | **str** |  | [optional] [readonly] 
**out_of_band_ip_gateway** | **str** |  | [optional] [readonly] 
**out_of_band_ip_mask** | **str** |  | [optional] [readonly] 
**out_of_band_mac** | **str** |  | [optional] [readonly] 
**switch_id** | **str** | The Switch Id of the network Element.    | [optional] [readonly] 
**cards** | [**list[EquipmentSwitchCard]**](EquipmentSwitchCard.md) | A reference to a equipmentSwitchCard resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**fanmodules** | [**list[EquipmentFanModule]**](EquipmentFanModule.md) | A reference to a equipmentFanModule resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**management_contoller** | [**ManagementController**](.md) |  | [optional] 
**management_entity** | [**ManagementEntity**](.md) |  | [optional] 
**psus** | [**list[EquipmentPsu]**](EquipmentPsu.md) | A reference to a equipmentPsu resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**top_system** | [**TopSystem**](.md) |  | [optional] 
**ucsm_running_firmware** | [**FirmwareRunningFirmware**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


