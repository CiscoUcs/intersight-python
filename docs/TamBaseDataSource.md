# TamBaseDataSource

Represents source for the data needed to analyze the alerts. this could one of several supported source types (textFsmTemplates/Intersight API/external API). TextFsmTemplates and Intersight API are the only ones supported currently. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name is used to unique identify and refer a given data source in an alert definition.   | [optional] 
**type** | **str** | Type of data source (for e.g. TextFsmTempalate based, Intersight API based etc.).    | [optional] [default to 'nxos']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


