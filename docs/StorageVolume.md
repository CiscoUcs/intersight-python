# StorageVolume

Generic storage volume object. It is a provisioned storage identity which can be mapped to host to enable host access. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Short description about the volume.   | [optional] [readonly] 
**naa_id** | **str** | NAA id of volume. It is a significant number to identify corresponding lun path in hypervisor.   | [optional] [readonly] 
**name** | **str** | Named entitiy of the volume.   | [optional] [readonly] 
**size** | **int** | User provisioned volume size. It is a size exposed to host.   | [optional] [readonly] 
**storage_utilization** | [**StorageCapacity**](StorageCapacity.md) |  | [optional] 
**storage_array** | [**StorageGenericArray**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


