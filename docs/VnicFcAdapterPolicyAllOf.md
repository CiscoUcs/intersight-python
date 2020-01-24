# VnicFcAdapterPolicyAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_detection_timeout** | **int** | Error Detection Timeout, also referred to as EDTOV, is the number of milliseconds to wait before the system assumes that an error has occurred.   | [optional] 
**error_recovery_settings** | [**VnicFcErrorRecoverySettings**](VnicFcErrorRecoverySettings.md) |  | [optional] 
**flogi_settings** | [**VnicFlogiSettings**](VnicFlogiSettings.md) |  | [optional] 
**interrupt_settings** | [**VnicFcInterruptSettings**](VnicFcInterruptSettings.md) |  | [optional] 
**io_throttle_count** | **int** | The maximum number of data or control I/O operations that can be pending for the virtual interface at one time. If this value is exceeded, the additional I/O operations wait in the queue until the number of pending I/O operations decreases and the additional operations can be processed.   | [optional] 
**lun_count** | **int** | The maximum number of LUNs that the Fibre Channel driver will export or show. The maximum number of LUNs is usually controlled by the operating system running on the server.   | [optional] 
**lun_queue_depth** | **int** | The number of commands that the HBA can send and receive in a single transmission per LUN.   | [optional] 
**plogi_settings** | [**VnicPlogiSettings**](VnicPlogiSettings.md) |  | [optional] 
**resource_allocation_timeout** | **int** | Resource Allocation Timeout, also referred to as RATOV, is the number of milliseconds to wait before the system assumes that a resource cannot be properly allocated.   | [optional] 
**rx_queue_settings** | [**VnicFcQueueSettings**](VnicFcQueueSettings.md) |  | [optional] 
**scsi_queue_settings** | [**VnicScsiQueueSettings**](VnicScsiQueueSettings.md) |  | [optional] 
**tx_queue_settings** | [**VnicFcQueueSettings**](VnicFcQueueSettings.md) |  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


