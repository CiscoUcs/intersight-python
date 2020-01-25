# StorageStorageUtilizationAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_reduction** | **float** | Ratio of mapped sectors within a volume versus the amount of physical space the data occupies after data compression and deduplication. The data reduction ratio does not include thin provisioning savings. For example, a data reduction ratio of 5.0 means that for every 5 MB the host writes to the array, 1 MB is stored on the array&#39;s flash modules.   | [optional] [readonly] 
**snapshot** | **int** | Physical space occupied by the snapshots, represented in bytes.   | [optional] [readonly] 
**thin_provisioned** | **float** | Percentage of volume sectors that do not contain host-written data because the hosts have not written data to them or the sectors have been explicitly trimmed.   | [optional] [readonly] 
**total_reduction** | **float** | Ratio of provisioned sectors within a volume versus the amount of physical space the data occupies after reduction via data compression and deduplication and with thin provisioning savings. Total reduction is data reduction with thin provisioning savings. For example, a total reduction ratio of 10.0 means that for every 10 MB of provisioned space, 1 MB is stored on the array&#39;s flash modules.   | [optional] [readonly] 
**volume** | **int** | Physical space occupied by volume data, excluding shared, array metadata and snapshots. Size id represented in bytes.    | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


