# ResourceMembership

ResourceMembership represents a resource's associated groups, organizations and the permissions associated to this resource via organizations. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_permission_roles** | [**list[IamGroupPermissionToRoles]**](IamGroupPermissionToRoles.md) |  | [optional] 
**target_app** | **str** | Name of the Service owning the resource.    | [optional] [readonly] 
**holder** | [**ResourceMembershipHolder**](.md) |  | [optional] 
**resource** | [**MoBaseMo**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


