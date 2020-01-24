# ApplianceImageBundleAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ansible_packages** | [**list[OnpremImagePackage]**](OnpremImagePackage.md) |  | [optional] 
**auto_upgrade** | **bool** | Indicates that the software upgrade was automatically initiated by the Intersight Appliance.   | [optional] [readonly] 
**dc_packages** | [**list[OnpremImagePackage]**](OnpremImagePackage.md) |  | [optional] 
**debug_packages** | [**list[OnpremImagePackage]**](OnpremImagePackage.md) |  | [optional] 
**description** | **str** | Short description of the software upgrade bundle.   | [optional] [readonly] 
**endpoint_packages** | [**list[OnpremImagePackage]**](OnpremImagePackage.md) |  | [optional] 
**fingerprint** | **str** | Fingerprint of the software manifest from which this bundle is created. Fingerprint is calculated using the SHA256 algorithm.   | [optional] [readonly] 
**has_error** | **bool** | Indicates that the ImageBundle has errors. The upgrade service sets this field when it encounters errors during the manifest processing.   | [optional] [readonly] 
**infra_packages** | [**list[OnpremImagePackage]**](OnpremImagePackage.md) |  | [optional] 
**init_packages** | [**list[OnpremImagePackage]**](OnpremImagePackage.md) |  | [optional] 
**name** | **str** | Name of the software upgrade bundle.   | [optional] [readonly] 
**notes** | **str** | Detailed description of the software upgrade bundle.   | [optional] [readonly] 
**priority** | **str** | Software upgrade manifest&#39;s upgrade priority. The upgrade service supports two priorities, Normal and Critical. Normal priority is used for regular software upgrades, and the upgrade service uses the Upgrade Policy to compute upgrade start time. Critical priority is used for the critical software security patches, and the upgrade service ignores the Upgrade Policy when it computes the upgrade start time.   | [optional] [readonly] [default to 'Normal']
**release_time** | **datetime** | Software upgrade manifest&#39;s release date and time.   | [optional] [readonly] 
**service_packages** | [**list[OnpremImagePackage]**](OnpremImagePackage.md) |  | [optional] 
**status_message** | **str** | Status message set during the manifest processing.   | [optional] [readonly] 
**system_packages** | [**list[OnpremImagePackage]**](OnpremImagePackage.md) |  | [optional] 
**ui_packages** | [**list[OnpremImagePackage]**](OnpremImagePackage.md) |  | [optional] 
**upgrade_end_time** | **datetime** | End date of the software upgrade process.   | [optional] [readonly] 
**upgrade_grace_period** | **int** | Grace period in seconds before the automatic upgrade is initiated. The upgrade service uses the grace period to compute the upgrade start time when it receives an upgrade notfication from the Intersight. If there is an Upgrade Policy configured for the Intersight Appliance, then the upgrade service uses the policy to compute the upgrade start time. However, the upgrade start time cannot not exceed the limit enforced by the grace period.   | [optional] [readonly] 
**upgrade_impact_duration** | **int** | Duration (in minutes) for which services will be disrupted.   | [optional] [readonly] 
**upgrade_impact_enum** | **str** | UpgradeImpactEnum is used to indicate the kind of impact the upgrade has on currently running services on the appliance.   | [optional] [readonly] [default to 'None']
**upgrade_start_time** | **datetime** | Start date of the software upgrade process.   | [optional] [readonly] 
**version** | **str** | Software upgrade manifest&#39;s version.    | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


