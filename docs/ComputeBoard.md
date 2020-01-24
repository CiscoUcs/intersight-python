# ComputeBoard

Mother board of a server. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**board_id** | **int** |  | [optional] [readonly] 
**cpu_type_controller** | **str** |  | [optional] [readonly] 
**oper_power_state** | **str** |  | [optional] [readonly] 
**presence** | **str** |  | [optional] [readonly] 
**compute_blade** | [**ComputeBlade**](.md) |  | [optional] 
**compute_rack_unit** | [**ComputeRackUnit**](.md) |  | [optional] 
**equipment_tpms** | [**list[EquipmentTpm]**](EquipmentTpm.md) | A reference to a equipmentTpm resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**graphics_cards** | [**list[GraphicsCard]**](GraphicsCard.md) | A reference to a graphicsCard resource. When the $expand query parameter is specified, the referenced resource is returned inline. It shows Graphics cards present in a server.  | [optional] [readonly] 
**memory_arrays** | [**list[MemoryArray]**](MemoryArray.md) | A reference to a memoryArray resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**pci_coprocessor_cards** | [**list[PciCoprocessorCard]**](PciCoprocessorCard.md) | A reference to a pciCoprocessorCard resource. When the $expand query parameter is specified, the referenced resource is returned inline. It shows PCI CoprocessorCard present in a server.  | [optional] [readonly] 
**pci_switch** | [**list[PciSwitch]**](PciSwitch.md) | A reference to a pciSwitch resource. When the $expand query parameter is specified, the referenced resource is returned inline. It shows PCI Switches presen in a server.  | [optional] [readonly] 
**persistent_memory_configuration** | [**MemoryPersistentMemoryConfiguration**](.md) |  | [optional] 
**processors** | [**list[ProcessorUnit]**](ProcessorUnit.md) | A reference to a processorUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**security_units** | [**list[SecurityUnit]**](SecurityUnit.md) | A reference to a securityUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**storage_controllers** | [**list[StorageController]**](StorageController.md) | A reference to a storageController resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**storage_flex_flash_controllers** | [**list[StorageFlexFlashController]**](StorageFlexFlashController.md) | A reference to a storageFlexFlashController resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**storage_flex_util_controllers** | [**list[StorageFlexUtilController]**](StorageFlexUtilController.md) | A reference to a storageFlexUtilController resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


