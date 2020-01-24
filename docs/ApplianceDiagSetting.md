# ApplianceDiagSetting

DiagSetting model is used for changing the password of the operating system's diagnostic user account. The diagnostic user account can be used to login to the Intersight Appliance virtual machine.  The diagnostic user account is protected by two separate authentication mechanisms: user's password and Cisco CT-engine generated key. Only the Intersight Appliance's local account administrator has the privileges to use this REST API. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_password_set** | **bool** |  | [optional] 
**message** | **str** | Status message of the password change operation.   | [optional] 
**password** | **str** | Password of the Intersight Appliance&#39;s OS diagnostic user account.    | [optional] 
**account** | [**IamAccount**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


