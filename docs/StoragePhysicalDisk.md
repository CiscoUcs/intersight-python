# StoragePhysicalDisk

Physical Disk on a server. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_size** | **str** | The block size of the physical disk.   | [optional] [readonly] 
**bootable** | **str** |  | [optional] [readonly] 
**configuration_checkpoint** | **str** |  | [optional] [readonly] 
**configuration_state** | **str** |  | [optional] [readonly] 
**discovered_path** | **str** |  | [optional] [readonly] 
**disk_id** | **str** |  | [optional] [readonly] 
**disk_state** | **str** | This field identifies the health of the disk.   | [optional] [readonly] 
**drive_firmware** | **str** |  | [optional] 
**drive_state** | **str** |  | [optional] [readonly] 
**fde_capable** | **str** |  | [optional] 
**link_speed** | **str** |  | [optional] [readonly] 
**link_state** | **str** |  | [optional] [readonly] 
**num_blocks** | **str** | The number of blocks present on the physical disk.   | [optional] [readonly] 
**oper_power_state** | **str** |  | [optional] [readonly] 
**oper_qualifier_reason** | **str** |  | [optional] [readonly] 
**operability** | **str** |  | [optional] [readonly] 
**physical_block_size** | **str** |  | [optional] [readonly] 
**pid** | **str** | This field identifies the Product ID for physicalDisk.   | [optional] [readonly] 
**presence** | **str** |  | [optional] [readonly] 
**protocol** | **str** |  | [optional] [readonly] 
**raw_size** | **str** |  | [optional] [readonly] 
**secured** | **str** | This field identifies whether the disk is encrypted.   | [optional] 
**size** | **str** |  | [optional] [readonly] 
**thermal** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**variant_type** | **str** |  | [optional] [readonly] 
**locator_led** | [**EquipmentLocatorLed**](.md) |  | [optional] 
**physical_disk_extensions** | [**list[StoragePhysicalDiskExtension]**](StoragePhysicalDiskExtension.md) | A reference to a storagePhysicalDiskExtension resource. When the $expand query parameter is specified, the referenced resource is returned inline. The physical connectivity between a SCSI controller and physical disks.  | [optional] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**running_firmware** | [**list[FirmwareRunningFirmware]**](FirmwareRunningFirmware.md) | A reference to a firmwareRunningFirmware resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**sas_ports** | [**list[StorageSasPort]**](StorageSasPort.md) | A reference to a storageSasPort resource. When the $expand query parameter is specified, the referenced resource is returned inline. It is a reference to SAS Port to physical disk.  | [optional] [readonly] 
**storage_controller** | [**StorageController**](.md) |  | [optional] 
**storage_enclosure** | [**StorageEnclosure**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


