# IamLocalUserPassword

LocalUserPassword type is used for changing local user's password. Caller must send old password in Password field and new password in newPassword field. Intersight will verify the old password and sets the new password if everything is OK. This API must not be used for resetting user's password. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_password** | **str** | User-entered passsord to be compared to password for change password function.   | [optional] 
**new_password** | **str** | New password that the user&#39;s password should be changed to.   | [optional] 
**password** | **str** | User&#39;s current valid passsord.    | [optional] 
**user** | [**IamUser**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


