# FirmwareDirectDownload

A specification for downloading the image from Cisco or appliance repository or user provided HTTP file server that hosts the image for firmware upgrade. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_server** | [**FirmwareHttpServer**](FirmwareHttpServer.md) |  | [optional] 
**image_source** | **str** | Source type referring the image to be downloaded from CCO or from a local https server.   | [optional] [default to 'cisco']
**is_password_set** | **bool** |  | [optional] 
**password** | **str** | Password as configured on the local https server.   | [optional] 
**upgradeoption** | **str** | Option to control the upgrade, e.g., sd_upgrade_mount_only - download the image into sd and upgrade wait for the server on-next boot.   | [optional] [default to 'sd_upgrade_mount_only']
**username** | **str** | Username as configured on the local https server.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


