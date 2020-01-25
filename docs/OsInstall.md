# OsInstall

This MO models the target server, answers and other properties needed for OS installation. The OS installation can be started in the target server by doing a POST on this MO. The requests to this MO starts a OS installation workflow that can be tracked using workflow engine MO workflow.WorkflowInfo. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the OS install configuration.     | [optional] 
**configuration_file** | [**OsConfigurationFile**](.md) |  | [optional] 
**image** | [**SoftwarerepositoryOperatingSystemFile**](.md) |  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 
**osdu_image** | [**FirmwareServerConfigurationUtilityDistributable**](.md) |  | [optional] 
**server** | [**ComputePhysical**](.md) |  | [optional] 
**workflow_info** | [**WorkflowWorkflowInfo**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


