# StorageRemoteKeySetting

Models the remote key configurarion required for disks encryptions. KMIP is the only remote key protocol supported in the policy. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_password_set** | **bool** |  | [optional] 
**password** | **str** | The password for the KMIP server login.   | [optional] 
**port** | **int** | The port to which the KMIP client should connect.   | [optional] 
**primary_server** | **str** | The IP address of the primary KMIP server. It could be an IPv4 address, an IPv6 address, or a hostname. Hostnames are valid only when Inband is configured for the CIMC address.   | [optional] 
**secondary_server** | **str** | The IP address of the secondary KMIP server. It could be an IPv4 address, an IPv6 address, or a hostname. Hostnames are valid only when Inband is configured for the CIMC address.   | [optional] 
**server_certificate** | **str** | The certificate/ public key of the KMIP server. It is required for initiating secure communication with the server.   | [optional] 
**username** | **str** | The user name for the KMIP server login.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


