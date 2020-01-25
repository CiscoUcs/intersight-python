# MemoryPersistentMemoryConfigurationAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_capacity** | **str** | This represents the memory capacity in GB of a persistent memory configuration on a server.   | [optional] [readonly] 
**num_of_dimms** | **str** | This represents the number of persistent memory modules of a Persistent Memory Configuration on a server.   | [optional] [readonly] 
**num_of_regions** | **str** | This represents the number of regions of a Persistent Memory Configuration on a server.   | [optional] [readonly] 
**persistent_memory_capacity** | **str** | This represents the persistent memory capacity in GB of a persistent memory configuration on a server.   | [optional] [readonly] 
**reserved_capacity** | **str** | This represents the reserved capacity in GB of a persistent memory configuration on a server.   | [optional] [readonly] 
**security_state** | **str** | This represents the collective security state of all persistent memory modules on a server.   | [optional] [readonly] 
**total_capacity** | **str** | This represents the total capacity in GB of a persistent memory configuration on a server.    | [optional] [readonly] 
**compute_board** | [**ComputeBoard**](.md) |  | [optional] 
**persistent_memory_config_result** | [**MemoryPersistentMemoryConfigResult**](.md) |  | [optional] 
**persistent_memory_regions** | [**list[MemoryPersistentMemoryRegion]**](MemoryPersistentMemoryRegion.md) | A reference to a memoryPersistentMemoryRegion resource. When the $expand query parameter is specified, the referenced resource is returned inline. This represents the collection of all the persistent memory regions configured on a server.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


