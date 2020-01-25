# WorkflowProperties

Properties for the task definition like the inputs, outputs, timeout and retry policies. Tasks are the building blocks for workflows. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_definition** | [**list[WorkflowBaseDataType]**](WorkflowBaseDataType.md) |  | [optional] 
**output_definition** | [**list[WorkflowBaseDataType]**](WorkflowBaseDataType.md) |  | [optional] 
**retry_count** | **int** | The number of times a task should be tried before marking as failed.   | [optional] 
**retry_delay** | **int** | The delay in seconds after which the the task is re-tried.   | [optional] 
**retry_policy** | **str** | The retry policy for the task.   | [optional] [default to 'Fixed']
**timeout** | **int** | The timeout value in seconds after which task will be marked as timed out. Max allowed value is 7 days.   | [optional] 
**timeout_policy** | **str** | The timeout policy for the task.    | [optional] [default to 'Timeout']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


