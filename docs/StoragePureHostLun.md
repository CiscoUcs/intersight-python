# StoragePureHostLun

A host LUN entity in Pure storage array. It exists only if the volume has a connection to host or host group. For host group mapping, it provides public connection to all hosts associated within host group. A volume can have private connection to host as well. It cannot have public and private connection. Pure assign same HLU for all the host in case if it is connected through host group. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_group_name** | **str** | Name of the host group associated with LUN.   | [optional] [readonly] 
**shared** | **bool** | Kind of volume connection to host. True if it is connected through host group. False in case of direct host connection.    | [optional] [readonly] 
**host_group** | [**StorageHost**](.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


