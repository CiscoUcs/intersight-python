# FirmwareRunningFirmware

Running Firmware on an endpoint. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** | Kind of the firmware - boot-booloader/system/kernel.   | [optional] [readonly] 
**package_version** | **str** | Package version which the firmware belongs to.   | [optional] [readonly] 
**type** | **str** | Type of the firmware.   | [optional] [readonly] 
**version** | **str** | Version of the firmware.    | [optional] [readonly] 
**bios_unit** | [**BiosUnit**](.md) |  | [optional] 
**management_controller** | [**ManagementController**](.md) |  | [optional] 
**network_elements** | [**list[NetworkElement]**](NetworkElement.md) | A reference to a networkElement resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**storage_controller** | [**StorageController**](.md) |  | [optional] 
**storage_physical_disk** | [**StoragePhysicalDisk**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


