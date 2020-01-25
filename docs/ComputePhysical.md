# ComputePhysical

Abstract class for all physical servers. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_power_state** | **str** |  | [optional] [readonly] 
**asset_tag** | **str** |  | [optional] [readonly] 
**available_memory** | **int** |  | [optional] [readonly] 
**fault_summary** | **int** |  | [optional] 
**kvm_ip_addresses** | [**list[ComputeIpAddress]**](ComputeIpAddress.md) |  | [optional] 
**memory_speed** | **str** |  | [optional] [readonly] 
**mgmt_ip_address** | **str** | Management address of the server.   | [optional] 
**num_adaptors** | **int** | Total number of Adaptors available.   | [optional] [readonly] 
**num_cpu_cores** | **int** |  | [optional] [readonly] 
**num_cpu_cores_enabled** | **int** | Number of CPU cores enabled.   | [optional] [readonly] 
**num_cpus** | **int** | Total number of CPU&#39;s available.   | [optional] [readonly] 
**num_eth_host_interfaces** | **int** | Number of Ethernet Host Interfaces.   | [optional] [readonly] 
**num_fc_host_interfaces** | **int** |  | [optional] [readonly] 
**num_threads** | **int** | Number of threads enabled.   | [optional] [readonly] 
**oper_power_state** | **str** |  | [optional] [readonly] 
**oper_state** | **str** |  | [optional] [readonly] 
**operability** | **str** |  | [optional] [readonly] 
**platform_type** | **str** | Platform type of the device.   | [optional] 
**presence** | **str** |  | [optional] [readonly] 
**service_profile** | **str** |  | [optional] [readonly] 
**total_memory** | **int** |  | [optional] [readonly] 
**user_label** | **str** |  | [optional] [readonly] 
**uuid** | **str** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


