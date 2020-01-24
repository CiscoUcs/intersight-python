# HyperflexClusterAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_runway** | **int** | The number of days remaining before the cluster&#39;s storage utilization reaches the recommended capacity limit of 76%.  Default value is math.MaxInt32 to indicate that the capacity runway is \&quot;Unknown\&quot; for a cluster that is not connected or with not sufficient data.    | [optional] [readonly] 
**cluster_name** | **str** | The name of this HyperFlex cluster.   | [optional] [readonly] 
**cluster_type** | **int** | The storage type of this cluster (All Flash or Hybrid).   | [optional] [readonly] 
**cluster_uuid** | **str** | The unique identifier for this HyperFlex cluster.   | [optional] [readonly] 
**compute_node_count** | **int** | The number of compute nodes that belong to this cluster.   | [optional] [readonly] 
**converged_node_count** | **int** | The number of converged nodes that belong to this cluster.   | [optional] [readonly] 
**deployment_type** | **str** | The deployment type of the HyperFlex cluster.  The cluster can have one of the following configurations: 1. Datacenter: The HyperFlex cluster consists of UCS Fabric Interconnect-attached nodes on a single site. 2. Stretched Cluster: The HyperFlex cluster consists of UCS Fabric Interconnect-attached nodes distributed across multiple sites. 3. Edge: The HyperFlex cluster consists of 2-4 standalone nodes.  If the cluster is running a HyperFlex Data Platform version less than 4.0 or if the deployment type cannot be determined, the deployment type is set as &#39;NA&#39; (not available).    | [optional] [readonly] [default to 'NA']
**device_id** | **str** | The unique identifier of the device registration that represents this HyperFlex cluster&#39;s connection to Intersight.   | [optional] [readonly] 
**flt_aggr** | **int** | The number of yellow (warning) and red (critical) alarms stored as an aggregate.  The first 16 bits indicate the number of red alarms, and the last 16 bits contain the number of yellow alarms.    | [optional] [readonly] 
**hx_version** | **str** | The HyperFlex Data Platform version of this cluster.   | [optional] [readonly] 
**hxdp_build_version** | **str** | The version and build number of the HyperFlex Data Platform for this cluster.  After a cluster upgrade, this version string will be updated on the next inventory cycle to reflect the newly installed version.    | [optional] [readonly] 
**hypervisor_type** | **str** | The type of hypervisor running on this cluster.   | [optional] [readonly] [default to 'Unknown']
**hypervisor_version** | **str** | The version of hypervisor running on this cluster.   | [optional] [readonly] 
**summary** | [**HyperflexSummary**](HyperflexSummary.md) |  | [optional] 
**utilization_percentage** | **float** | The storage utilization percentage is computed based on total capacity and current capacity utilization.   | [optional] [readonly] 
**utilization_trend_percentage** | **float** | The storage utilization trend percentage represents the trend in percentage computed using the first and last point from historical data.   | [optional] [readonly] 
**vm_count** | **int** | The number of virtual machines present on this cluster.    | [optional] [readonly] 
**alarm** | [**list[HyperflexAlarm]**](HyperflexAlarm.md) | A reference to a hyperflexAlarm resource. When the $expand query parameter is specified, the referenced resource is returned inline. The alarms that have been raised for this HyperFlex cluster.  New alarms are added to this collection, and existing alarms are updated if the severity changes. Deleted alarms are not removed but are cleared by marking them as green.  | [optional] [readonly] 
**health** | [**HyperflexHealth**](.md) |  | [optional] 
**nodes** | [**list[HyperflexNode]**](HyperflexNode.md) | A reference to a hyperflexNode resource. When the $expand query parameter is specified, the referenced resource is returned inline. The nodes belonging to this HyperFlex cluster.  The node object contains inventory information about a specific HyperFlex node, such as host IP address, hypervisor type and version, and operational status.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


