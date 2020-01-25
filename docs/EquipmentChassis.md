# EquipmentChassis

A physical holder housing blade servers. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis_id** | **int** | The assigned identifier for a chassis.   | [optional] [readonly] 
**connection_path** | **str** | This field identifies the connectivity path for the chassis enclosure.   | [optional] [readonly] 
**connection_status** | **str** | This field identifies the connectivity status for the chassis enclosure.   | [optional] [readonly] 
**description** | **str** | This field is to provide description for chassis model.   | [optional] [readonly] 
**fault_summary** | **int** |  | [optional] 
**name** | **str** | This field identifies the name for the chassis enclosure.   | [optional] [readonly] 
**oper_state** | **str** |  | [optional] [readonly] 
**part_number** | **str** | Part Number identifier for the chassis enclosure.   | [optional] [readonly] 
**pid** | **str** | This field identifies the Product ID for the chassis enclosure.   | [optional] [readonly] 
**platform_type** | **str** |  | [optional] 
**product_name** | **str** | This field identifies the Product Name for the chassis enclosure.   | [optional] [readonly] 
**sku** | **str** | This field identifies the Stock Keeping Unit for the chassis enclosure.   | [optional] [readonly] 
**vid** | **str** | This field identifies the Vendor ID for the chassis enclosure.    | [optional] [readonly] 
**blades** | [**list[ComputeBlade]**](ComputeBlade.md) | A reference to a computeBlade resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**fanmodules** | [**list[EquipmentFanModule]**](EquipmentFanModule.md) | A reference to a equipmentFanModule resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**ioms** | [**list[EquipmentIoCard]**](EquipmentIoCard.md) | A reference to a equipmentIoCard resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**psus** | [**list[EquipmentPsu]**](EquipmentPsu.md) | A reference to a equipmentPsu resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**sasexpanders** | [**list[StorageSasExpander]**](StorageSasExpander.md) | A reference to a storageSasExpander resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**siocs** | [**list[EquipmentSystemIoController]**](EquipmentSystemIoController.md) | A reference to a equipmentSystemIoController resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**storage_enclosures** | [**list[StorageEnclosure]**](StorageEnclosure.md) | A reference to a storageEnclosure resource. When the $expand query parameter is specified, the referenced resource is returned inline. This field identifies the chassis enclosures.  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


