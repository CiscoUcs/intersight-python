# PolicyAbstractConfigChangeDetailAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | **list[str]** |  | [optional] 
**config_change_context** | [**PolicyConfigResultContext**](PolicyConfigResultContext.md) |  | [optional] 
**config_change_flag** | **str** | Config change flag to differentiate Pending-changes and Config-drift.   | [optional] [default to 'Pending-changes']
**disruptions** | **list[str]** |  | [optional] 
**message** | **str** | Detailed description of the config change.   | [optional] 
**mod_status** | **str** | Modification status of the mo in this config change.    | [optional] [default to 'None']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


