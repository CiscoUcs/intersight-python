# LicenseAccountLicenseData

License information for an account. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Root user&#39;s ID of the account.   | [optional] [readonly] 
**agent_data** | **str** | Agent trusted store data.   | [optional] [readonly] 
**auth_expire_time** | **str** | Authorization expiration time.   | [optional] [readonly] 
**auth_initial_time** | **str** | Intial authorization time.   | [optional] [readonly] 
**auth_next_time** | **str** | Next time for the authorization.   | [optional] [readonly] 
**category** | **str** | Account license data category name.   | [optional] [readonly] 
**default_license_type** | **str** | Default license tier set by user.    | [optional] [default to 'Base']
**group** | **str** | Account license data group name.   | [optional] [readonly] 
**last_sync** | **datetime** | Specifies last sync time with SA.   | [optional] [readonly] 
**last_updated_time** | **datetime** | Record&#39;s last update datetime.   | [optional] [readonly] 
**license_state** | **str** | Aggregrated mode for the agent.   | [optional] [readonly] 
**license_tech_support_info** | **str** | Tech-support info of a smart-agent.   | [optional] [readonly] 
**register_expire_time** | **str** | Registration exipiration time.   | [optional] [readonly] 
**register_initial_time** | **str** | Initial time of registration.   | [optional] [readonly] 
**register_next_time** | **str** | Next time for the license registration.   | [optional] [readonly] 
**registration_status** | **str** | Registration status of a smart-agent.   | [optional] [readonly] 
**renew_failure_string** | **str** | License renewal failure message.   | [optional] [readonly] 
**smart_account** | **str** | Name of the smart account.   | [optional] [readonly] 
**sync_status** | **str** | Current sync status for the account.   | [optional] [readonly] 
**virtual_account** | **str** | Name of the virtual account.    | [optional] [readonly] 
**account** | [**IamAccount**](.md) |  | [optional] 
**customer_op** | [**LicenseCustomerOp**](.md) |  | [optional] 
**licenseinfos** | [**list[LicenseLicenseInfo]**](LicenseLicenseInfo.md) | A reference to a licenseLicenseInfo resource. When the $expand query parameter is specified, the referenced resource is returned inline. All LicenceInfo records refercing this AccountLicenseData record.  | [optional] 
**smartlicense_token** | [**LicenseSmartlicenseToken**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


