# UcsdUcsdRestoreParameters

Restore Configuration Parameters for UCS Director restore workflow 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_password_set** | **bool** |  | [optional] 
**location** | **str** | The complete location of the path on the server. The location should be specified in the following format- hostname-or-ipv4address&lt;:port&gt;/absolute-file-path   | [optional] 
**password** | **str** | The password of the target backup server. Only required if the target server is accessed using SFTP or SCP protocol.   | [optional] 
**protocol** | **str** | The protocol used to backup the UCS Director.   | [optional] 
**restore_configuration_files** | **bool** | Decides whether UCS Director property files should also be restored   | [optional] 
**restore_license** | **bool** | Decides whether license should also be restored   | [optional] 
**username** | **str** | The username of the target backup server. Only required if the target server is accessed using SFTP or SCP protocol.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


