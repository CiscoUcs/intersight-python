# IpmioverlanPolicy

Intelligent Platform Management Interface Over LAN Policy. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | State of the IPMI Over LAN service on the endpoint.   | [optional] 
**is_encryption_key_set** | **bool** | Indicates whether the value of the &#39;encryptionKey&#39; property has been set.   | [optional] [readonly] 
**encryption_key** | **str** | The encryption key to use for IPMI communication. It should have an even number of hexadecimal characters and not exceed 40 characters.   | [optional] 
**privilege** | **str** | The highest privilege level that can be assigned to an IPMI session on a server.    | [optional] [default to 'admin']
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 
**profiles** | [**list[PolicyAbstractConfigProfile]**](PolicyAbstractConfigProfile.md) | A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the profile object.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


