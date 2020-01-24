# StorageSnapshot

Reference marker for volume at a particular point in time. It is a point-in-time copy of the volume. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time** | **datetime** | Exact date and time on which snapshot is created.   | [optional] [readonly] 
**name** | **str** | Name of the snapshot which represents point in time copy of volume.   | [optional] [readonly] 
**protection_group_name** | **str** | Name of the protection group to which the snapshot belongs. Value is emptry, if the snapshot is created directly on volume.   | [optional] [readonly] 
**size** | **int** | Snapshot size represented in bytes.   | [optional] [readonly] 
**source** | **str** | Source object on which the snapshot is created. It is a name of the originating volume.    | [optional] [readonly] 
**protection_group_snapshot** | [**StorageProtectionGroupSnapshot**](.md) |  | [optional] 
**storage_array** | [**StorageGenericArray**](.md) |  | [optional] 
**volume** | [**StorageVolume**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


