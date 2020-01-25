# HclDriverImage

Collection used to store the driver ISO urls for each server based on how it is managed. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver_iso_url** | **str** | URL of the driver ISO images.   | [optional] 
**management_type** | **str** | Type of the UCS version indicating whether it is a UCSM release vesion or a IMC release.   | [optional] [default to 'UCSM']
**server_pid** | **str** | Three part ID representing the server model as returned by UCSM/CIMC XML APIs.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


