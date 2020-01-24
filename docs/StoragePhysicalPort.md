# StoragePhysicalPort

Common attributes for physical port in storage array. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iqn** | **str** | ISCSI qualified name applicable for ethernet port. eg &#39;iqn.2008-05.com.storage:fnm00151300643-514f0c50141faf05&#39;.   | [optional] [readonly] 
**name** | **str** | Name of the physical port available in storage array.   | [optional] [readonly] 
**speed** | **int** | Operational speed of physical port measured in Gbps.   | [optional] [readonly] 
**status** | **str** | Status of storage array port.   | [optional] [readonly] [default to 'Unknown']
**type** | **str** | Port type, it can be a any of the following category FC, FCoE and iSCSI.   | [optional] [readonly] [default to 'FC']
**wwn** | **str** | World wide name of FC port. It is a combination of WWNN and WWPN represented in 128 bit hexa decimal formatted with colon. e.g &#39;51:4f:0c:50:14:1f:af:01:51:4f:0c:51:14:1f:af:01&#39;.   | [optional] [readonly] 
**wwnn** | **str** | World wide node name of FC port. Represented in 64 bit digit hexa formatted with colon eg &#39;51:4f:0c:50:14:1f:af:01&#39;.   | [optional] [readonly] 
**wwpn** | **str** | World wide port name of FC port. Represented in 64 bit digit hexa formatted with colon eg &#39;51:4f:0c:51:14:1f:af:01&#39;.    | [optional] [readonly] 
**controller** | [**StorageArrayController**](.md) |  | [optional] 
**storage_array** | [**StorageGenericArray**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


