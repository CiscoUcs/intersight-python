# IamEndPointPasswordPropertiesAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_password_expiry** | **bool** | Enables password expiry on the endpoint.   | [optional] 
**enforce_strong_password** | **bool** | Enables a strong password policy Strong password requirements: A. The password must have a minimum of 8 and a maximum of 20 characters. B. The password must not contain the User&#39;s Name. C. The password must contain characters from three of the following four categories. 1) English uppercase characters (A through Z). 2) English lowercase characters (a through z). 3) Base 10 digits (0 through 9). 4) Non-alphabetic characters (!, @, #, $, %, ^, &amp;, *, -, _, +, &#x3D;).    | [optional] 
**grace_period** | **int** | Time period until when you can use the existing password, after it expires.   | [optional] 
**notification_period** | **int** | The duration by when the password will expire.   | [optional] 
**password_expiry_duration** | **int** | Set time period for password expiration. Value should be greater than notification period and grace period.   | [optional] 
**password_history** | **int** | Tracks password change history. Specifies in number of instances, that the new password was already used.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


