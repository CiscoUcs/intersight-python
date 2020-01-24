# ResourceLicenseResourceCountAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_type** | **str** | Type of licensing defined for this resource group. Used for licensing group.   | [optional] [readonly] [default to 'Base']
**resource_count** | **int** | The number of resource belongs to this licensing tier.    | [optional] [readonly] 
**account** | [**IamAccount**](.md) |  | [optional] 
**license_groups** | [**list[ResourceGroup]**](ResourceGroup.md) | A reference to a resourceGroup resource. When the $expand query parameter is specified, the referenced resource is returned inline. The list of all license groups bind with this server count object.  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


