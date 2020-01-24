# ForecastCatalog

A catalog for managing forecast settings. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sched_time** | **str** | The time at which the regression model needs to run for all the metrics specified in catalog.   | [optional] [readonly] 
**version** | **str** | The catalog version used in forecast configuration service.    | [optional] [readonly] 
**definition** | [**list[ForecastDefinition]**](ForecastDefinition.md) | A reference to a forecastDefinition resource. When the $expand query parameter is specified, the referenced resource is returned inline. The list of forecast definitions.  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


