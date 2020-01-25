# TopSystem

Root container for all UCSM / CIMC MOs. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4_address** | **str** | The IPv4 address of system.   | [optional] [readonly] 
**ipv6_address** | **str** | The IPv6 address of system.   | [optional] [readonly] 
**mode** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**time_zone** | **str** | The operational timezone of the system, empty indicates no timezone has been set specifically.    | [optional] 
**compute_blades** | [**list[ComputeBlade]**](ComputeBlade.md) | A reference to a computeBlade resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] 
**compute_rack_units** | [**list[ComputeRackUnit]**](ComputeRackUnit.md) | A reference to a computeRackUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**management_controller** | [**ManagementController**](.md) |  | [optional] 
**network_elements** | [**list[NetworkElement]**](NetworkElement.md) | A reference to a networkElement resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


