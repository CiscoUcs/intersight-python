# AssetConnectionControlMessageAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | The account id to which the device belongs.   | [optional] 
**connector_version** | **str** | The version of the device connector currently running on the platform. Deprecated by newer connectors that will report this directly to the device connector gateway in a websocket header, but included to continue to support older versions which report any version change after connect.   | [optional] 
**device_id** | **str** | The Moid of the device under change. Used to route the message to a devices connection.   | [optional] 
**domain_group** | **str** | The domain group id to which the device belongs.   | [optional] 
**evict** | **bool** | Flag to force any open connections to be evicted. Used in case device has been deleted or blacklisted.   | [optional] 
**leadership** | **str** | The current leadership of a device cluster member.   | [optional] [default to 'Unknown']
**new_identity** | **str** | The new identity assigned to a device on ownership change (claim/unclaim).   | [optional] 
**partition** | **int** | The partition the device was last connected to, used to address the control message to the device connector gateway instance holding the devices connection.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


