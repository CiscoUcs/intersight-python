# IaasUcsdInfo

UCS Director accounts managed by Intersight. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | Moid of the UCSD device connector&#39;s asset.DeviceRegistration.   | [optional] [readonly] 
**guid** | **str** | Unique ID of UCSD getting registerd with Intersight.   | [optional] [readonly] 
**host_name** | **str** | The UCSD host name.   | [optional] [readonly] 
**ip** | **str** | The UCSD IP address.   | [optional] [readonly] 
**last_backup** | **datetime** | Last successful backup created for this UCS Director appliance if backup is configured.   | [optional] [readonly] 
**node_type** | **str** | NodeType specifies if UCSD is deployed in Stand-alone or Multi Node.   | [optional] [readonly] 
**product_name** | **str** | The UCSD product name.   | [optional] [readonly] 
**product_vendor** | **str** | The UCSD product vendor.   | [optional] [readonly] 
**product_version** | **str** | The UCSD product/platform version.   | [optional] [readonly] 
**status** | **str** | The UCSD status. Possible values are Active, Inactive, Unknown.    | [optional] [readonly] 
**connector_pack** | [**list[IaasConnectorPack]**](IaasConnectorPack.md) | A reference to a iaasConnectorPack resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to a collection of connector packs installed on the UCSD.  | [optional] [readonly] 
**device_status** | [**list[IaasDeviceStatus]**](IaasDeviceStatus.md) | A reference to a iaasDeviceStatus resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to a collection of infra accounts managed by the UCSD.  | [optional] [readonly] 
**license_info** | [**IaasLicenseInfo**](.md) |  | [optional] 
**most_run_tasks** | [**list[IaasMostRunTasks]**](IaasMostRunTasks.md) | A reference to a iaasMostRunTasks resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to collection of MostRunTasks objects with cascade on delete of UcsdInfo object.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**ucsd_managed_infra** | [**IaasUcsdManagedInfra**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


