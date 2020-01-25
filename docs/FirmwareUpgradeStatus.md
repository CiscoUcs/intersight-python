# FirmwareUpgradeStatus

Status of the upgrade operation includes the status of download and upgrade stages. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_error** | **str** | The error message from the endpoint during the download.   | [optional] 
**download_percentage** | **int** | The percentage of the image downloaded in the endpoint.   | [optional] 
**download_stage** | **str** | The image download stages. Example:downloading, flashing.   | [optional] 
**download_status** | **str** | The download status of the image in the endpoint.   | [optional] 
**ep_power_status** | **str** | The server power status after the upgrade request is submitted in the endpoint.   | [optional] [default to 'none']
**overall_error** | **str** | The reason for the operation failure.   | [optional] 
**overall_percentage** | **int** | The overall percentage of the operation.   | [optional] 
**overallstatus** | **str** | The overall status of the operation.   | [optional] [default to 'none']
**pending_type** | **str** | Pending reason for the upgrade waiting.    | [optional] [default to 'none']
**upgrade** | [**FirmwareUpgrade**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


