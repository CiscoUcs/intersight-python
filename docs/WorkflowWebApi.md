# WorkflowWebApi

This models a single Web API request within a batch of requests that get executed within a single workflow task. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | [**object**](.md) | Collection of key value pairs to set in the request header.    | [optional] 
**method** | **str** | The HTTP method to be executed in the given URL (GET, POST, PUT, etc). If the value is not specified, GET will be used as default.    | [optional] 
**protocol** | **str** | The accepted web protocol values are http and https.    | [optional] 
**target_type** | **str** | If the web API is to be executed in a remote device connected to the Intersight through device connector, &#39;Endpoint&#39; is expected as the value whereas if the API is an Intersight API, &#39;Local&#39; is expected as the value.    | [optional] [default to 'Endpoint']
**url** | **str** | The URL of the resource in the target to which the API request is made.     | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


