# RecoveryScheduleConfigPolicy

Base Schedule config which contains all the required inputs to do schedule on a local or remote server. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule** | [**RecoveryBackupSchedule**](RecoveryBackupSchedule.md) |  | [optional] 
**backup_profiles** | [**list[RecoveryBackupProfile]**](RecoveryBackupProfile.md) | A reference to a recoveryBackupProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of Backup profiles using this policy.  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


