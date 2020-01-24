# VmediaPolicyAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | State of the Virtual Media service on the endpoint.   | [optional] 
**encryption** | **bool** | If enabled, allows encryption of all Virtual Media communications.   | [optional] 
**low_power_usb** | **bool** | If enabled, the virtual drives appear on the boot selection menu after mapping the image and rebooting the host.   | [optional] 
**mappings** | [**list[VmediaMapping]**](VmediaMapping.md) |  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 
**profiles** | [**list[PolicyAbstractConfigProfile]**](PolicyAbstractConfigProfile.md) | A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the profile object.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


