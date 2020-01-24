# PolicyAbstractConfigProfile

AbstractConfigProfile is an abstract base type for all config actions on a profile. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | User initiated action. Each profile type has its own supported actions. For HyperFlex cluster profile, the supported actions are -- Validate, Deploy, Continue, Retry, Abort, Unassign For server profile, the support actions are -- Deploy, Unassign.   | [optional] 
**config_context** | [**PolicyConfigContext**](PolicyConfigContext.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


