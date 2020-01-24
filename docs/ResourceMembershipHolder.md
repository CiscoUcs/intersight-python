# ResourceMembershipHolder

A holder of REST resources and their membership. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this resource membership holder.    | [optional] [readonly] 
**account** | [**IamAccount**](.md) |  | [optional] 
**memberships** | [**list[ResourceMembership]**](ResourceMembership.md) | A reference to a resourceMembership resource. When the $expand query parameter is specified, the referenced resource is returned inline. The list of all resources and their membership which are part of resource groups.  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


