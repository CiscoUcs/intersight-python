# AssetParentConnectionSignatureAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | The moid of the parent device registration.   | [optional] 
**node_id** | **str** | The node identity of the parent device, corresponds to the parents ClusterMember.memberIdentity. Used on connect to establish through which device in a cluster the child is connected through.   | [optional] 
**signature** | **str** | The result of signing the deviceId appended with the timeStamp fields with the devices private key.   | [optional] 
**time_stamp** | **datetime** | The time at which the signature was generated. Date is accurate to Intersights clock. Used to expire the signature.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


