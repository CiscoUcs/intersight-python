# IamUserAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_ip_address** | **str** | IP address from which the user last logged in to Intersight.   | [optional] [readonly] 
**email** | **str** | Email of the user. Users are added to Intersight using the email configured in the IdP.   | [optional] 
**first_name** | **str** | First name of the user. This field is populated from the IdP attributes received after authentication.   | [optional] [readonly] 
**last_login_time** | **datetime** | Last successful login time for user.   | [optional] [readonly] 
**last_name** | **str** | Last name of the user. This field is populated from the IdP attributes received after authentication.   | [optional] [readonly] 
**name** | **str** | UserID as configured in the IdP.   | [optional] [readonly] 
**user_type** | **str** | Type of the User. If a user is added manually by specifying the email address, or has logged in using groups, based on the IdP attributes received during authentication. If added manually, the user type will be static, otherwise dynamic.    | [optional] [readonly] 
**api_keys** | [**list[IamApiKey]**](IamApiKey.md) | A reference to a iamApiKey resource. When the $expand query parameter is specified, the referenced resource is returned inline. Current user&#39;s API keys. API keys are used to programatically perform API calls.  | [optional] [readonly] 
**app_registrations** | [**list[IamAppRegistration]**](IamAppRegistration.md) | A reference to a iamAppRegistration resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of registered OAuth2 applications created by the User.  | [optional] [readonly] 
**idp** | [**IamIdp**](.md) |  | [optional] 
**idpreference** | [**IamIdpReference**](.md) |  | [optional] 
**local_user_password** | [**IamLocalUserPassword**](.md) |  | [optional] 
**oauth_tokens** | [**list[IamOAuthToken]**](IamOAuthToken.md) | A reference to a iamOAuthToken resource. When the $expand query parameter is specified, the referenced resource is returned inline. Collection of the available OAuthTokens. Each OAuthToken lives 30 days unless it is deleted manually by User. OAuthToken is created when Login performed via OAuth Client (AppRegistration). OAuthToken itself is not sensitive data since it doesn&#39;t contain salt, salt is stored in Vault.  | [optional] [readonly] 
**permissions** | [**list[IamPermission]**](IamPermission.md) | A reference to a iamPermission resource. When the $expand query parameter is specified, the referenced resource is returned inline. Permissions assigned to the user. Permission provides a way to assign roles to a user or user group to perform operations on object hierarchy.  | [optional] 
**sessions** | [**list[IamSession]**](IamSession.md) | A reference to a iamSession resource. When the $expand query parameter is specified, the referenced resource is returned inline. Current user&#39;s web sessions. After a user logs into Intersight, a session object is created. This session object is deleted upon logout, idle timeout, expiry timeout, or manual deletion.  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


