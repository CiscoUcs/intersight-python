# IamEndPointUserPolicy

Enables creation of local users on endpoints. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password_properties** | [**IamEndPointPasswordProperties**](IamEndPointPasswordProperties.md) |  | [optional] 
**end_point_user_roles** | [**list[IamEndPointUserRole]**](IamEndPointUserRole.md) | A reference to a iamEndPointUserRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the collection of Endpoint user roles.  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 
**profiles** | [**list[PolicyAbstractConfigProfile]**](PolicyAbstractConfigProfile.md) | A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the server profile object.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


