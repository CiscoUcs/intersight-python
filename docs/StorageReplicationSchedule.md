# StorageReplicationSchedule

Configuration parameters for snapshot creation on target arrays. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **str** | Replication frequency. It is an interval on which replication is set to trigger. Examples:     PT2H, Snapshot is performed for every 2 hours.     P30D, Snapshot is scheduled for every 30 days.     PT2H34M56.123S is 2 hours, 34 minutes, 56 seconds and 123 milliseconds.    | [optional] [readonly] 
**name** | **str** | Replication schedule name.   | [optional] [readonly] 
**replication_time** | **str** | Preferred time of day at which to replicate the snapshots on target array. It is applicable only if the replication frequency is set for a day or more. Format: hh:mm:ss Example: 15:00:00, Replication is set for 3:00 PM.    | [optional] [readonly] 
**retention_time** | **str** | Duration to keep the replicated snapshots on the targets. Replicated snapshots are deleted from target array once mentioned rentention period is elapsed. Examples: P30D, Snapshots are available for 30 days. PT2H34M56.123S, 2 hours, 34 minutes, 56 seconds and 123 milliseconds.     | [optional] [readonly] 
**protection_group** | [**StorageProtectionGroup**](.md) |  | [optional] 
**storage_array** | [**StorageGenericArray**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


