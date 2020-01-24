# StorageVirtualDrive

A Virtual Disk or LUN. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_policy** | **str** |  | [optional] [readonly] 
**actual_write_cache_policy** | **str** |  | [optional] [readonly] 
**available_size** | **str** |  | [optional] [readonly] 
**block_size** | **str** |  | [optional] [readonly] 
**bootable** | **str** |  | [optional] [readonly] 
**config_state** | **str** |  | [optional] [readonly] 
**configured_write_cache_policy** | **str** |  | [optional] [readonly] 
**connection_protocol** | **str** |  | [optional] [readonly] 
**drive_cache** | **str** |  | [optional] [readonly] 
**drive_security** | **str** |  | [optional] [readonly] 
**drive_state** | **str** | It shows the Virtual drive state.   | [optional] [readonly] 
**io_policy** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**num_blocks** | **str** |  | [optional] [readonly] 
**oper_state** | **str** | It shows the current operational state of Virtual drive.   | [optional] [readonly] 
**operability** | **str** |  | [optional] [readonly] 
**physical_block_size** | **str** |  | [optional] [readonly] 
**presence** | **str** |  | [optional] [readonly] 
**read_policy** | **str** |  | [optional] [readonly] 
**security_flags** | **str** |  | [optional] [readonly] 
**size** | **str** |  | [optional] [readonly] 
**strip_size** | **str** | The strip size is the portion of a stripe that resides on a single drive in the drive group, this is measured in KB.   | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**uuid** | **str** |  | [optional] [readonly] 
**vendor_uuid** | **str** |  | [optional] [readonly] 
**virtual_drive_id** | **str** |  | [optional] [readonly] 
**physical_disk_usages** | [**list[StoragePhysicalDiskUsage]**](StoragePhysicalDiskUsage.md) | A reference to a storagePhysicalDiskUsage resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**storage_controller** | [**StorageController**](.md) |  | [optional] 
**vd_member_eps** | [**list[StorageVdMemberEp]**](StorageVdMemberEp.md) | A reference to a storageVdMemberEp resource. When the $expand query parameter is specified, the referenced resource is returned inline. It is a reference to LocalDisk to build up a VirtualDrive.  | [optional] [readonly] 
**virtual_drive_extension** | [**StorageVirtualDriveExtension**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


