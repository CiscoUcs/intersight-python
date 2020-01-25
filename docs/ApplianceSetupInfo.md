# ApplianceSetupInfo

SetupInfo will have only one managed object. SetupInfo managed object is to keep track of the Intersight Appliance's setup information and guide the UI through the initial configuration of the Intersight Appliance.  The SetupInfo managed object is created during the Intersight Appliance setup. The Intersight UI uses this object to store the initial configuration states that the user has completed. If the user closes the Intersight UI without finishing all the initial configuration, then the Intersight UI will use this managed object to display the next configuration that the user needs to complete when the user uses the Intersight Appliance next time. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_type** | **str** | Build type of the Intersight Appliance setup (e.g. release or debug).   | [optional] [readonly] 
**capabilities** | [**list[ApplianceKeyValuePair]**](ApplianceKeyValuePair.md) |  | [optional] 
**cloud_url** | **str** | URL of the Intersight to which this Intersight Appliance is connected to.   | [optional] [readonly] 
**end_time** | **datetime** | End date of the Intersight Appliance&#39;s initial setup.    | [optional] [readonly] 
**setup_states** | **list[str]** |  | [optional] 
**start_time** | **datetime** | Start date of the Intersight Appliance&#39;s initial setup.    | [optional] [readonly] 
**account** | [**IamAccount**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


