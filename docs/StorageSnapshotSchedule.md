# StorageSnapshotSchedule

Configuration parameters for snapshot creation at source array. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **str** | Snapshot frequency. It is an interval on which snapshot is set to trigger on source array. Examples:     PT2H, Snapshot is performed for every 2 hours.     P4D, Snapshot is scheduled for every 4 days.     PT2H34M56.123S is 2 hours, 34 minutes, 56 seconds and 123 milliseconds.    | [optional] [readonly] 
**name** | **str** | Name of the snapshot schedule.   | [optional] 
**retention_time** | **str** | Duration to keep the snapshots on the source array. Once the period expires, system deletes the snapshot automatically from source array. Examples: P200D,  200 days. PT2H34M56.123S, 2 hours, 34 minutes, 56 seconds and 123 milliseconds.    | [optional] [readonly] 
**snapshot_time** | **str** | Preferred time of the day to capture the snapshot. it is applicable only if the frequency is set for a day or more. Format: hh:mm:ss Example: 08:30:00, Snapshot is set for 08:30 AM.     | [optional] [readonly] 
**protection_group** | [**StorageProtectionGroup**](.md) |  | [optional] 
**storage_array** | [**StorageGenericArray**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


