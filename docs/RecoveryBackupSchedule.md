# RecoveryBackupSchedule

Encapsulates the various backup settings available to the user for scheduling a backup on the endpoint. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_time** | **datetime** | The time at which the backup is to be run on a given day. This is used when the frequency unit is daily.   | [optional] 
**frequency_unit** | **str** | The frequency at which the backup schedule must run.   | [optional] [default to 'Daily']
**hours** | **int** | The frequency, in hours, at which the backup schedule runs.    | [optional] [default to 8]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


