# VnicFcErrorRecoverySettings

Fibre Channel Error Recovery Settings. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enables Fibre Channel Error recovery.   | [optional] 
**io_retry_count** | **int** | The number of times an I/O request to a port is retried because the port is busy before the system decides the port is unavailable.   | [optional] 
**io_retry_timeout** | **int** | The number of seconds the adapter waits before aborting the pending command and resending the same IO request.   | [optional] 
**link_down_timeout** | **int** | The number of milliseconds the port should actually be down before it is marked down and fabric connectivity is lost.   | [optional] 
**port_down_timeout** | **int** | The number of milliseconds a remote Fibre Channel port should be offline before informing the SCSI upper layer that the port is unavailable. For a server with a VIC adapter running ESXi, the recommended value is 10000. For a server with a port used to boot a Windows OS from the SAN, the recommended value is 5000 milliseconds.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


