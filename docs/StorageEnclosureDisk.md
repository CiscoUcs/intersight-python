# StorageEnclosureDisk

Physical Disk on the enclosure. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_size** | **str** | The block size of the physical disk in bytes.   | [optional] 
**disk_id** | **str** | This field represents the disk Id in the storage enclosure.   | [optional] 
**disk_state** | **str** | This field identifies the current disk configuration applied in the physical disk.   | [optional] 
**health** | **str** |  | [optional] 
**num_blocks** | **str** | The number of blocks present on the physical disk.   | [optional] 
**pid** | **str** | This field identifies the Product ID for physicalDisk.   | [optional] [readonly] 
**sas_address1** | **str** | This field identifies the SAS address assigned to the disk SAS port-1.   | [optional] 
**sas_address2** | **str** | This field identifies the SAS address assigned to the disk SAS port-2.   | [optional] 
**size** | **str** | The size of the physical disk in MB.    | [optional] 
**physical_disk** | [**StoragePhysicalDisk**](.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**storage_enclosure** | [**StorageEnclosure**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


