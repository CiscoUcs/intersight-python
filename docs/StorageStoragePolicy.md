# StorageStoragePolicy

The storage policy models the reusable storage related configuration that can be applied on many servers. This policy allows creation of RAID groups using existing disk group policies and virtual drives on the drive groups. The user has options to move all unused disks to JBOD or Unconfigured good state. The encryption of drives can be enabled through this policy using remote keys from a KMIP server. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_hot_spares** | [**list[StorageLocalDisk]**](StorageLocalDisk.md) |  | [optional] 
**retain_policy_virtual_drives** | **bool** | Retains the virtual drives defined in policy if they exist already. If this flag is false, the existing virtual drives are removed and created again based on virtual drives in the policy.    | [optional] 
**unused_disks_state** | **str** | This is used to specify the state, unconfigured good or jbod, in which the disks that are not used in this policy should be moved.   | [optional] [default to 'UnconfiguredGood']
**virtual_drives** | [**list[StorageVirtualDriveConfig]**](StorageVirtualDriveConfig.md) |  | [optional] 
**disk_group_policies** | [**list[StorageDiskGroupPolicy]**](StorageDiskGroupPolicy.md) | A reference to a storageDiskGroupPolicy resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the used disk group policies.  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 
**profiles** | [**list[PolicyAbstractConfigProfile]**](PolicyAbstractConfigProfile.md) | A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the profile objects.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


