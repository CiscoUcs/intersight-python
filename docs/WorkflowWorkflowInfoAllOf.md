# WorkflowWorkflowInfoAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action of the workflow such as start, cancel, retry, pause.   | [optional] [default to 'Start']
**cleanup_time** | **datetime** | The time when the workflow info will be removed from database.   | [optional] [readonly] 
**end_time** | **datetime** | The time when the workflow reached a final state.   | [optional] [readonly] 
**failed_workflow_cleanup_duration** | **int** | The duration in hours after which the workflow info for failed, terminated or timed out workflow will be removed from database.   | [optional] 
**input** | [**object**](.md) | All the given inputs for the workflow.   | [optional] 
**inst_id** | **str** | A workflow instance Id which is the unique identified for the workflow execution.   | [optional] [readonly] 
**internal** | **bool** | Denotes if this workflow is internal and should be hidden from user view of running workflows.   | [optional] 
**message** | [**list[WorkflowMessage]**](WorkflowMessage.md) |  | [optional] 
**meta_version** | **int** | Version of the workflow metadata for which this workflow execution was started.   | [optional] 
**name** | **str** | A name of the workflow execution instance.   | [optional] 
**output** | [**object**](.md) | All the generated outputs for the workflow.   | [optional] [readonly] 
**progress** | **float** | This field indicates percentage of workflow task execution.    | [optional] [readonly] 
**src** | **str** | The source microservice name which is the owner for this workflow.   | [optional] [readonly] 
**start_time** | **datetime** | The time when the workflow was started for execution.   | [optional] [readonly] 
**status** | **str** | A status of the workflow (RUNNING, WAITING, COMPLETED, TIME_OUT, FAILED).   | [optional] [readonly] 
**success_workflow_cleanup_duration** | **int** | The duration in hours after which the workflow info for successful workflow will be removed from database.   | [optional] 
**trace_id** | **str** | The trace id to keep track of workflow execution.   | [optional] [readonly] 
**type** | **str** | A type of the workflow (serverconfig, ansible_monitoring).   | [optional] [readonly] 
**user_id** | **str** | The user identifier which indicates the user that started this workflow.   | [optional] [readonly] 
**wait_reason** | **str** | Denotes the reason workflow is in waiting status.   | [optional] [default to 'None']
**workflow_ctx** | [**object**](.md) | The workflow context which contains initiator and target information.    | [optional] 
**workflow_meta_type** | **str** | The type of workflow meta. Derived from the workflow meta that is used to launch this workflow instance.   | [optional] [default to 'SystemDefined']
**workflow_task_count** | **int** | Total number of workflow tasks in this workflow.    | [optional] [readonly] 
**_0_cluster_profile** | [**HyperflexClusterProfile**](.md) |  | [optional] 
**_1_profile** | [**ServerProfile**](.md) |  | [optional] 
**account** | [**IamAccount**](.md) |  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 
**parent_task_info** | [**WorkflowTaskInfo**](.md) |  | [optional] 
**pending_dynamic_workflow_info** | [**WorkflowPendingDynamicWorkflowInfo**](.md) |  | [optional] 
**permission** | [**IamPermission**](.md) |  | [optional] 
**task_infos** | [**list[WorkflowTaskInfo]**](WorkflowTaskInfo.md) | A reference to a workflowTaskInfo resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of task instances that ran as part of this workflow execution.  | [optional] [readonly] 
**workflow_definition** | [**WorkflowWorkflowDefinition**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


