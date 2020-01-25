# MemoryPersistentMemoryRegion

This represents a Persistent Memory Region configured on the persistent memory modules on a server. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimm_locater_ids** | **str** | This represents a set of DIMM locator IDs that are included in the Persistent Memory Region.   | [optional] [readonly] 
**free_capacity** | **str** | This represents the free capacity in GB of a Persistent Memory Region.   | [optional] [readonly] 
**health_state** | **str** | This represents the health state of a Persistent Memory Region.   | [optional] [readonly] 
**interleaved_set_id** | **str** | This represents the ID of a Interleaved Set formed for a Persistent Memory Region.   | [optional] [readonly] 
**persistent_memory_type** | **str** | This represents the persistent memory type of a Persistent Memory Region.   | [optional] [readonly] 
**region_id** | **str** | This represents the ID of a Persistent Memory Region.   | [optional] [readonly] 
**socket_id** | **str** | This represents the Socket ID of a Persistent Memory Region.   | [optional] [readonly] 
**socket_memory_id** | **str** | This represents the Socket Memory ID of a Persistent Memory Region.   | [optional] [readonly] 
**total_capacity** | **str** | This represents the total capacity in GB of a Persistent Memory Region.    | [optional] [readonly] 
**memory_persistent_memory_configuration** | [**MemoryPersistentMemoryConfiguration**](.md) |  | [optional] 
**persistent_memory_namespaces** | [**list[MemoryPersistentMemoryNamespace]**](MemoryPersistentMemoryNamespace.md) | A reference to a memoryPersistentMemoryNamespace resource. When the $expand query parameter is specified, the referenced resource is returned inline. This represents the collection of all the persistent memory namespaces configured within a persistent memory region.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


