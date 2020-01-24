# FirmwareUpgrade

Firmware upgrade operation that downloads the image from Cisco/appliance/user provided HTTP repository or use the image from a network share and upgrade. The direct download is used for upgrade to use the image from Cisco repository or appliance repository. The network share is used for upgrade to use the image from a network share in user data center. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direct_download** | [**FirmwareDirectDownload**](FirmwareDirectDownload.md) |  | [optional] 
**network_share** | [**FirmwareNetworkShare**](FirmwareNetworkShare.md) |  | [optional] 
**upgrade_type** | **str** | Desired upgrade mode to choose either direct download based upgrade or network share upgrade.    | [optional] [default to 'direct_upgrade']
**device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**distributable** | [**FirmwareDistributable**](.md) |  | [optional] 
**server** | [**ComputeRackUnit**](.md) |  | [optional] 
**upgrade_status** | [**FirmwareUpgradeStatus**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


