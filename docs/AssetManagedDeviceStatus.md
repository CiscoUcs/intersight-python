# AssetManagedDeviceStatus

Maintains the Managed Device Status. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_port** | **int** | Port used for the connection to the Cloud by the Device Connector for the Managed Device.   | [optional] 
**connection_failure_reason** | **str** | Maintains the reason for the failure of connection to the Device in case of connection failure.   | [optional] 
**connection_status** | **str** | Maintains the status of the connection to the Device.   | [optional] [default to 'Unknown']
**error_code** | **int** | Maintains code related to error from Device Connector, if any.   | [optional] 
**error_reason** | **str** | Maintains the reason for the error from Device Connector, if any.   | [optional] 
**process_id** | **int** | Maintains the process pid of the Device Connector for the Managed Device.   | [optional] 
**server_port** | **int** | Port used for receiving requests from Intersight Assist by the Device Connector for the Managed Device.   | [optional] 
**state** | **str** | Maintains the state of the Managed Device, such as Start Success, Start Failure, etc. See ManagedDeviceState for device connection states.    | [optional] [default to 'New']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


