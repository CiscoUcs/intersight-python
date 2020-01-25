# WorkflowBuildTaskMeta

Contains relationship for tasks within a workflow. It is used to dynamically generate a workflow. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for the BuildTaskMeta instance used to created a dynamic workflow.   | [optional] [readonly] 
**src** | **str** | Microservice owner for the task in this workflow.   | [optional] [readonly] 
**task_list** | [**object**](.md) | Task list used to build the dynamic workflow.   | [optional] [readonly] 
**task_type** | **str** | The type of the task within this workflow.   | [optional] [readonly] 
**workflow_type** | **str** | The type for the dynamic workflow.    | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


