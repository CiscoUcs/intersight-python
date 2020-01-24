# WorkflowTaskMeta

This MO contains a task definition. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** | A task execution type to indicate if it is a system task.   | [optional] 
**description** | **str** | A description of the task.   | [optional] 
**input_keys** | **list[str]** |  | [optional] 
**internal** | **bool** | Denotes whether or not this is an internal task.  Internal tasks will be hidden from the UI within a workflow.   | [optional] 
**name** | **str** | A task name that should be unique in Conductor DB.   | [optional] 
**output_keys** | **list[str]** |  | [optional] 
**response_timeout_sec** | **int** | The worker respnose timeout value.   | [optional] 
**retry_count** | **int** | A number of reties for this task.   | [optional] 
**retry_delay_sec** | **int** | The time on which the retry will be delayed.   | [optional] 
**retry_logic** | **str** | A logic which defines the way to handle retry (FIXED, EXPONENTIAL_BACKOFF).   | [optional] 
**src** | **str** | A service owns the task metadata.   | [optional] 
**timeout_policy** | **str** | A policy which defines the way to handle timeout (RETRY, TIME_OUT_WF, ALERT_ONLY).   | [optional] 
**timeout_sec** | **int** | A timeout value for the task in seconds.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


