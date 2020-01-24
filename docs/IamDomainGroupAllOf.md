# IamDomainGroupAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the domain-group.    | [optional] [readonly] 
**partition1** | **int** | The partition number domain group related messages are produced for &#39;Partition1&#39; category service topics.    | [optional] [readonly] 
**partition2** | **int** | In a cloud environment this parameter will indicate to which partition number domain group related messages are produced for &#39;Partition2&#39; category service topics.    | [optional] [readonly] 
**partition3** | **int** | In a cloud environment this parameter will indicate to which partition number domain group related messages are produced for &#39;Partition3&#39; category service topics.    | [optional] [readonly] 
**partition_key** | **str** | Partition key used for producing messages to Kafka partitions. By default Domain-group id will be used as parition key. For Domain-groups belonging to Early adopters domain-group id will be prefixed with &#39;H&#39; and used as partition key, such partition key will be treated differently and messages will always be produced to partition 0.    | [optional] [readonly] 
**usage** | **int** | The number of devices in the domain-group. Device registration notifications are processed to update the usage of the domain-group. The on-boarding account will have multiple domain-groups, and during the device registration least used domain-group will be selected for the device.     | [optional] [readonly] 
**account** | [**IamAccount**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


