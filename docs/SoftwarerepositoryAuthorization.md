# SoftwarerepositoryAuthorization

Consent that a user has provided to Intersight for contacting an external software repository such as cisco.com, on the user account's behalf. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_password_set** | **bool** |  | [optional] 
**is_user_id_set** | **bool** |  | [optional] 
**password** | **str** | The password that will be used by Intersight to create OAuth2 tokens for interacting with the external repository, on the user account&#39;s behalf.   | [optional] 
**repository_type** | **str** | The external repository for which this authorization has been provided. The only supported repository today is cisco.com.   | [optional] [default to 'Cisco']
**user_id** | **str** | The username that will be used by Intersight to create OAuth2 tokens for interacting with the external repository, on the user account&#39;s behalf.    | [optional] 
**account** | [**IamAccount**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


