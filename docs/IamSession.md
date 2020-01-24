# IamSession

The web session of a user. After a user logs into Intersight, a session object is created. Session object is deleted upon logout, idle timeout, expiry timeout, or manual deletion. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_permissions** | [**list[IamAccountPermissions]**](IamAccountPermissions.md) |  | [optional] 
**client_ip_address** | **str** | The user agent IP address from which the session is launched.   | [optional] [readonly] 
**expiration** | **datetime** | Expiration time for the session.   | [optional] [readonly] 
**idle_time_expiration** | **datetime** | Idle time expiration for the session.   | [optional] [readonly] 
**last_login_client** | **str** | The client address from which last login is initiated.   | [optional] [readonly] 
**last_login_time** | **datetime** | The last login time for user.       | [optional] [readonly] 
**permission** | [**IamPermission**](.md) |  | [optional] 
**user** | [**IamUser**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


