# WorkflowCliCommand

This models a single CLI command that can be executed on the end point. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** | The command to run on the device connector.    | [optional] 
**end_prompt** | **str** | The regex string that identifies the end of the command response.    | [optional] 
**expect_prompts** | [**list[WorkflowExpectPrompt]**](WorkflowExpectPrompt.md) |  | [optional] 
**skip_status_check** | **bool** | Skips the execution status check of the terminal command. One use case for this is while exiting the terminal session from esxi host.    | [optional] 
**terminal_end** | **bool** | If this flag is set, it marks the end of the terminal session where the previous commands were executed.    | [optional] 
**terminal_start** | **bool** | If this flag is set, the execution of this command initiates a terminal session in which the subsequent CLI commands are executed until a command with terminalEnd flag is encountered or the end of the batch.    | [optional] 
**type** | **str** | The type of the command - can be interactive or non-interactive.     | [optional] [default to 'NonInteractive']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


