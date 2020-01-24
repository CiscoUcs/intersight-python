# IamCertificateRequest

The information required to generate a certificate signing request (CSR), which is a block of encoded text that is given to a Certificate Authority when applying for an SSL Certificate. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** | User input email address, an optional part of the subject of the certificate request.   | [optional] 
**name** | **str** | Name of the certificate request.   | [optional] 
**request** | **str** | Generated certificate signing request (CSR) in PEM format.   | [optional] [readonly] 
**self_signed** | **bool** | Whether the user wants the generated CSR to be self-signed by the appliance.   | [optional] 
**subject** | [**PkixDistinguishedName**](PkixDistinguishedName.md) |  | [optional] 
**subject_alternate_name** | [**PkixSubjectAlternateName**](PkixSubjectAlternateName.md) |  | [optional] 
**account** | [**IamAccount**](.md) |  | [optional] 
**certificate** | [**IamCertificate**](.md) |  | [optional] 
**private_key_spec** | [**IamPrivateKeySpec**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


