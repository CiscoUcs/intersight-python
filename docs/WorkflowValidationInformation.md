# WorkflowValidationInformation

Type used to capture all the validation information for the workflow definition. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The current validation state of this workflow. The possible states are Valid, Invalid, NotValidated (default).   | [optional] [readonly] [default to 'NotValidated']
**validation_error** | [**list[WorkflowValidationError]**](WorkflowValidationError.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


