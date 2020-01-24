# Error

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | A value that is used to determine the nature of the error, and why it occurred. | 
**message_id** | **str** | A language-independent identifier of the specific error message. | [optional] 
**message** | **str** | A human-readable description of the error, localized with the i18n standard. The language is determined from the \&quot;Accept-Language\&quot; request-header. The Accept-Language request-header restricts the set of natural languages that are preferred as a response to the request. See RFC 2616 for more details.  Codes: 1. **InternalServerError**   An internal error occurred. 1. **InvalidMethod**         The HTTP method (POST, PUT...) is invalid for this API path. For example, a POST request was sent but this API path only supports GET. 1. **InvalidUrl**            The HTTP request contains an invalid URL. 1. **InvalidRequest**        The HTTP request contains an invalid or malformed message body. 1. **NotSupported**          The request is not supported for the specified REST resource. 1. **NotImplemented**        This API path is experimental and not implemented yet. 1. **NotFound**              The requested REST resource does not exist. 1. **AuthenticationFailure** The request lacks valid authentication credentials. 1. **UnauthorizedOperation** The client is not authorized to perform the operation, such as when the user has insufficient privileges. 1. **ValidationConflict**    The request contains conflicting attributes, such as two mutually exclusive attribute values. 1. **ServiceUnavailable**    See RFC 7231, status 503.  | 
**cause** | [**Error**](Error.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


