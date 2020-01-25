# VnicPlacementSettings

Placement Settings for the virtual interface. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | PCIe Slot where the VIC adapter is installed. Supported values are (1-15) and MLOM.   | [optional] 
**pci_link** | **int** | The PCI Link used as transport for the virtual interface. All VIC adapters have a single PCI link except VIC 1385 which has two.    | [optional] 
**uplink** | **int** | Adapter port on which the virtual interface will be created.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


