# GraphicsCard

Graphics Card present in a server. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **int** | It shows the id of graphics card.   | [optional] [readonly] 
**device_id** | **int** | It shows the device id of grphics card.   | [optional] [readonly] 
**expander_slot** | **str** | It shows the expander slot inforamtion for the card.   | [optional] [readonly] 
**firmware_version** | **str** | It shows current firmware version of graphics card.   | [optional] [readonly] 
**mode** | **str** | It shows the current mode of graphics card.   | [optional] [readonly] 
**num_gpus** | **str** | It shows number of controllers under each card.   | [optional] 
**oper_state** | **str** | It shows the current operational state of graphics card.   | [optional] [readonly] 
**pci_address** | **str** | It shows the pci address of graphics card.   | [optional] [readonly] 
**pci_address_list** | **str** | This list contains the pci address of all controllers for corresponding card.   | [optional] [readonly] 
**pci_slot** | **str** | It shows the pci slot name for grapchics card.    | [optional] [readonly] 
**compute_board** | [**ComputeBoard**](.md) |  | [optional] 
**graphics_controllers** | [**list[GraphicsController]**](GraphicsController.md) | A reference to a graphicsController resource. When the $expand query parameter is specified, the referenced resource is returned inline. It shows the controllers under each graphics card.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


