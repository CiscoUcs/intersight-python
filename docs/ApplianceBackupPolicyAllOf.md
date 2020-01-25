# ApplianceBackupPolicyAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_time** | **datetime** | The next backup time set by the backup scheduler. Backup scheduler calculates the next backup time with the user-defined schedule set in the Schedule field.   | [optional] [readonly] 
**is_password_set** | **bool** |  | [optional] 
**manual_backup** | **bool** | Backup mode of the appliance. Automatic backups of the appliance are not initiated if this property is set to &#39;true&#39; and the backup schedule field is ignored.   | [optional] 
**password** | **str** | Password to authenticate the file server.   | [optional] 
**schedule** | [**OnpremSchedule**](OnpremSchedule.md) |  | [optional] 
**account** | [**IamAccount**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


