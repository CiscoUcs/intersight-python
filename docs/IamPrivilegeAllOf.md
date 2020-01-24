# IamPrivilegeAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname_prefix** | **str** | The hostname prefix of the resource corresponding to this privilege. For example \\&#39;sentry\\&#39; in https://sentry.intersight.com .   | [optional] [readonly] 
**method** | **str** | The API method on the rest resource corresponding to privilege. For example READ, CREATE, UPDATE etc.   | [optional] [readonly] 
**name** | **str** | The name of the privilege reported by microservice.    | [optional] [readonly] 
**rest_path** | **str** | The REST API path of the resource corresponding to this privilege. For example /v1/iam/Accounts, /v1/iam/Sessions.   | [optional] [readonly] 
**url_prefix** | **str** | The URL path prefix of the resource corresponding to this privilege. For example /devops/kibana, /devops/grafana etc.     | [optional] [readonly] 
**account** | [**IamAccount**](.md) |  | [optional] 
**system** | [**IamSystem**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


