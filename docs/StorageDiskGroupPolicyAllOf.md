# StorageDiskGroupPolicyAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dedicated_hot_spares** | [**list[StorageLocalDisk]**](StorageLocalDisk.md) |  | [optional] 
**raid_level** | **str** | The supported RAID level for the disk group.   | [optional] [default to 'Raid0']
**span_groups** | [**list[StorageSpanGroup]**](StorageSpanGroup.md) |  | [optional] 
**use_jbods** | **bool** | Selected disks in the disk group in JBOD state will be set to Unconfigured Good state before they are used in virtual drive creation.    | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 
**storage_policies** | [**list[StorageStoragePolicy]**](StorageStoragePolicy.md) | A reference to a storageStoragePolicy resource. When the $expand query parameter is specified, the referenced resource is returned inline. A collection of references to the [storage.StoragePolicy](mo://storage.StoragePolicy) Managed Object.  When this managed object is deleted, the referenced [storage.StoragePolicy](mo://storage.StoragePolicy) MOs unset their reference to this deleted MO.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


