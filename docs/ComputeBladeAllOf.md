# ComputeBladeAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis_id** | **str** | The id of the chassis that the blade is located in.   | [optional] [readonly] 
**scaled_mode** | **str** |  | [optional] [readonly] 
**slot_id** | **int** |  | [optional] [readonly] 
**adapters** | [**list[AdapterUnit]**](AdapterUnit.md) | A reference to a adapterUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**bios_units** | [**list[BiosUnit]**](BiosUnit.md) | A reference to a biosUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**bmc** | [**ManagementController**](.md) |  | [optional] 
**board** | [**ComputeBoard**](.md) |  | [optional] 
**equipment_chassis** | [**EquipmentChassis**](.md) |  | [optional] 
**equipment_io_expanders** | [**list[EquipmentIoExpander]**](EquipmentIoExpander.md) | A reference to a equipmentIoExpander resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**generic_inventory_holders** | [**list[InventoryGenericInventoryHolder]**](InventoryGenericInventoryHolder.md) | A reference to a inventoryGenericInventoryHolder resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**locator_led** | [**EquipmentLocatorLed**](.md) |  | [optional] 
**pci_devices** | [**list[PciDevice]**](PciDevice.md) | A reference to a pciDevice resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**storage_enclosures** | [**list[StorageEnclosure]**](StorageEnclosure.md) | A reference to a storageEnclosure resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**top_system** | [**TopSystem**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


