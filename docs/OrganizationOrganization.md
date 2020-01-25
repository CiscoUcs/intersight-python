# OrganizationOrganization

Organization provides multi-tenancy within an account. Multiple organizations can be present under an account. Resources are associated to organization using resource groups. Organization can have heterogeneous resources. Resources can be shared among multiple organizations. Organizations are associated to user permissions and privileges can be specified to provide access control. User can have access to multiple organizations in same permission and with different privileges on each organization. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The informative description about the usage of this organization.   | [optional] 
**name** | **str** | The name of the organization. There can be multiple organizations under an account.    | [optional] 
**account** | [**IamAccount**](.md) |  | [optional] 
**resource_groups** | [**list[ResourceGroup]**](ResourceGroup.md) | A reference to a resourceGroup resource. When the $expand query parameter is specified, the referenced resource is returned inline. The resource groups associated with these organization.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


