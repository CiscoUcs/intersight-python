# EquipmentRackEnclosureAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enclosure_id** | **int** |  | [optional] [readonly] 
**fanmodules** | [**list[EquipmentFanModule]**](EquipmentFanModule.md) | A reference to a equipmentFanModule resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**psus** | [**list[EquipmentPsu]**](EquipmentPsu.md) | A reference to a equipmentPsu resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**slots** | [**list[EquipmentRackEnclosureSlot]**](EquipmentRackEnclosureSlot.md) | A reference to a equipmentRackEnclosureSlot resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


