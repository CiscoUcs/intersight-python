# ApplianceUpgradeAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates if the software upgrade is active or not.   | [optional] [readonly] 
**auto_created** | **bool** | Indicates that the request was automatically created by the system.   | [optional] [readonly] 
**completed_phases** | [**list[OnpremUpgradePhase]**](OnpremUpgradePhase.md) |  | [optional] 
**current_phase** | [**OnpremUpgradePhase**](OnpremUpgradePhase.md) |  | [optional] 
**description** | **str** | Description of the software upgrade.   | [optional] [readonly] 
**elapsed_time** | **int** | Elapsed time in seconds during the software upgrade.   | [optional] [readonly] 
**end_time** | **datetime** | End date of the software upgrade.   | [optional] [readonly] 
**fingerprint** | **str** | Software upgrade manifest&#39;s fingerprint.   | [optional] [readonly] 
**messages** | **list[str]** |  | [optional] 
**services** | **list[str]** |  | [optional] 
**start_time** | **datetime** | Start date of the software upgrade. UI can modify startTime to re-schedule an upgrade.   | [optional] 
**status** | **str** | Status of the Intersight Appliance&#39;s software upgrade.   | [optional] [readonly] 
**ui_packages** | **list[str]** |  | [optional] 
**version** | **str** | Software upgrade manifest&#39;s version.    | [optional] [readonly] 
**account** | [**IamAccount**](.md) |  | [optional] 
**image_bundle** | [**ApplianceImageBundle**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


