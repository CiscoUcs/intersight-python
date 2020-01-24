# EquipmentFanModuleAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | This field is to provide description for the fan module.   | [optional] [readonly] 
**module_id** | **int** | This field acts as the identifier for this particular Module, within the Fabric Interconnect.   | [optional] [readonly] 
**oper_state** | **str** | This field is used to indicate this fan module&#39;s operational state.   | [optional] [readonly] 
**part_number** | **str** | This field identifies the Part Number for this Fan Module.   | [optional] [readonly] 
**pid** | **str** | This field identifies the Product ID for the fan module.   | [optional] [readonly] 
**presence** | **str** | This field is used to indicate this fan module&#39;s presence.   | [optional] [readonly] 
**sku** | **str** | This field identifies the Stockkeeping Unit for this Fan Module.   | [optional] [readonly] 
**tray_id** | **int** | Tray identifier for the fan module.   | [optional] [readonly] 
**vid** | **str** | This field identifies the Vendor ID for this Fan Module.    | [optional] [readonly] 
**compute_rack_unit** | [**ComputeRackUnit**](.md) |  | [optional] 
**equipment_chassis** | [**EquipmentChassis**](.md) |  | [optional] 
**equipment_rack_enclosure** | [**EquipmentRackEnclosure**](.md) |  | [optional] 
**fans** | [**list[EquipmentFan]**](EquipmentFan.md) | A reference to a equipmentFan resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**network_element** | [**NetworkElement**](.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


