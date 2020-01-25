# StorageControllerAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_flags** | **str** |  | [optional] [readonly] 
**controller_id** | **str** | It shows the Id of controller.   | [optional] [readonly] 
**controller_status** | **str** | It shows the current status of controller.   | [optional] [readonly] 
**hw_revision** | **str** | It shows the hardware revision of controller.   | [optional] [readonly] 
**oob_interface_supported** | **str** | It shows CIMC support for out-of-band configuration of controller.   | [optional] [readonly] 
**oper_state** | **str** | It shows the current operational state of controller.   | [optional] [readonly] 
**operability** | **str** |  | [optional] [readonly] 
**pci_addr** | **str** | It shows the current pci address of controller.   | [optional] [readonly] 
**pci_slot** | **str** | It shows the pci slot name for the controller.   | [optional] [readonly] 
**presence** | **str** | It shows physical presence or absence of the controller on server.   | [optional] [readonly] 
**raid_support** | **str** | It shows the RAID levels supported by controller.   | [optional] [readonly] 
**rebuild_rate** | **str** |  | [optional] [readonly] 
**self_encrypt_enabled** | **str** |  | [optional] 
**type** | **str** | Controller types are SAS, SATA, PCH, NVME.    | [optional] [readonly] 
**compute_board** | [**ComputeBoard**](.md) |  | [optional] 
**physical_disk_extensions** | [**list[StoragePhysicalDiskExtension]**](StoragePhysicalDiskExtension.md) | A reference to a storagePhysicalDiskExtension resource. When the $expand query parameter is specified, the referenced resource is returned inline. Indicates a SCSI controller has physical connectivity to specified physical disk.  | [optional] [readonly] 
**physical_disks** | [**list[StoragePhysicalDisk]**](StoragePhysicalDisk.md) | A reference to a storagePhysicalDisk resource. When the $expand query parameter is specified, the referenced resource is returned inline. Physical Disk on a server.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**running_firmware** | [**list[FirmwareRunningFirmware]**](FirmwareRunningFirmware.md) | A reference to a firmwareRunningFirmware resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**virtual_drive_extensions** | [**list[StorageVirtualDriveExtension]**](StorageVirtualDriveExtension.md) | A reference to a storageVirtualDriveExtension resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**virtual_drives** | [**list[StorageVirtualDrive]**](StorageVirtualDrive.md) | A reference to a storageVirtualDrive resource. When the $expand query parameter is specified, the referenced resource is returned inline. Storage physical drives are grouped as Drive Group, a drive group then can be partitioned into virtual drives.  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


