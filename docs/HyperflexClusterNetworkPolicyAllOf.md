# HyperflexClusterNetworkPolicyAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jumbo_frame** | **bool** | Enable or disable jumbo frames.   | [optional] 
**kvm_ip_range** | [**HyperflexIpAddrRange**](HyperflexIpAddrRange.md) |  | [optional] 
**mac_prefix_range** | [**HyperflexMacAddrPrefixRange**](HyperflexMacAddrPrefixRange.md) |  | [optional] 
**mgmt_vlan** | [**HyperflexNamedVlan**](HyperflexNamedVlan.md) |  | [optional] 
**uplink_speed** | **str** | Link speed of the server adapter port to the upstream switch. When the policy is attached to a cluster profile with EDGE management platform, the uplink speed can be &#39;1G&#39; or &#39;10G&#39;. When the policy is attached to a cluster profile with Fabric Interconnect management platform, the uplink speed can be &#39;default&#39; only.   | [optional] [default to 'default']
**vm_migration_vlan** | [**HyperflexNamedVlan**](HyperflexNamedVlan.md) |  | [optional] 
**vm_network_vlans** | [**list[HyperflexNamedVlan]**](HyperflexNamedVlan.md) |  | [optional] 
**cluster_profiles** | [**list[HyperflexClusterProfile]**](HyperflexClusterProfile.md) | A reference to a hyperflexClusterProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of cluster profiles using this policy.  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


