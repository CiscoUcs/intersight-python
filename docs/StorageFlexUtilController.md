# StorageFlexUtilController

Storage Flex Util Adapter. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_name** | **str** |  | [optional] 
**controller_status** | **str** |  | [optional] 
**ff_controller_id** | **str** |  | [optional] 
**internal_state** | **str** |  | [optional] 
**compute_board** | [**ComputeBoard**](.md) |  | [optional] 
**flex_util_physical_drives** | [**list[StorageFlexUtilPhysicalDrive]**](StorageFlexUtilPhysicalDrive.md) | A reference to a storageFlexUtilPhysicalDrive resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**flex_util_virtual_drives** | [**list[StorageFlexUtilVirtualDrive]**](StorageFlexUtilVirtualDrive.md) | A reference to a storageFlexUtilVirtualDrive resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


