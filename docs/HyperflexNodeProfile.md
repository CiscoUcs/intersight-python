# HyperflexNodeProfile

A configuration profile per node in the HyperFlex cluster. It defines node settings such as IP address configuration for hypervisor management network, storage data network, HyperFlex management network, and the assigned physical server. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hxdp_data_ip** | **str** | IP address for storage data network (Controller VM interface).   | [optional] 
**hxdp_mgmt_ip** | **str** | IP address for HyperFlex management network.   | [optional] 
**hypervisor_data_ip** | **str** | IP address for storage data network (Hypervisor interface).   | [optional] 
**hypervisor_mgmt_ip** | **str** | IP address for Hypervisor management network.    | [optional] 
**assigned_server** | [**ComputeRackUnit**](.md) |  | [optional] 
**cluster_profile** | [**HyperflexClusterProfile**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


