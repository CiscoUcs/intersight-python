# HyperflexVcenterConfigPolicy

A policy specifying vCenter configuration. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_center** | **str** | The vCenter datacenter name.   | [optional] 
**hostname** | **str** | The vCenter server FQDN or IP.   | [optional] 
**is_password_set** | **bool** |  | [optional] 
**password** | **str** | The password for authenticating with vCenter. Follow the corresponding password policy governed by vCenter.   | [optional] 
**sso_url** | **str** | Overrides the default vCenter Single Sign-On URL. Do not specify unless instructed by Cisco TAC.   | [optional] 
**username** | **str** | The vCenter username (e.g. administrator@vsphere.local).    | [optional] 
**cluster_profiles** | [**list[HyperflexClusterProfile]**](HyperflexClusterProfile.md) | A reference to a hyperflexClusterProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of cluster profiles using this policy.  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


