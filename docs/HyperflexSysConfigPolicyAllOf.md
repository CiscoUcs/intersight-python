# HyperflexSysConfigPolicyAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_domain_name** | **str** | The DNS Search Domain Name. This setting applies to HyperFlex Data Platform 3.0 or later only.   | [optional] 
**dns_servers** | **list[str]** |  | [optional] 
**ntp_servers** | **list[str]** |  | [optional] 
**timezone** | **str** | The timezone of the HyperFlex cluster&#39;s system clock.    | [optional] [default to 'Pacific/Niue']
**cluster_profiles** | [**list[HyperflexClusterProfile]**](HyperflexClusterProfile.md) | A reference to a hyperflexClusterProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of cluster profiles using this policy.  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


