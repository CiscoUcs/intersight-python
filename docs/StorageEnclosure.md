# StorageEnclosure

Storage Enclosure for physical disks. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis_id** | **int** |  | [optional] [readonly] 
**description** | **str** |  | [optional] [readonly] 
**enclosure_id** | **int** |  | [optional] [readonly] 
**num_slots** | **int** |  | [optional] [readonly] 
**presence** | **str** |  | [optional] [readonly] 
**server_id** | **int** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**compute_blade** | [**ComputeBlade**](.md) |  | [optional] 
**compute_rack_unit** | [**ComputeRackUnit**](.md) |  | [optional] 
**enclosure_disk_slots** | [**list[StorageEnclosureDiskSlotEp]**](StorageEnclosureDiskSlotEp.md) | A reference to a storageEnclosureDiskSlotEp resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**enclosure_disks** | [**list[StorageEnclosureDisk]**](StorageEnclosureDisk.md) | A reference to a storageEnclosureDisk resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**equipment_chassis** | [**EquipmentChassis**](.md) |  | [optional] 
**physical_disks** | [**list[StoragePhysicalDisk]**](StoragePhysicalDisk.md) | A reference to a storagePhysicalDisk resource. When the $expand query parameter is specified, the referenced resource is returned inline.  | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


