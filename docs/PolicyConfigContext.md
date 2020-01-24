# PolicyConfigContext

Configuration related state and results. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_state** | **str** | Indicates a profile&#39;s configuration deploying state. Values -- Assigned, Not-assigned, Associated, Pending-changes, Validating, Configuring, Failed.   | [optional] [readonly] 
**control_action** | **str** | System action to trigger the appropriate workflow. Values -- No_op, ConfigChange, Deploy, Unbind.   | [optional] 
**error_state** | **str** | Indicates a profile&#39;s error state. Values -- Validation-error (Static validation error), Pre-config-error (Runtime validation error), Config-error (Runtime configuration error).   | [optional] 
**oper_state** | **str** | Combined state (configState, and operational state of the associated physical resource) to indicate the current state of the profile. Values -- n/a, Power-off, Pending-changes, Configuring, Ok, Failed.    | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


