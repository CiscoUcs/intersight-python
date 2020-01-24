# StoragePureProtectionGroup

Protection group entity in Pure storage array. A volume can be protected by associating with protection group either directly or indirectly (either host or host group). Snapshots are created on protected volume in local array or target array or both as per scheduler configuration. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | Overall size of all snapshots in the protection group, represented in bytes.   | [optional] 
**source** | **str** | Name of PureStorage array name on which the protection group is created.   | [optional] [readonly] 
**targets** | **list[str]** |  | [optional] 
**host_groups** | [**list[StoragePureHost]**](StoragePureHost.md) | A reference to a storagePureHost resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of host group object associated to the protection group.  | [optional] [readonly] 
**hosts** | [**list[StoragePureHost]**](StoragePureHost.md) | A reference to a storagePureHost resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of host object associated to the protection group.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**volumes** | [**list[StoragePureVolume]**](StoragePureVolume.md) | A reference to a storagePureVolume resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of volume object associated to the protection group.  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


