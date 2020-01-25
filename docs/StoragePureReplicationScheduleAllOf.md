# StoragePureReplicationScheduleAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daily_limit** | **int** | Total number of snapshots per day to be available on target above and over the specified retention time. PureStorage FlashArray maintains all created snapshot until retention period. Daily limit is applied only on the snapshots once retention time is expired. In case of, daily limit is less than the number of snapshot available on source, system select snapshots evenly spaced out throughout the day.    | [optional] [readonly] 
**replication_blackout_intervals** | [**list[StorageReplicationBlackout]**](StorageReplicationBlackout.md) |  | [optional] 
**snapshot_expiry_time** | **str** | Duration to keep the daily limit snapshots on target array. StorageArray deletes the snapshots permanently from the targets beyond this period.    | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


