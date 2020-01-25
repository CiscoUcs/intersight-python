# LicenseLicenseInfo

License state information for a specific license entitlement. Essentials license entitlement is supported currently. licenseState attribute is used for license enforcement. When license state is one of TrialPeriod, Compliance, or OutOfCompliance, the feature set defined for the license entitlement is granted to the customer. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_admin** | **bool** | The license administrative state.  Set this property to &#39;true&#39; to activate the license entitlements.    | [optional] 
**days_left** | **int** | The number of days left for licenseState to stay in TrialPeriod or OutOfCompliance state.   | [optional] [readonly] 
**end_time** | **datetime** | The date and time when the trial period expires.  The value of the &#39;endTime&#39; property is set when the account enters the TrialPeriod or OutOfCompliance state.    | [optional] [readonly] 
**enforce_mode** | **str** | The entitlement mode reported by Cisco Smart Software Manager.   | [optional] [readonly] 
**error_desc** | **str** | The detailed error message when there is any error related to this licensing entitlement.   | [optional] [readonly] 
**evaluation_period** | **int** | The default Trial or Grace period customer is entitled to.   | [optional] 
**extra_evaluation** | **int** | The number of days the trial Trial or Grace period is extended.  The trial or grace period can be extended once.    | [optional] 
**license_count** | **int** | The total number of devices claimed in the Intersight account.   | [optional] [readonly] 
**license_state** | **str** | The license state defined by Intersight.  The value may be one of NotLicensed, TrialPeriod, OutOfCompliance, Compliance, GraceExpired, or TrialExpired.    | [optional] [readonly] [default to 'NotLicensed']
**license_type** | **str** | The name of the Intersight license entitlement. For example, this property may be set to &#39;Essential&#39;.    | [optional] [readonly] [default to 'Base']
**start_time** | **datetime** | The date and time when the licenseState entered the TrialPeriod or OutOfCompliance state.   | [optional] [readonly] 
**trial_admin** | **bool** | The administrative state of the trial license.  When the LicenseState is set to &#39;NotLicensed&#39;, &#39;trialAdmin&#39; can be set to true to start the trial period, i.e. licenseState is set to be TrialPeriod.     | [optional] 
**account_license_data** | [**LicenseAccountLicenseData**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


