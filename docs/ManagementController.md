# ManagementController

A specialized service processor that monitors the physical state of a server, using sensors and communicating with the system administrator through an independent connection. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Model of the endpoint that houses the management controller.    | [optional] [readonly] 
**adapter_unit** | [**AdapterUnit**](.md) |  | [optional] 
**compute_blade** | [**ComputeBlade**](.md) |  | [optional] 
**compute_rack_unit** | [**ComputeRackUnit**](.md) |  | [optional] 
**management_interfaces** | [**list[ManagementInterface]**](ManagementInterface.md) | A reference to a managementInterface resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**network_element** | [**NetworkElement**](.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**running_firmware** | [**list[FirmwareRunningFirmware]**](FirmwareRunningFirmware.md) | A reference to a firmwareRunningFirmware resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**storage_sas_expander** | [**StorageSasExpander**](.md) |  | [optional] 
**top_system** | [**TopSystem**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


