# ServerProfileAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_changes** | [**PolicyConfigChange**](PolicyConfigChange.md) |  | [optional] 
**assigned_server** | [**ComputeRackUnit**](.md) |  | [optional] 
**associated_server** | [**ComputeRackUnit**](.md) |  | [optional] 
**config_change_details** | [**list[ServerConfigChangeDetail]**](ServerConfigChangeDetail.md) | A reference to a serverConfigChangeDetail resource. When the $expand query parameter is specified, the referenced resource is returned inline. The configuration change details are captured here.  | [optional] [readonly] 
**config_result** | [**ServerConfigResult**](.md) |  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 
**running_workflows** | [**list[WorkflowWorkflowInfo]**](WorkflowWorkflowInfo.md) | A reference to a workflowWorkflowInfo resource. When the $expand query parameter is specified, the referenced resource is returned inline. The WorkflowInfos in the workflow engine that are running for this server Profile.  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


