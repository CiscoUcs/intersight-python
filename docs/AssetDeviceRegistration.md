# AssetDeviceRegistration

DeviceRegistration represents a device connector enabled endpoint which has registered with Intersight. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | An identifier for the credential used by the device connector to authenticate with the Intersight web socket gateway.   | [optional] 
**claimed_by_user_name** | **str** | The name of the user who claimed the device for the account.   | [optional] [readonly] 
**claimed_time** | **datetime** | The date and time at which the device was claimed to this account.   | [optional] [readonly] 
**device_hostname** | **list[str]** |  | [optional] 
**device_ip_address** | **list[str]** |  | [optional] 
**execution_mode** | **str** | Indicates if the platform is an actual device or an emulated device for testing, demos, etc. Permitted values are [Normal, Emulator, ContainerEmulator].   | [optional] [default to '']
**parent_signature** | [**AssetParentConnectionSignature**](AssetParentConnectionSignature.md) |  | [optional] 
**pid** | **list[str]** |  | [optional] 
**platform_type** | **str** | The platform type on which device connector is executing.   | [optional] [default to '']
**public_access_key** | **str** | The device connector&#39;s public key used by the cloud to authenticate a connection from the device connector. The public key is used to verify that the signature a device connector sends on connect has been signed by the connector&#39;s private key stored on the device&#39;s filesystem. Must be a PEM encoded RSA public key string.    | [optional] [readonly] 
**read_only** | **bool** | Flag reported by devices to indicate an administrator of the device has disabled management operations of the device connector and only monitoring is permitted.   | [optional] [readonly] 
**serial** | **list[str]** |  | [optional] 
**vendor** | **str** | The vendor of the managed device.    | [optional] [readonly] 
**account** | [**IamAccount**](.md) |  | [optional] 
**claimed_by_user** | [**IamUser**](.md) |  | [optional] 
**cluster_members** | [**list[AssetClusterMember]**](AssetClusterMember.md) | A reference to a assetClusterMember resource. When the $expand query parameter is specified, the referenced resource is returned inline. The set of nodes within the devices cluster.  | [optional] [readonly] 
**device_claim** | [**AssetDeviceClaim**](.md) |  | [optional] 
**device_configuration** | [**AssetDeviceConfiguration**](.md) |  | [optional] 
**domain_group** | [**IamDomainGroup**](.md) |  | [optional] 
**parent_connection** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


