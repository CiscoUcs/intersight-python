# IamTrustPoint

To affirm the identity of trusted source. Allows import of third-party CA certificates in X.509 (CER) format. It can be a root CA or an trust chain that leads to a root CA. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificates** | [**list[X509Certificate]**](X509Certificate.md) |  | [optional] 
**chain** | **str** | The certificate information for this trusted point. The certificate must be in Base64 encoded X.509 (CER) format.    | [optional] 
**account** | [**IamAccount**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


