# HyperflexConfigResult

Profile configuration (deploy, validation) results with the overall state and detailed result messages. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_progress** | **str** | The progress percentage of the running configuration or workflow.   | [optional] 
**duration** | **str** | The duration of the running configuration or workflow.   | [optional] 
**start_time** | **str** | The start time of the configuration or workflow.    | [optional] 
**cluster_profile** | [**HyperflexClusterProfile**](.md) |  | [optional] 
**result_entries** | [**list[HyperflexConfigResultEntry]**](HyperflexConfigResultEntry.md) | A reference to a hyperflexConfigResultEntry resource. When the $expand query parameter is specified, the referenced resource is returned inline. Detailed result entries for both validation &amp; configration. Each result entry can be error/warning/info messages and the context.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


