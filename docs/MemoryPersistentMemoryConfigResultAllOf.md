# MemoryPersistentMemoryConfigResultAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_error_desc** | **str** | This describes the error in the result of a previously applied Persistent Memory Configuration on a server.   | [optional] [readonly] 
**config_result** | **str** | This represents the result of a previously applied Persistent Memory Configuration on a server.   | [optional] [readonly] 
**config_sequence_no** | **int** | This represents the sequence number of a previously applied Persistent Memory Configuration on a server.   | [optional] [readonly] 
**config_state** | **str** | This represents the state of a previously applied Persistent Memory Configuration on a server.    | [optional] [readonly] 
**memory_persistent_memory_configuration** | [**MemoryPersistentMemoryConfiguration**](.md) |  | [optional] 
**persistent_memory_namespace_config_results** | [**list[MemoryPersistentMemoryNamespaceConfigResult]**](MemoryPersistentMemoryNamespaceConfigResult.md) | A reference to a memoryPersistentMemoryNamespaceConfigResult resource. When the $expand query parameter is specified, the referenced resource is returned inline. This represents the collection of all the results of the previously applied Persistent Memory Namespaces on a server.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


