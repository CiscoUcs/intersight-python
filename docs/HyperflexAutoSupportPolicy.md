# HyperflexAutoSupportPolicy

A policy specifying the configuration to automatically generate support tickets with Cisco TAC. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_state** | **bool** | Enable or disable Auto Support.   | [optional] 
**service_ticket_receipient** | **str** | The email address recipient for support tickets.    | [optional] 
**cluster_profiles** | [**list[HyperflexClusterProfile]**](HyperflexClusterProfile.md) | A reference to a hyperflexClusterProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of cluster profiles using this policy.  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


