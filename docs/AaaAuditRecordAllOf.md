# AaaAuditRecordAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email of the associated user that made the change.  This is needed in case that user is later deleted, we still have some reference to the information.   | [optional] 
**inst_id** | **str** | The instance id of AuditRecordLocal, which is used to identify if the comming AuditRecordLocal was already processed before.   | [optional] 
**source_ip** | **str** | The source IP of the client.   | [optional] 
**timestamp** | **datetime** | The creation time of AuditRecordLocal, which is the time when the affected MO was created/modified/deleted.    | [optional] [readonly] 
**account** | [**IamAccount**](.md) |  | [optional] 
**sessions** | [**IamSession**](.md) |  | [optional] 
**user** | [**IamUser**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


