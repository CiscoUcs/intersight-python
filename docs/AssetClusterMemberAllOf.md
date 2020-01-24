# AssetClusterMemberAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leadership** | **str** | The current leadershipstate of this member. Updated by the device connector on failover or leadership change. If a member is elected as Primary within the cluster this connection will be the same as the DeviceRegistration connection. E.g a message addressed to the DeviceRegistration will be forwarded to the ClusterMember connection.   | [optional] [readonly] [default to 'Unknown']
**locked_leader** | **bool** | Devices lock their leadership on failure to heartbeat with peers. Value acts as a third party tie breaker in election between nodes. Intersight enforces that only one cluster member exists with this value set to true.   | [optional] 
**member_identity** | **str** | The unique identity of the member within the cluster. The identity is retrieved from the platform and reported by the device connector at connection time.   | [optional] [readonly] 
**parent_cluster_member_identity** | **str** | The member idenity of the cluster member through which this device is connected if applicable.   | [optional] [readonly] 
**sudi** | [**AssetSudiInfo**](AssetSudiInfo.md) |  | [optional] 
**device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


