# StorageProtectionGroupSnapshot

Protection group snapshot entity in protection group. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time** | **datetime** | Protection group snapshot created time.   | [optional] [readonly] 
**name** | **str** | Protection group snapshot name which represents point in time copy of all members in protection group.   | [optional] [readonly] 
**size** | **int** | Snapshot size represented in bytes. It is a cummulative size of all snapshots in a set.   | [optional] [readonly] 
**source** | **str** | Source protection group name on which the snapshot is created.    | [optional] [readonly] 
**protection_group** | [**StorageProtectionGroup**](.md) |  | [optional] 
**storage_array** | [**StorageGenericArray**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


