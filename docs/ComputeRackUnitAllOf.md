# ComputeRackUnitAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **int** |  | [optional] [readonly] 
**adapters** | [**list[AdapterUnit]**](AdapterUnit.md) | A reference to a adapterUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**bios_bootmode** | [**BiosBootMode**](.md) |  | [optional] 
**biosunits** | [**list[BiosUnit]**](BiosUnit.md) | A reference to a biosUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**bmc** | [**ManagementController**](.md) |  | [optional] 
**board** | [**ComputeBoard**](.md) |  | [optional] 
**boot_device_bootmode** | [**BootDeviceBootMode**](.md) |  | [optional] 
**fanmodules** | [**list[EquipmentFanModule]**](EquipmentFanModule.md) | A reference to a equipmentFanModule resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**generic_inventory_holders** | [**list[InventoryGenericInventoryHolder]**](InventoryGenericInventoryHolder.md) | A reference to a inventoryGenericInventoryHolder resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**locator_led** | [**EquipmentLocatorLed**](.md) |  | [optional] 
**pci_devices** | [**list[PciDevice]**](PciDevice.md) | A reference to a pciDevice resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**psus** | [**list[EquipmentPsu]**](EquipmentPsu.md) | A reference to a equipmentPsu resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**rack_enclosure_slot** | [**EquipmentRackEnclosureSlot**](.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**sas_expanders** | [**list[StorageSasExpander]**](StorageSasExpander.md) | A reference to a storageSasExpander resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] 
**storage_enclosures** | [**list[StorageEnclosure]**](StorageEnclosure.md) | A reference to a storageEnclosure resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**top_system** | [**TopSystem**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


