# VnicTcpOffloadSettingsAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**large_receive** | **bool** | Enables the reassembly of segmented packets in hardware before sending them to the CPU.   | [optional] 
**large_send** | **bool** | Enables the CPU to send large packets to the hardware for segmentation.   | [optional] 
**rx_checksum** | **bool** | When enabled, the CPU sends all packet checksums to the hardware for validation.   | [optional] 
**tx_checksum** | **bool** | When enabled, the CPU sends all packets to the hardware so that the checksum can be calculated.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


