# MetaDefinition

The meta-data of managed objects and complex types. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_privileges** | [**list[MetaAccessPrivilege]**](MetaAccessPrivilege.md) |  | [optional] 
**ancestor_classes** | **list[str]** |  | [optional] 
**is_concrete** | **bool** | Boolean flag to specify whether the meta class is a concrete class or not.   | [optional] [readonly] 
**meta_type** | **str** | Indicates whether the meta class is a complex type or managed object.   | [optional] [readonly] [default to 'ManagedObject']
**name** | **str** | The fully-qualified class name of the Managed Object or complex type. For example, \&quot;compute:Blade\&quot; where the Managed Object is \&quot;Blade\&quot; and the package is &#39;compute&#39;.   | [optional] [readonly] 
**namespace** | **str** | The namespace of the meta.   | [optional] [readonly] 
**parent_class** | **str** | The fully-qualified name of the parent metaclass in the class inheritance hierarchy.   | [optional] [readonly] 
**permission_supported** | **bool** | Boolean flag to specify whether instances of this class type can be specified in permissions for instance based access control. Permissions can be created for entire Intersight account or to a subset of resources (instance based access control). In the first release, permissions are supported for entire account or for a subset of organizations.    | [optional] [readonly] 
**properties** | [**list[MetaPropDefinition]**](MetaPropDefinition.md) |  | [optional] 
**rbac_resource** | **bool** | Boolean flag to specify whether instances of this class type can be assigned to resource groups that are part of an organization for access control. Inventoried physical/logical objects which needs access control should have rbacResource&#x3D;yes. These objects are not part of any organization by default like device registrations and should be assigned to organizations for access control. Profiles, policies, workflow definitions which are created by specifying organization need not have this flag set.    | [optional] [readonly] 
**relationships** | [**list[MetaRelationshipDefinition]**](MetaRelationshipDefinition.md) |  | [optional] 
**rest_path** | **str** | Restful URL path for the meta.   | [optional] [readonly] 
**version** | **str** | The version of the service that defines the meta-data.    | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


