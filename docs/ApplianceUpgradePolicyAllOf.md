# ApplianceUpgradePolicyAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_upgrade** | **bool** | Indicates if the upgrade service is set to automatically start the software upgrade or not. If autoUpgrade is true, then the value of the schedule field is ignored.   | [optional] 
**blackout_dates_enabled** | **bool** | If enabled, allows the user to define a blackout period during which the appliance will not be upgraded.   | [optional] 
**blackout_end_date** | **datetime** | End date of the black out period.   | [optional] 
**blackout_start_date** | **datetime** | Start date of the black out period. The appliance will not be upgraded during this period.   | [optional] 
**schedule** | [**OnpremSchedule**](OnpremSchedule.md) |  | [optional] 
**account** | [**IamAccount**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


