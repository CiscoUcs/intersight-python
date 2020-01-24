# AssetSudiInfo

The SUDI is an X.509v3 certificate, which maintains the product identifier and serial number. The identity is implemented at manufacturing and chained to a publicly identifiable root certificate authority. It can be used as an unchangeable identity for configuration, security, auditing, and management. This strucure contains the SUDI information read from the device's Trust Anchor Module (TAM). 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pid** | **str** | The device model (PID) extracted from the X.509 SUDI Leaf Certificate.   | [optional] 
**serial_number** | **str** | The device SerialNumber extracted from the X.509 SUDI Leaf Certiicate.   | [optional] 
**signature** | **str** | The signature is obtained by taking the base64 encoding of the Serial Number + PID + Status, taking the SHA256 hash and then signing with the SUDI X.509 Leaf Certifiate.   | [optional] 
**status** | **str** | The validation status of the device.   | [optional] [default to 'DeviceStatusUnknown']
**sudi_certificate** | [**X509Certificate**](X509Certificate.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


