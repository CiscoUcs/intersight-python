# ForecastInstance

Entity representing forecast result for instance of managed object, ie, data source. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alt_model** | **list[float]** |  | [optional] 
**device_id** | **str** | The Moid of the Intersight managed device instance for which regression model is derived.   | [optional] [readonly] 
**full_cap_days** | **int** | The number of days remaining before the device reaches its full functional capacity.   | [optional] [readonly] 
**metric_name** | **str** | The name of the metric for which regression model is generated.   | [optional] [readonly] 
**min_days_for_forecast** | **int** | The minimum number of days the HyperFlex cluster should be up for computing forecast.   | [optional] [readonly] 
**model** | [**ForecastModel**](ForecastModel.md) |  | [optional] 
**threshold_days** | **int** | The number of days remaining before the device reaches the specified threshold for the metric as defined in definition.    | [optional] [readonly] 
**forecast_def** | [**ForecastDefinition**](.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


