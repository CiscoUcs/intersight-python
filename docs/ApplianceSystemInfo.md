# ApplianceSystemInfo

The Intersight Appliance's system information. SystemInfo is a singleton managed object created during the Intersight Appliance setup. The Intersight Appliance updates the SystemInfo managed object with up to date cluster status information periodically. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_conn_status** | **str** | Connection state of the Intersight Appliance to the Intersight.    | [optional] [readonly] [default to '']
**deployment_size** | **str** | Current running deployment size for the Intersight Appliance cluster. Eg. small, medium, large etc.   | [optional] [readonly] 
**hostname** | **str** | Publicly accessible FQDN or IP address of the Intersight Appliance.   | [optional] [readonly] 
**init_done** | **bool** | Indicates that the setup initialization process has been completed.   | [optional] [readonly] 
**operational_status** | **str** | Operational status of the Intersight Appliance cluster.   | [optional] [readonly] [default to 'Unknown']
**serial_id** | **str** | SerialId of the Intersight Appliance. SerialId is generated when the Intersight Appliance is setup. It is a unique UUID string, and serialId will not change for the life time of the Intersight Appliance.   | [optional] [readonly] 
**time_zone** | **str** | Timezone of the Intersight Appliance.   | [optional] [default to 'Pacific/Niue']
**version** | **str** | Current software version of the Intersight Appliance.    | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


