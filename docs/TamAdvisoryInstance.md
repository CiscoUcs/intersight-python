# TamAdvisoryInstance

Instance of an Intersight advisory applicable for an Intersight managed object. An advisory instance is created when a given advisory is found applicable for an Intersight managed object. An advisory instance is retained for some time even after being cleared for historical purposes. A 'cleared' advisory instance is deleted after the retention time is elaspsed. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_object_moid** | **str** | Moid of the Intersight MO affected by the alert. Deprecated now and will be removed in subsequent releases.   | [optional] 
**affected_object_type** | **str** | Object type of the Intersight MO affected by the alert. Deprecated now and will be removed in subsequent releases.   | [optional] 
**last_state_change_time** | **datetime** | Timestamp when a state change was observed on this advisory instnace.   | [optional] [readonly] 
**last_verified_time** | **datetime** | Timestamp when this advisory was last evaluated.   | [optional] [readonly] 
**state** | **str** | Current state of the advisory instance (Active/Cleared/Unknown etc.).    | [optional] [default to 'unknown']
**advisory** | [**TamAdvisory**](.md) |  | [optional] 
**affected_object** | [**MoBaseMo**](.md) |  | [optional] 
**device_registration** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


