# StoragePhysicalDiskExtension

Information of disks as reported by controller. In certain cases like S-series servers, disk information will be reported by controller separately and this represents such information. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootable** | **str** | It shows whether disk is bootable or not.   | [optional] [readonly] 
**disk_dn** | **str** | It shows the Physical drive Dn.   | [optional] [readonly] 
**disk_id** | **int** | It shows storage Enclosure slotId.   | [optional] [readonly] 
**disk_state** | **str** | It shows the current drive state of disk.   | [optional] [readonly] 
**health** | **str** | It shows the current drive state of disk.    | [optional] 
**physical_disk** | [**StoragePhysicalDisk**](.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**storage_controller** | [**StorageController**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


