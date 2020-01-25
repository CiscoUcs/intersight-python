# MoBaseMo

The base abstract class for all Cisco Intersight managed objects. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_moid** | **str** | The Account ID for this managed object.   | [optional] [readonly] 
**create_time** | **datetime** | The time when this managed object was created.   | [optional] [readonly] 
**domain_group_moid** | **str** | The DomainGroup ID for this managed object.   | [optional] [readonly] 
**mod_time** | **datetime** | The time when this managed object was last modified.   | [optional] [readonly] 
**moid** | **str** | The unique identifier of this Managed Object instance.    | [optional] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.    | [readonly] 
**owners** | **list[str]** |  | [optional] 
**shared_scope** | **str** | Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a &#39;shared&#39; ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.   | [optional] [readonly] 
**tags** | [**list[MoTag]**](MoTag.md) |  | [optional] 
**version_context** | [**MoVersionContext**](MoVersionContext.md) |  | [optional] 
**ancestors** | [**list[MoBaseMo]**](MoBaseMo.md) | A reference to a moBaseMo resource. When the $expand query parameter is specified, the referenced resource is returned inline. The array containing the MO references of the ancestors in the object containment hierarchy.  | [optional] [readonly] 
**parent** | [**MoBaseMo**](.md) |  | [optional] 
**permission_resources** | [**list[MoBaseMo]**](MoBaseMo.md) | A reference to a moBaseMo resource. When the $expand query parameter is specified, the referenced resource is returned inline. A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


