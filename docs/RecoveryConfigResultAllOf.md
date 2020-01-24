# RecoveryConfigResultAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_0_on_demand_backup** | [**RecoveryOnDemandBackup**](.md) |  | [optional] 
**backup_profile** | [**RecoveryBackupProfile**](.md) |  | [optional] 
**result_entries** | [**list[RecoveryConfigResultEntry]**](RecoveryConfigResultEntry.md) | A reference to a recoveryConfigResultEntry resource. When the $expand query parameter is specified, the referenced resource is returned inline. Detailed result entries for both validation &amp; configration. Each result entry can be error/warning/info messages and the context.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


