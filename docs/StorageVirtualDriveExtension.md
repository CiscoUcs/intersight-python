# StorageVirtualDriveExtension

Information of virtual drives as reported by a storage controller. In certain cases like S-series servers, virtual drive information will be reported by the controller separately and this represents such information. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootable** | **str** | It shows virtual drive is bootable.   | [optional] [readonly] 
**container_id** | **int** |  | [optional] [readonly] 
**drive_state** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**oper_device_id** | **str** |  | [optional] [readonly] 
**uuid** | **str** |  | [optional] [readonly] 
**vendor_uuid** | **str** |  | [optional] [readonly] 
**virtual_drive_dn** | **str** |  | [optional] [readonly] 
**virtual_drive_id** | **str** | It shows virtual drive Id.    | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**storage_controller** | [**StorageController**](.md) |  | [optional] 
**virtual_drive** | [**StorageVirtualDrive**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


