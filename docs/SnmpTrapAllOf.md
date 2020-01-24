# SnmpTrapAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | Address to which the SNMP trap information is sent.   | [optional] 
**enabled** | **bool** | Enables/disables the trap on the server If enabled, trap is active on the server.   | [optional] 
**port** | **int** | Port used by the server to communicate with trap destination. Enter a value between 1-65535.   | [optional] 
**type** | **str** | Type of trap which decides whether to receive a notification when a trap is received at the destination.   | [optional] [default to 'Trap']
**user** | **str** | SNMP user for the trap. Applicable only to SNMPv3.   | [optional] 
**version** | **str** | SNMP version used for the trap.    | [optional] [default to 'V3']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


