# PatchDocument

A JSONPatch document as defined by RFC 6902. A JSONPatch document can be used in a request body when the 'Content-Type' HTTP header is set to 'application/json-patch+json'. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | The PATCH operation to be performed. &#39;move&#39; and &#39;copy&#39; are defined in RFC 6902 but are not supported in the Intersight API.  | 
**path** | **str** | A JSON-Pointer to a property in a REST resource. | 
**value** | [**object**](.md) | The value to be used within the operations. | [optional] 
**_from** | **str** | A string containing a JSON Pointer value. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


