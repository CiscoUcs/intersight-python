# InventoryRequest

Request MO allows the inventory of specific devices to be collected on demand. The inventory can be collected in three levels - all the MOs of a specific device, MOs of specific MO types for a given device or specific MO instances of specific MO types for a given device. These MO instances are used just to collect the requests and not persisted. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mos** | [**list[InventoryInventoryMo]**](InventoryInventoryMo.md) |  | [optional] 
**device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


