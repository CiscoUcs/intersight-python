# VnicFcIf

Virtual Fibre Channel Interface. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the virtual fibre channel interface.   | [optional] 
**order** | **int** | The order in which the virtual interface is brought up. The order assigned to an interface should be unique for all the Ethernet and Fibre-Channel interfaces on each PCI link on a VIC adapter. The maximum value of PCI order is limited by the number of virtual interfaces (Ethernet and Fibre-Channel) on each PCI link on a VIC adapter. All VIC adapters have a single PCI link except VIC 1385 which has two.   | [optional] 
**persistent_bindings** | **bool** | Enables retention of LUN ID associations in memory until they are manually cleared.   | [optional] 
**placement** | [**VnicPlacementSettings**](VnicPlacementSettings.md) |  | [optional] 
**type** | **str** | VHBA Type configuration for SAN Connectivity Policy. This configuration is supported only on Cisco VIC 14XX series and higher series of adapters.    | [optional] [default to 'fc-initiator']
**fc_adapter_policy** | [**VnicFcAdapterPolicy**](.md) |  | [optional] 
**fc_network_policy** | [**VnicFcNetworkPolicy**](.md) |  | [optional] 
**fc_qos_policy** | [**VnicFcQosPolicy**](.md) |  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 
**san_connectivity_policy** | [**VnicSanConnectivityPolicy**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


