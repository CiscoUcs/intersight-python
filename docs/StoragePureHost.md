# StoragePureHost

A host entity in PureStorage FlashArray. It is an abstraction used by PureStorage to organize the storage network addresses (Fibre Channel worldwide names or iSCSI qualified names) of client computers and to control communications between clients and volumes. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_group_name** | **str** | Name of host group where the host belongs to. Empty if HostType is set as HostGroup.   | [optional] [readonly] 
**host_names** | **list[str]** |  | [optional] 
**storage_utilization** | [**StorageHostUtilization**](StorageHostUtilization.md) |  | [optional] 
**type** | **str** | Type of host entity whether it is a single host or host group (collection of host).    | [optional] [readonly] [default to 'Host']
**host_group** | [**StoragePureHost**](.md) |  | [optional] 
**hosts** | [**list[StoragePureHost]**](StoragePureHost.md) | A reference to a storagePureHost resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of host object associated to the host group.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


