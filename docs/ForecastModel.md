# ForecastModel

Model encapsulated model type and the model generated based on the type for computing forecast. For example if linear regression predictive modeling is used then the model data contains slope, coefficient and RMSE. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accuracy** | **float** | The standard error of the estimate is a measure of the accuracy of predictions from predective modeling.   | [optional] 
**model_data** | **list[float]** |  | [optional] 
**model_type** | **str** | Model type indicating type of predictive model used for computing forecast.    | [optional] [default to 'Linear']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


