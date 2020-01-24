# X509CertificateAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | [**PkixDistinguishedName**](PkixDistinguishedName.md) |  | [optional] 
**not_after** | **datetime** | The date on which the certificate&#39;s validity period ends.   | [optional] [readonly] 
**not_before** | **datetime** | The date on which the certificate&#39;s validity period begins.   | [optional] [readonly] 
**pem_certificate** | **str** | The base64 encoded certificate in PEM format.   | [optional] 
**sha256_fingerprint** | **str** | The computed SHA-256 fingerprint of the certificate. Equivalent to &#39;openssl x509 -fingerprint -sha256&#39;.   | [optional] [readonly] 
**signature_algorithm** | **str** | Signature algorithm, as specified in [RFC 5280](https://tools.ietf.org/html/rfc5280).   | [optional] [readonly] 
**subject** | [**PkixDistinguishedName**](PkixDistinguishedName.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


