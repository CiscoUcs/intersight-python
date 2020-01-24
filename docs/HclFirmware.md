# HclFirmware

Model which holds the details of firmware version and driver version. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver_name** | **str** | Protocol for which the driver is provided. E.g.  enic, fnic, lsi_mr3.   | [optional] 
**driver_version** | **str** | Version of the Driver supported.   | [optional] 
**error_code** | **str** | Error code for the support status.   | [optional] [readonly] [default to 'Success']
**firmware_version** | **str** | Firmware version of the product/adapter supported.   | [optional] 
**id** | **str** | Identifier of the firmware.   | [optional] 
**latest_driver** | **bool** | True if the driver is latest recommended driver.   | [optional] [readonly] 
**latest_firmware** | **bool** | True if the firmware is latest recommended firmware.    | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


