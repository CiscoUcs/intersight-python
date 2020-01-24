# IamEndPointUser

Endpoint User or Local User. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Username.    | [optional] 
**end_point_user_role** | [**list[IamEndPointUserRole]**](IamEndPointUserRole.md) | A reference to a iamEndPointUserRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. A collection of references to the [iam.EndPointUserRole](mo://iam.EndPointUserRole) Managed Object.  When this managed object is deleted, the referenced [iam.EndPointUserRole](mo://iam.EndPointUserRole) MOs unset their reference to this deleted MO.  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


