# WorkflowInternalPropertiesAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_task_type** | **str** | This field will hold the base task type like HttpBaseTask or RemoteAnsibleBaseTask.   | [optional] [readonly] 
**constraints** | **str** | This field will hold any constraints a concrete task definition will specify in order to limit the environment where the task can execute.   | [optional] [readonly] 
**internal** | **bool** | Denotes this is an internal task.  Internal tasks will be hidden from the UI within a workflow.   | [optional] [readonly] 
**owner** | **str** | The service that owns and is responsible for execution of the task.    | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


