# IamApiKey

API keys are used to programatically perform API calls. API keys can be created by passing purpose field, which is a description for the application using API keys. Maximum of 3 API keys per user is allowed. API key will have RSA key pair generated and as part of create request key MOID, private and public key in PEM format are returned. In Intersight only the public key is stored. Client side private key is stored and is used for signature calculation. API key requests are authenticated using RSA SHA 256 signature validations. If the incoming request for authorization has X-Starship-Token, then session based authorization is done, else API key based authorization is performed. Once User, API key and Account are found and signature verification succeeds, then the privilege validations are performed. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash_algorithm** | **str** | The cryptographic hash algorithm to calculate the message digest.    | [optional] [default to 'SHA256']
**key_spec** | [**PkixKeyGenerationSpec**](PkixKeyGenerationSpec.md) |  | [optional] 
**private_key** | **str** | Holds the private key for the API key.    | [optional] 
**purpose** | **str** | The purpose of the API Key.   | [optional] 
**signing_algorithm** | **str** | The signing algorithm used by the client to authenticate API requests to Intersight. The following key generation schemes are supported: 1. RSASSA-PSS, as defined in RFC 8017 [RFC8017], Section 8.1, 2. ECDSA P-256, as defined in ANSI X9.62-2005 ECDSA and FIPS 186-4, 3. Ed25519ph, Ed25519ctx, and Ed25519, as defined in RFC 8032 [RFC8032], Section 5.1. The signing algorithm must be compatible with the key generation specification.     | [optional] [default to 'RSASSA-PKCS1-v1_5']
**permission** | [**IamPermission**](.md) |  | [optional] 
**user** | [**IamUser**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


