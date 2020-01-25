# WorkflowWorkerTask

A WorkerTask is a simple task and the smallest granularity of work that can be defined as a task. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_moid** | **str** | Specify the catalog moid that this task belongs.   | [optional] 
**task_definition_id** | **str** | The resolved referenced task definition managed object.   | [optional] [readonly] 
**task_definition_name** | **str** | The qualified name of task that should be executed.   | [optional] 
**version** | **int** | The task definition version to use in this workflow. When no version is specified then the default version of the task at the time of creating or updating this workflow is used.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


