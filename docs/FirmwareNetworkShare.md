# FirmwareNetworkShare

Firmware upgrade where the image is located in remote shared machine. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cifs_server** | [**FirmwareCifsServer**](FirmwareCifsServer.md) |  | [optional] 
**http_server** | [**FirmwareHttpServer**](FirmwareHttpServer.md) |  | [optional] 
**is_password_set** | **bool** |  | [optional] 
**map_type** | **str** | File server protocols like CIFS, NFS, WWW for HTTP (S) that hosts the image.   | [optional] [default to 'nfs']
**nfs_server** | [**FirmwareNfsServer**](FirmwareNfsServer.md) |  | [optional] 
**password** | **str** | Password as configured on the file server.   | [optional] 
**upgradeoption** | **str** | Option to control the upgrade, e.g., 1) nw_upgrade_mount_only - mount the image from a file server and run upgrade on-next server boot 2) nw_upgrade_full - mount the image and run upgrade immediately.   | [optional] [default to 'nw_upgrade_full']
**username** | **str** | Username as configured on the file server.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


