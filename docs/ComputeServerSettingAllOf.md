# ComputeServerSettingAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_locator_led_state** | **str** | User configured state of the locator LED for the server.   | [optional] [default to 'None']
**admin_power_state** | **str** | User configured power state of the server.   | [optional] [default to 'Policy']
**config_state** | **str** | The configured state of these settings in the target server. The value is any one of Applied, Applying, Failed. Applied - This state denotes that the settings are applied successfully in the target server. Applying - This state denotes that the settings are being applied in the target server. Failed - This state denotes that the settings could not be applied in the target server.   | [optional] [readonly] [default to 'Applied']
**one_time_boot_device** | **str** | The name of the device chosen by user for configuring One-Time Boot device.   | [optional] 
**server_config** | [**ComputeServerConfig**](ComputeServerConfig.md) |  | [optional] 
**locator_led** | [**EquipmentLocatorLed**](.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 
**server** | [**ComputeRackUnit**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


