# StorageArrayController

Common attributes for Storage array controller. It can be a hardware or software unit which manages the physical storage disk available in array. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Storage array controller name.   | [optional] [readonly] 
**operational_mode** | **str** | Controller running mode, Primary or Secondary.   | [optional] [readonly] [default to 'Unknown']
**status** | **str** | Status of the storage controller.   | [optional] [readonly] [default to 'Unknown']
**version** | **str** | Software version running on a storage controller.    | [optional] [readonly] 
**storage_array** | [**StorageGenericArray**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


