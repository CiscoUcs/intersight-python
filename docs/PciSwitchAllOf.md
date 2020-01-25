# PciSwitchAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | It shows the device id of the switch.   | [optional] [readonly] 
**health** | **str** | It shows the composite health of the switch.   | [optional] [readonly] 
**num_of_adaptors** | **str** | It shows the number of gpus and pci adapters connected the switch.   | [optional] [readonly] 
**pci_address** | **str** | It shows shows the PCI address of switch.   | [optional] [readonly] 
**pci_slot** | **str** | It shows the PCI slot name for switch.   | [optional] [readonly] 
**product_name** | **str** | It shows the model information for the switch.   | [optional] [readonly] 
**product_revision** | **str** | It shows the revision for the product.   | [optional] [readonly] 
**sub_device_id** | **str** | It shows the sub device id of the switch.   | [optional] [readonly] 
**sub_vendor_id** | **str** | It shows the sub vendor id of the switch.   | [optional] [readonly] 
**temperature** | **str** | It shows the current temperature of the switch.   | [optional] [readonly] 
**type** | **str** | It shows the type inforamtion of switch.   | [optional] 
**vendor_id** | **str** | It shows the vendor id of the switch.    | [optional] [readonly] 
**compute_board** | [**ComputeBoard**](.md) |  | [optional] 
**links** | [**list[PciLink]**](PciLink.md) | A reference to a pciLink resource. When the $expand query parameter is specified, the referenced resource is returned inline. It shows the number of gpus and pci adapters under each switch.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


