# WorkflowWorkflowMeta

Contains a workflow definition which is a sequence of tasks to execute. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description for the workflow.   | [optional] 
**input_parameters** | **list[str]** |  | [optional] 
**name** | **str** | The name given to the workflow.   | [optional] 
**output_parameters** | [**object**](.md) | The workflow output parameters.   | [optional] 
**schema_version** | **int** | The Conductor schema version that decides what attribute can be supported.   | [optional] 
**src** | **str** | The src is workflow owner service.   | [optional] 
**tasks** | [**object**](.md) | The tasks contained inside of the workflow.   | [optional] 
**type** | **str** | The type of workflow definition.   | [optional] [default to 'SystemDefined']
**version** | **int** | The version for the workflow so we can support multiple versions for the same workflow name.   | [optional] 
**wait_on_duplicate** | **bool** | Parameter decides if workflows will wait for a duplicate to finish before starting a new one.    | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


