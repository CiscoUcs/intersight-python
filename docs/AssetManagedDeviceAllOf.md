# AssetManagedDeviceAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | [**CommCredential**](CommCredential.md) |  | [optional] 
**device_type** | **str** | Type of the Device such as VMware, Pure Storage supported by Intersight Assist.   | [optional] [default to '']
**ignore_cert** | **bool** | Ignore Certificates with protocol https for connecting to the Managed Device. It is not used for other protocols.   | [optional] 
**is_enabled** | **bool** | Device is Enabled/Disabled.   | [optional] 
**management_address** | **str** | Management address of the device. It can be IPv4, IPv6 or FQDN.   | [optional] 
**port** | **int** | Port to use for connecting to the Managed Device. Port is optional. If not specified, default port for protocol is used.   | [optional] 
**protocol** | **str** | Protocol to use for connecting to the Managed Device.   | [optional] [default to 'https']
**status** | [**AssetManagedDeviceStatus**](AssetManagedDeviceStatus.md) |  | [optional] 
**account** | [**IamAccount**](.md) |  | [optional] 
**device_connector_manager** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**workflow_info** | [**WorkflowWorkflowInfo**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


