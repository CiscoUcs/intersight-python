# ForecastDefinition

Definition for forecast metric settings. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_threshold_in_percentage** | **int** | Threshold above which user needs to be indicated through alarm/alert.   | [optional] [readonly] 
**data_source** | **str** | Data source from where we get the data for the metrics to compute regression model. For example Druid.   | [optional] [readonly] 
**metric_name** | **str** | Metric for which forecast prediction is done. Metrics are defined in the catalog file. Currently its only HyperFlex cluster storage capacity usage.   | [optional] [readonly] 
**min_num_of_days_of_data** | **int** | Minimum number of days of data required for computing forecast model.   | [optional] [readonly] 
**num_of_days_of_historical_data** | **int** | Number of days of data queried from the data source (example Druid ) which is used as input data for computing forecast model.   | [optional] [readonly] 
**platform_type** | **str** | The platform type for which we want to compute forecast. For example HyperFlex, NetworkElement.    | [optional] [readonly] 
**catalog** | [**ForecastCatalog**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


