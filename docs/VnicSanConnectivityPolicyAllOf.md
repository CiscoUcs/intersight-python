# VnicSanConnectivityPolicyAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fc_ifs** | [**list[VnicFcIf]**](VnicFcIf.md) | A reference to a vnicFcIf resource. When the $expand query parameter is specified, the referenced resource is returned inline. A collection of references to the [vnic.FcIf](mo://vnic.FcIf) Managed Object.  When this managed object is deleted, the referenced [vnic.FcIf](mo://vnic.FcIf) MOs on the other side of the relationship are deleted.  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 
**profiles** | [**list[PolicyAbstractConfigProfile]**](PolicyAbstractConfigProfile.md) | A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the server profile.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


