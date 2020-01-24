# IamSessionLimitsAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idle_time_out** | **int** | The idle timeout interval for the web session in seconds. The default value is 1800 seconds. When a session is not refreshed for this duration, backend will mark the session as idle and remove the session.   | [optional] [readonly] 
**maximum_limit** | **int** | The maximum number of sessions allowed in an account. The default value is 128.   | [optional] [readonly] 
**per_user_limit** | **int** | The maximum number of sessions allowed per user. Default value is 32.    | [optional] [readonly] 
**session_time_out** | **int** | The session expiry duration in seconds. The default value is 57600 seconds or 16 hours.    | [optional] [readonly] 
**account** | [**IamAccount**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


