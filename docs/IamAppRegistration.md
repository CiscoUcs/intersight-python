# IamAppRegistration

AppRegistration encapsulates the meta-data values of a registered OAuth2 client application, as described in https://tools.ietf.org/html/rfc7591#section-2. Registered client applications have a set of metadata values associated with their client identifier at the Intersight authorization server, including the list of valid redirection URIs or a display name. The meta-data is used to specify how a client application can retrieve a OAuth2 Access Token and subsequently invoke Intersight API on behalf of this AppRegistration.  To register an OAuth2 application, the following information must be provided. 1) Application name 2) An icon for the application 3) URL to the application's home page 4) A short description of the application 5) A list of redirect URLs  When an AppRegistration is created, a unique OAuth2 clientId is generated and returned in the HTTP response. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | A unique identifier for the OAuth2 client application. The client ID is auto-generated when the AppRegistration object is created.    | [optional] [readonly] 
**client_name** | **str** | App Registration name specified by user.    | [optional] 
**client_secret** | **str** | The OAuth2 client secret. The value of this property is generated when grantType includes &#39;client-credentials&#39;. Otherwise, no client-secret is generated.    | [optional] 
**client_type** | **str** | The type of the OAuth2 client (public or confidential), as specified in https://tools.ietf.org/html/rfc6749#section-2.1.    | [optional] [default to 'public']
**description** | **str** | Description of the application.    | [optional] 
**grant_types** | **list[str]** |  | [optional] 
**redirect_uris** | **list[str]** |  | [optional] 
**renew_client_secret** | **bool** | Set value to true to renew the client-secret. Applicable to client_credentials grant type.    | [optional] 
**response_types** | **list[str]** |  | [optional] 
**revocation_timestamp** | **datetime** | Used to perform revocation for tokens of AppRegistration. Updated only internally is case Revoke property come from UI with value true. On each request with OAuth2 access token the CreationTime of the OAuth2 token will be compared to RevokationTimestamp of the corresponding App Registration.    | [optional] [readonly] 
**revoke** | **bool** | Used to trigger update the revocationTimestamp value. If UI sent updating request with the Revoke value is true, then update RevocationTimestamp.     | [optional] 
**account** | [**IamAccount**](.md) |  | [optional] 
**oauth_tokens** | [**list[IamOAuthToken]**](IamOAuthToken.md) | A reference to a iamOAuthToken resource. When the $expand query parameter is specified, the referenced resource is returned inline. Collection of the OAuth2 tokens. Each OAuth2 token represents valid OAuth session. OAuth2 token is created when login over OAuth2 is performed using Authorization Code grant type.  | [optional] [readonly] 
**permission** | [**IamPermission**](.md) |  | [optional] 
**roles** | [**list[IamRole]**](IamRole.md) | A reference to a iamRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. The set of roles that can be used when a OAuth2 client is accessing this registered application. For example, multiple roles may be defined in your Intersight account, but you want users to login with the &#39;Read-Only&#39; role when accessing Intersight through a registered application. In that case, the &#39;roles&#39; property should contain a single element referencing the &#39;Read-Only&#39; role. A user can only assign roles they already have.  This relationship is deprecated. Authorization is now performed by passing the &#39;scope&#39; query parameter in the first request of the Authorization Code OAuth2 flow. The value of the &#39;scope&#39; parameter is a list of scope names separated by comma: ROLE.Account Administrator, ROLE.&lt;any role name&gt;.  | [optional] 
**user** | [**IamUser**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


