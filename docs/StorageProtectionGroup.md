# StorageProtectionGroup

A protection group contains list of members, that are protected together through snapshots with point-in-time consistency across the members. The members within the protection group have common data protection requirements and the same snapshot, replication, and retention schedules. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the protection Group.   | [optional] 
**prefix** | **str** | Prefix used for all generated snapshots from the protection group.   | [optional] 
**replication_enabled** | **bool** | Flag to determine if the replication is enabled. Snapshots are created on target array if the flag is set.   | [optional] 
**snapshot_enabled** | **bool** | Flag to determine if the snapshot is enabled. Snapshots are created on local array if the flag is set.    | [optional] 
**storage_array** | [**StorageGenericArray**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


