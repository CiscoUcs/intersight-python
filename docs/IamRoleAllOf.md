# IamRoleAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Informative description about each role.   | [optional] [readonly] 
**name** | **str** | The name of the role which has to be granted to user.   | [optional] 
**privilege_names** | **list[str]** |  | [optional] 
**account** | [**IamAccount**](.md) |  | [optional] 
**privilege_sets** | [**list[IamPrivilegeSet]**](IamPrivilegeSet.md) | A reference to a iamPrivilegeSet resource. When the $expand query parameter is specified, the referenced resource is returned inline. Reference to the privilege sets. Privilege set is a collection of privileges. Privilege sets are assigned to a user using roles.  | [optional] [readonly] 
**system** | [**IamSystem**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


