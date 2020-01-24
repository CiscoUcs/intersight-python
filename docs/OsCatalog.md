# OsCatalog

A catalog of operating systems related objects such as configuration files and post install scripts. Each user account will have a local OS catalog where account users can store their private configuration files and post install scripts. Cisco provides validated answer files and post install scripts to Intersight users via shared catalogs. Intersight users will be able to read, use these files and scripts in OS installation within their account context. The shared catalogs will be managed entirely by Cisco. Contributions to shared catalogs will need to be provided to Cisco who will publish them at their own discretion. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The catalog name. There will be one for system and one for each user account.    | [optional] 
**configuration_files** | [**list[OsConfigurationFile]**](OsConfigurationFile.md) | A reference to a osConfigurationFile resource. When the $expand query parameter is specified, the referenced resource is returned inline. This captures the associated Configuration files.  | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


