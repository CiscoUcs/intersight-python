# PortGroup

Holder for multiple ports. A switch card will have one or more port groups. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transport** | **str** |  | [optional] [readonly] 
**equipment_shared_io_module** | [**EquipmentSharedIoModule**](.md) |  | [optional] 
**equipment_switch_card** | [**EquipmentSwitchCard**](.md) |  | [optional] 
**ethernet_ports** | [**list[EtherPhysicalPort]**](EtherPhysicalPort.md) | A reference to a etherPhysicalPort resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**fc_ports** | [**list[FcPhysicalPort]**](FcPhysicalPort.md) | A reference to a fcPhysicalPort resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**sub_groups** | [**list[PortSubGroup]**](PortSubGroup.md) | A reference to a portSubGroup resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


