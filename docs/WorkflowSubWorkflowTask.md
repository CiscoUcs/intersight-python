# WorkflowSubWorkflowTask

A SubWorkflowTask is used to include another workflow as a task within this workflow. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_moid** | **str** | Specify the catalog moid that this task belongs.   | [optional] 
**version** | **int** | The workflow definition version to use as subworkflow. When no version is specified then the default version of the workflow at the time of creating or updating this workflow is used.   | [optional] 
**workflow_definition_id** | **str** | The resolved referenced workflow definition managed object.   | [optional] [readonly] 
**workflow_definition_name** | **str** | The qualified name of workflow that should be executed as a task.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


