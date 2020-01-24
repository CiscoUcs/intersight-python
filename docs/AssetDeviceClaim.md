# AssetDeviceClaim

DeviceClaim captures the intent to claim a device to an Intersight account. A device can be unclaimed by performing a DELETE on a DeviceClaim instance. When performing a claim, a secret passphrase must be obtained from the device connector UI/API by a sufficiently privileged user. The passphrase is timebound and proves that the user currently has privileged administrative access to the device being claimed. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_updates** | [**list[AssetConnectionControlMessage]**](AssetConnectionControlMessage.md) |  | [optional] 
**security_token** | **str** | Obtained from the device connector management UI or API (REST endpoint &#39;/connector/SecurityTokens&#39;).   | [optional] 
**serial_number** | **str** | Obtained from the device connector management UI or API (REST endpoint &#39;/connector/DeviceIdentifiers&#39;).    | [optional] 
**account** | [**IamAccount**](.md) |  | [optional] 
**device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


