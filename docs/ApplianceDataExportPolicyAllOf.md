# ApplianceDataExportPolicyAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Status of the data collection mode. If the value is &#39;true&#39;, then data collection is enabled.   | [optional] 
**name** | **str** | Name of the Data Export Policy.    | [optional] [readonly] 
**account** | [**IamAccount**](.md) |  | [optional] 
**parent_config** | [**ApplianceDataExportPolicy**](.md) |  | [optional] 
**sub_configs** | [**list[ApplianceDataExportPolicy]**](ApplianceDataExportPolicy.md) | A reference to a applianceDataExportPolicy resource. When the $expand query parameter is specified, the referenced resource is returned inline. Sub-configurations of the current Data Export Policy. For example, if the current Data Export Policy is Inventory, the sub-configurations would include the Network and Storage inventory.  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


