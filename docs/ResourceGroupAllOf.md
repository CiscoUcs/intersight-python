# ResourceGroupAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this resource group.   | [optional] 
**per_type_combined_selector** | [**list[ResourcePerTypeCombinedSelector]**](ResourcePerTypeCombinedSelector.md) |  | [optional] 
**qualifier** | **str** | Qualifier shall be used to specify if we want to organize resources using multiple resource group or single For an account, resource groups can be of only one of the above types. (Both the types are mutually exclusive for an account.).   | [optional] [default to 'Allow-Selectors']
**selectors** | [**list[ResourceSelector]**](ResourceSelector.md) |  | [optional] 
**account** | [**IamAccount**](.md) |  | [optional] 
**organizations** | [**list[OrganizationOrganization]**](OrganizationOrganization.md) | A reference to a organizationOrganization resource. When the $expand query parameter is specified, the referenced resource is returned inline. A collection of references to the [organization.Organization](mo://organization.Organization) Managed Object.  When this managed object is deleted, the referenced [organization.Organization](mo://organization.Organization) MOs unset their reference to this deleted MO.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


