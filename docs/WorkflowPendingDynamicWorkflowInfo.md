# WorkflowPendingDynamicWorkflowInfo

Information for a pending Dynamic Workflow Instance before it is run.  Validation needs to be done on the dynamic workflow tasks before starting.  After it begins, it will be tracked with regular WorkflowInstance. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**object**](.md) | The inputs of the workflow.   | [optional] 
**name** | **str** | A name for the pending dynamic workflow.   | [optional] 
**pending_services** | **list[str]** |  | [optional] 
**src** | **str** | The src is workflow owner service.   | [optional] 
**status** | **str** | The current status of the PendingDynamicWorkflowInfo.   | [optional] [default to 'GatheringTasks']
**wait_on_duplicate** | **bool** | When set to true workflow engine will wait for a duplicate to finish before starting a new one.   | [optional] 
**workflow_action_task_lists** | [**list[WorkflowDynamicWorkflowActionTaskList]**](WorkflowDynamicWorkflowActionTaskList.md) |  | [optional] 
**workflow_ctx** | [**object**](.md) | The workflow&#39;s workflow context which contains initiator and target information.   | [optional] 
**workflow_key** | **str** | This key contains workflow, initiator and target name. Workflow engine uses the key to do workflow dedup.   | [optional] 
**workflow_meta** | [**object**](.md) | The metadata of the workflow.    | [optional] 
**workflow_info** | [**WorkflowWorkflowInfo**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


