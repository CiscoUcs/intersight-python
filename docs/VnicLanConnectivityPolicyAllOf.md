# VnicLanConnectivityPolicyAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eth_ifs** | [**list[VnicEthIf]**](VnicEthIf.md) | A reference to a vnicEthIf resource. When the $expand query parameter is specified, the referenced resource is returned inline. A collection of references to the [vnic.EthIf](mo://vnic.EthIf) Managed Object.  When this managed object is deleted, the referenced [vnic.EthIf](mo://vnic.EthIf) MOs on the other side of the relationship are deleted.  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 
**profiles** | [**list[PolicyAbstractConfigProfile]**](PolicyAbstractConfigProfile.md) | A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the server profile.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


