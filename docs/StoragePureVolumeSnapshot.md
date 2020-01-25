# StoragePureVolumeSnapshot

Volume snapshot entity in Pure protection group. Volume snapshots are created either on-demand or using scheduler. Snapshots are immutable and it cannot be connected to hosts or host groups, and therefore the data it contains cannot be read or written. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial** | **str** | Unique serial number of the snapshot allocated by the storage array.    | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


