# MetaPropDefinitionAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_access** | **str** | API access control for the property. Examples are NoAccess, ReadOnly, CreateOnly etc.   | [optional] [readonly] [default to 'NoAccess']
**name** | **str** | The name of the property.   | [optional] [readonly] 
**op_security** | **str** | The data-at-rest security protection applied to this property when a Managed Object is persisted.  For example, Encrypted or Cleartext.    | [optional] [readonly] [default to 'ClearText']
**search_weight** | **float** | Enables the property to be searchable from global search. A value of 0 means this property is not globally searchable.    | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


