# HyperflexClusterProfileAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_ip_address** | **str** | The storage data IP address for the HyperFlex cluster.   | [optional] 
**hypervisor_type** | **str** | The hypervisor type for the HyperFlex cluster.   | [optional] [default to 'Unknown']
**mac_address_prefix** | **str** | The MAC address prefix in the form of 00:25:B5:XX.   | [optional] 
**mgmt_ip_address** | **str** | The management IP address for the HyperFlex cluster.   | [optional] 
**mgmt_platform** | **str** | The management platform for the HyperFlex cluster.   | [optional] [default to 'FI']
**replication** | **int** | The number of copies of each data block written.   | [optional] 
**storage_data_vlan** | [**HyperflexNamedVlan**](HyperflexNamedVlan.md) |  | [optional] 
**wwxn_prefix** | **str** | The WWxN prefix in the form of 20:00:00:25:B5:XX.    | [optional] 
**associated_cluster** | [**HyperflexCluster**](.md) |  | [optional] 
**auto_support** | [**HyperflexAutoSupportPolicy**](.md) |  | [optional] 
**cluster_network** | [**HyperflexClusterNetworkPolicy**](.md) |  | [optional] 
**cluster_storage** | [**HyperflexClusterStoragePolicy**](.md) |  | [optional] 
**config_result** | [**HyperflexConfigResult**](.md) |  | [optional] 
**ext_fc_storage** | [**HyperflexExtFcStoragePolicy**](.md) |  | [optional] 
**ext_iscsi_storage** | [**HyperflexExtIscsiStoragePolicy**](.md) |  | [optional] 
**local_credential** | [**HyperflexLocalCredentialPolicy**](.md) |  | [optional] 
**node_config** | [**HyperflexNodeConfigPolicy**](.md) |  | [optional] 
**node_profile_config** | [**list[HyperflexNodeProfile]**](HyperflexNodeProfile.md) | A reference to a hyperflexNodeProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of node profiles representing the configuraion of the corresponding HX cluster nodes.  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 
**proxy_setting** | [**HyperflexProxySettingPolicy**](.md) |  | [optional] 
**running_workflows** | [**list[WorkflowWorkflowInfo]**](WorkflowWorkflowInfo.md) | A reference to a workflowWorkflowInfo resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of workflows that are currently running for this cluster profile.  | [optional] [readonly] 
**software_version** | [**HyperflexSoftwareVersionPolicy**](.md) |  | [optional] 
**sys_config** | [**HyperflexSysConfigPolicy**](.md) |  | [optional] 
**ucsm_config** | [**HyperflexUcsmConfigPolicy**](.md) |  | [optional] 
**vcenter_config** | [**HyperflexVcenterConfigPolicy**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


