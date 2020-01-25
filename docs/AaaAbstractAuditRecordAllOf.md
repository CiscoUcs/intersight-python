# AaaAbstractAuditRecordAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** | The operation that was performed on this Managed Object. The event is a compound string that includes the CRUD operation such as Create, Modify, Delete, and a string representing the Managed Object type.   | [optional] 
**mo_type** | **str** | The object type of the REST resource that was created, modified or deleted.   | [optional] 
**object_moid** | **str** | The Moid of the REST resource that was created, modified or deleted.   | [optional] 
**request** | [**object**](.md) | The body of the REST request that was received from a client to create or modify a REST resource, represented as a JSON document.   | [optional] 
**trace_id** | **str** | The trace id of the request that was used to create, modify or delete a REST resource.  A trace id is a unique identifier for one particular REST request. It may be used for troubleshooting purpose by the Intersight technical support team.     | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


