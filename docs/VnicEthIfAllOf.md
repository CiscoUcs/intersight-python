# VnicEthIfAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdn** | [**VnicCdn**](VnicCdn.md) |  | [optional] 
**name** | **str** | Name of the virtual ethernet interface.   | [optional] 
**order** | **int** | The order in which the virtual interface is brought up. The order assigned to an interface should be unique for all the Ethernet and Fibre-Channel interfaces on each PCI link on a VIC adapter. The maximum value of PCI order is limited by the number of virtual interfaces (Ethernet and Fibre-Channel) on each PCI link on a VIC adapter. All VIC adapters have a single PCI link except VIC 1385 which has two.   | [optional] 
**placement** | [**VnicPlacementSettings**](VnicPlacementSettings.md) |  | [optional] 
**usnic_settings** | [**VnicUsnicSettings**](VnicUsnicSettings.md) |  | [optional] 
**vmq_settings** | [**VnicVmqSettings**](VnicVmqSettings.md) |  | [optional] 
**eth_adapter_policy** | [**VnicEthAdapterPolicy**](.md) |  | [optional] 
**eth_network_policy** | [**VnicEthNetworkPolicy**](.md) |  | [optional] 
**eth_qos_policy** | [**VnicEthQosPolicy**](.md) |  | [optional] 
**lan_connectivity_policy** | [**VnicLanConnectivityPolicy**](.md) |  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


