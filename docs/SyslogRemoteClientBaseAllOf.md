# SyslogRemoteClientBaseAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enables/disables remote logging for the endpoint If enabled, log messages will be sent to the syslog server mentioned in the Hostname/IP Address field.   | [optional] 
**hostname** | **str** | Hostname or IP Address of the syslog server where log should be stored.   | [optional] 
**min_severity** | **str** | Lowest level of messages to be included in the remote log.   | [optional] [default to 'warning']
**port** | **int** | Port number used for logging on syslog server.   | [optional] 
**protocol** | **str** | Transport layer protocol for transmission of log messages to syslog server.    | [optional] [default to 'udp']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


