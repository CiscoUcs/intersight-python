# EquipmentSharedIoModuleAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_state** | **str** | This field identifies the configuration state for this SIOM Unit.   | [optional] [readonly] 
**discovery** | **str** | This field identifies the discovery state of SIOM.    | [optional] [readonly] 
**mac_of_shared_iom_aside** | **str** | This field identifies the MAC of IOM-A side.   | [optional] [readonly] 
**mac_of_shared_iom_bside** | **str** | This field identifies the MAC of IOM-B side.   | [optional] [readonly] 
**oper_state** | **str** | This field identifies the SIOM operational state.   | [optional] [readonly] 
**part_number** | **str** | This field identifies the Part Number for this SIOM Unit.   | [optional] [readonly] 
**reachability** | **str** | This field identifies the reachability to FI-A and B side.   | [optional] [readonly] 
**usr_lbl** | **str** | User label configured for the SIOM.   | [optional] [readonly] 
**vid** | **str** | This field identifies the vendor id for this SIOM Unit.    | [optional] [readonly] 
**equipment_system_io_controller** | [**EquipmentSystemIoController**](.md) |  | [optional] 
**port_groups** | [**list[PortGroup]**](PortGroup.md) | A reference to a portGroup resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


