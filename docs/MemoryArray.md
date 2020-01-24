# MemoryArray

Holder housing multiple memory units. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **int** |  | [optional] [readonly] 
**cpu_id** | **int** |  | [optional] [readonly] 
**current_capacity** | **str** |  | [optional] [readonly] 
**error_correction** | **str** |  | [optional] [readonly] 
**max_capacity** | **str** |  | [optional] [readonly] 
**max_devices** | **str** |  | [optional] [readonly] 
**oper_power_state** | **str** |  | [optional] [readonly] 
**presence** | **str** |  | [optional] [readonly] 
**compute_board** | [**ComputeBoard**](.md) |  | [optional] 
**persistent_memory_units** | [**list[MemoryPersistentMemoryUnit]**](MemoryPersistentMemoryUnit.md) | A reference to a memoryPersistentMemoryUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline. This represents all the persistent memory modules found in a memory array of a server.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**units** | [**list[MemoryUnit]**](MemoryUnit.md) | A reference to a memoryUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline. This represents all the DIMMs found in a memory array of a server. This includes both regular DIMMs and persistent memory modules.  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


