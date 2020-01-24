# ApplianceRestore

Restore tracks requests to restore the Intersight Appliance. There will be only one Restore managed object with a 'Started' state at any time. All other Restore managed objects will be in terminal states. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed_time** | **int** | Elapsed time in seconds since the restore process has started.   | [optional] [readonly] 
**end_time** | **datetime** | End date and time of the restore process.   | [optional] [readonly] 
**is_password_set** | **bool** |  | [optional] 
**messages** | **list[str]** |  | [optional] 
**password** | **str** | Password for authenticating with the file server.   | [optional] 
**start_time** | **datetime** | Start date and time of the restore process.   | [optional] [readonly] 
**status** | **str** | Status of the restore managed object.    | [optional] [readonly] [default to 'Started']
**account** | [**IamAccount**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


