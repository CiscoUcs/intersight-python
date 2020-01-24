# AdapterUnit

The physical adapter present on a server. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adapter_id** | **str** | Unique Identifier of an adapter Unit within a Rack Interface.   | [optional] [readonly] 
**base_mac_address** | **str** |  | [optional] [readonly] 
**integrated** | **str** |  | [optional] [readonly] 
**oper_state** | **str** |  | [optional] [readonly] 
**operability** | **str** |  | [optional] [readonly] 
**part_number** | **str** |  | [optional] [readonly] 
**pci_slot** | **str** |  | [optional] [readonly] 
**power** | **str** |  | [optional] [readonly] 
**presence** | **str** |  | [optional] [readonly] 
**thermal** | **str** |  | [optional] [readonly] 
**vid** | **str** |  | [optional] [readonly] 
**compute_blade** | [**ComputeBlade**](.md) |  | [optional] 
**compute_rack_unit** | [**ComputeRackUnit**](.md) |  | [optional] 
**controller** | [**ManagementController**](.md) |  | [optional] 
**ext_eth_ifs** | [**list[AdapterExtEthInterface]**](AdapterExtEthInterface.md) | A reference to a adapterExtEthInterface resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**host_eth_ifs** | [**list[AdapterHostEthInterface]**](AdapterHostEthInterface.md) | A reference to a adapterHostEthInterface resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**host_fc_ifs** | [**list[AdapterHostFcInterface]**](AdapterHostFcInterface.md) | A reference to a adapterHostFcInterface resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**host_iscsi_ifs** | [**list[AdapterHostIscsiInterface]**](AdapterHostIscsiInterface.md) | A reference to a adapterHostIscsiInterface resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


