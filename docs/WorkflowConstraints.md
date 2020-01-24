# WorkflowConstraints

Captures the constraints for valid parameter values. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enum_list** | [**list[WorkflowEnumEntry]**](WorkflowEnumEntry.md) |  | [optional] 
**max** | **float** | Allowed maximum value of the parameter if parameter is integer/float or maximum length of the parameter if the parameter is string. When max and min are set to 0, then the limits are not checked.    | [optional] 
**min** | **float** | Allowed minimum value of the parameter if parameter is integer/float or minimum length of the parameter if the parameter is string. When max and min are set to 0, then the limits are not checked.    | [optional] 
**regex** | **str** | When the parameter is a string this regular expression is used to ensure the value is valid.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


