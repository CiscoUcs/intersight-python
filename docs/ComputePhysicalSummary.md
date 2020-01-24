# ComputePhysicalSummary

Consolidated view of Blades and RackUnits. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_power_state** | **str** |  | [optional] [readonly] 
**asset_tag** | **str** |  | [optional] [readonly] 
**available_memory** | **int** |  | [optional] [readonly] 
**chassis_id** | **str** | The id of the chassis that the blade is located in.   | [optional] [readonly] 
**cpu_capacity** | **float** | CPU Capacity &#x3D; Number of CPU Sockets x Enabled Cores x Speed (GHz).   | [optional] [readonly] 
**device_mo_id** | **str** |  | [optional] [readonly] 
**dn** | **str** | The Distinguished Name unambiguously identifies an object in the system.   | [optional] [readonly] 
**fault_summary** | **int** |  | [optional] [readonly] 
**firmware** | **str** | The firmware version of the Cisco Integrated Management Controller (CIMC) for this server.   | [optional] [readonly] 
**ipv4_address** | **str** | The IPv4 address configured on the management interface of the Integrated Management Controller.   | [optional] [readonly] 
**kvm_ip_addresses** | [**list[ComputeIpAddress]**](ComputeIpAddress.md) |  | [optional] 
**memory_speed** | **str** |  | [optional] [readonly] 
**mgmt_ip_address** | **str** | The IP address of the management interface on the UCS Fabric Interconnect or Cisco Integrated Management Controller.   | [optional] [readonly] 
**model** | **str** | This field identifies the model of the given component.   | [optional] [readonly] 
**name** | **str** | The name of the UCS Fabric Interconnect cluster or Cisco Integrated Management Controller (CIMC).  When this server is attached to a UCS Fabric Interconnect, the value of this property is the name of the UCS Fabric Interconnect. When this server configured in standalone mode, the value of this property is the name of the Cisco Integrated Management Controller.    | [optional] [readonly] 
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
**platform_type** | **str** | Platform type of the device.   | [optional] [readonly] 
**presence** | **str** |  | [optional] [readonly] 
**revision** | **str** |  | [optional] [readonly] 
**rn** | **str** | The Relative Name uniquely identifies an object within a given context.   | [optional] [readonly] 
**scaled_mode** | **str** |  | [optional] [readonly] 
**serial** | **str** | This field identifies the serial of the given component.   | [optional] [readonly] 
**server_id** | **int** |  | [optional] [readonly] 
**service_profile** | **str** |  | [optional] [readonly] 
**slot_id** | **int** |  | [optional] [readonly] 
**source_object_type** | **str** | The source object type of this view MO.   | [optional] [readonly] 
**total_memory** | **int** |  | [optional] [readonly] 
**user_label** | **str** |  | [optional] [readonly] 
**uuid** | **str** |  | [optional] [readonly] 
**vendor** | **str** | This field identifies the vendor of the given component.    | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


