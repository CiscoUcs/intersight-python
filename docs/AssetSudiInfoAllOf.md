# AssetSudiInfoAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pid** | **str** | The device model (PID) extracted from the X.509 SUDI Leaf Certificate.   | [optional] 
**serial_number** | **str** | The device SerialNumber extracted from the X.509 SUDI Leaf Certiicate.   | [optional] 
**signature** | **str** | The signature is obtained by taking the base64 encoding of the Serial Number + PID + Status, taking the SHA256 hash and then signing with the SUDI X.509 Leaf Certifiate.   | [optional] 
**status** | **str** | The validation status of the device.   | [optional] [default to 'DeviceStatusUnknown']
**sudi_certificate** | [**X509Certificate**](X509Certificate.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


