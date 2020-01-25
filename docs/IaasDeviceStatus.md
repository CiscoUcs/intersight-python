# IaasDeviceStatus

List of infra accounts managed by UCSD. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** | The UCSD infra account name. Account Name is created when UCSD admin adds any new infra account (Physical/Virtual/Compute/Network) to be managed by UCSD.   | [optional] [readonly] 
**account_type** | **str** | The UCSD Infra Account type.   | [optional] [readonly] 
**claim_status** | **str** | Describes if the device is claimed in Intersight or not.   | [optional] [readonly] [default to 'Unknown']
**connection_status** | **str** | Describes about the connection status between the UCSD and the actual end device.   | [optional] [readonly] 
**device_model** | **str** | Describes about the device model.   | [optional] [readonly] 
**device_vendor** | **str** | Describes about the device vendor/manufacturer of the device.   | [optional] [readonly] 
**device_version** | **str** | Describes about the current firmware version running on the device.   | [optional] [readonly] 
**ip_address** | **str** | The IPAddress of the device.   | [optional] [readonly] 
**pod** | **str** | Describes about the pod to which this device belongs to in UCSD.   | [optional] [readonly] 
**pod_type** | **str** | Describes about the podType of Pod to which this device belongs to in UCSD.    | [optional] [readonly] 
**guid** | [**IaasUcsdInfo**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


