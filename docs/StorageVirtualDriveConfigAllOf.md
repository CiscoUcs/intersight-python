# StorageVirtualDriveConfigAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_policy** | **str** | This property holds the access policy that host has on this virtual drive.   | [optional] [default to 'Default']
**boot_drive** | **bool** | This flag enables the use of this virtual drive as a boot drive.   | [optional] 
**disk_group_name** | **str** | Disk group policy that has the disk group in which this virtual drive needs to be created.   | [optional] [readonly] 
**disk_group_policy** | **str** | Disk group policy that has the disk group in which this virtual drive needs to be created.   | [optional] 
**drive_cache** | **str** | This property expect disk cache policy.   | [optional] [default to 'Default']
**expand_to_available** | **bool** | This flag enables this virtual drive to use all the available space in the disk group. When this flag is configured, the size property is ignored.   | [optional] 
**io_policy** | **str** | This property expects the desired IO mode - direct IO or cached IO.   | [optional] [default to 'Default']
**name** | **str** | The name of the virtual drive. The name can be between 1 and 15 alphanumeric characters. Spaces or any special characters other than - (hyphen), _ (underscore), : (colon), and . (period) are not allowed.   | [optional] 
**read_policy** | **str** | This property holds the read ahead mode to be used.   | [optional] [default to 'Default']
**size** | **int** | Virtual drive size in MB. This is a required field unless the &#39;Expand to Available&#39; option is enabled.   | [optional] 
**write_policy** | **str** | This property holds the write mode used to write the data in this virtual drive.    | [optional] [default to 'Default']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


