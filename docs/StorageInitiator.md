# StorageInitiator

An initiator is the consumer of storage, typically a server with an adapter card in it called a Host Bus Adapter (HBA). The initiator \"initiates\" a connection over the fabric to one or more ports on storage system target ports. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iqn** | **str** | IQN (iSCSI qualified name). Can be up to 255 characters long and has the following format, iqn.yyyy-mm.naming-authority:unique name.   | [optional] [readonly] 
**name** | **str** | Name of the initiator represented in storage array.   | [optional] [readonly] 
**type** | **str** | Initiator type, it can be FC or iSCSI.   | [optional] [readonly] [default to 'FC']
**wwn** | **str** | World wide name, 128 bit address represented in hexa decimal notation. (51:4f:0c:50:14:1f:af:01:51:4f:0c:51:14:1f:af:01).    | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


