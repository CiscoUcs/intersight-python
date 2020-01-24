# StorageHostLun

Generic storage host lun object. It exists only if the volume is associated to host initiator. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hlu** | **str** | Logical unit number (LUN) by which hosts address specified volume.   | [optional] [readonly] 
**host_name** | **str** | Name of the host associated with LUN.   | [optional] [readonly] 
**volume_name** | **str** | Name of the storage volume associated with LUN.    | [optional] [readonly] 
**host** | [**StorageHost**](.md) |  | [optional] 
**storage_array** | [**StorageGenericArray**](.md) |  | [optional] 
**volume** | [**StorageVolume**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


