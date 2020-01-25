# CondAlarm

A state-full entity representing a found problem. Alarms can be reported by the managed system itself or can be determined by Intersight. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_mo_id** | **str** | MoId of the affected object from the managed system&#39;s point of view.   | [optional] 
**affected_mo_type** | **str** | Managed system affected object type. For example Adaptor, FI, CIMC.   | [optional] 
**affected_object** | **str** | A unique key for an alarm instance, consists of a combination of a unique system name and msAffectedObject.   | [optional] 
**ancestor_mo_id** | **str** | Parent MoId of the fault from managed system. For example, Blade moid for adaptor fault.   | [optional] 
**ancestor_mo_type** | **str** | Parent MO type of the fault from managed system. For example, Blade for adaptor fault.   | [optional] 
**code** | **str** | A unique alarm code. For alarms mapped from UCS faults, this will be the same as the UCS fault code.   | [optional] 
**creation_time** | **datetime** | The time the alarm was created.   | [optional] 
**description** | **str** | A longer description of the alarm than the name. The description contains details of the component reporting the issue.   | [optional] 
**last_transition_time** | **datetime** | The time the alarm last had a change in severity.   | [optional] 
**ms_affected_object** | **str** | A unique key for the alarm from the managed system&#39;s point of view. For example, in the case of UCS, this is the fault&#39;s dn.   | [optional] 
**name** | **str** | Uniquely identifies the type of alarm. For alarms originating from Intersight, this will be a descriptive name. For alarms that are mapped from faults, the name will be derived from fault properties. For example, alarms mapped from UCS faults will use a prefix of UCS and appended with the fault code.   | [optional] 
**orig_severity** | **str** | The original severity when the alarm was first created.   | [optional] [default to 'None']
**severity** | **str** | The severity of the alarm. Valid values are Critical, Warning, Info, and Cleared.    | [optional] [default to 'None']
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


