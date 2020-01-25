# IamPrivilegeSetAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the privilege set.   | [optional] [readonly] 
**name** | **str** | Name of the privilege set.   | [optional] 
**privilege_names** | **list[str]** |  | [optional] 
**account** | [**IamAccount**](.md) |  | [optional] 
**associated_privilege_sets** | [**list[IamPrivilegeSet]**](IamPrivilegeSet.md) | A reference to a iamPrivilegeSet resource. When the $expand query parameter is specified, the referenced resource is returned inline. A privilege set can be associated to other privilege sets.  | [optional] 
**privileges** | [**list[IamPrivilege]**](IamPrivilege.md) | A reference to a iamPrivilege resource. When the $expand query parameter is specified, the referenced resource is returned inline. Reference to the privileges. Privilege represents an action which can be performed in Intersight such as creating server profile, deleting a user etc. Privileges are assigned to a user using privilege sets and roles.  | [optional] [readonly] 
**system** | [**IamSystem**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


