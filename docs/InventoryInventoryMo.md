# InventoryInventoryMo

Complex type representing the inventory MO. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mo_dn** | **str** | The UCS DN of the MO for which the latest inventory to be fetched. If this property is empty and moId property has the Moid of the MO to be updated, the Moid will be used. If this property is empty and moId is also empty, all the MOs of the given moType will be updated.   | [optional] 
**mo_id** | **str** | The MO id of an MO for which the latest inventory to be fetched. If this property is empty and moDn property has the UCS DN of the MO to be updated, the DN will be used. If this property is empty and moDn is also empty, all the MOs of the given moType will be updated.   | [optional] 
**mo_type** | **str** | The type of the MO for which the latest inventory to be fetched.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


