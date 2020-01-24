# OsConfigurationFileAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_content** | **str** | The content of the entire configuration file is stored as value. The content can either be a static file content or a template content.  The template is expected to conform to the golang template syntax. The values from os.Answers properties will be used to populate this template.    | [optional] 
**name** | **str** | The name of the OS ConfigurationFile that uniquely identifies the configuration file.   | [optional] 
**placeholders** | [**list[OsPlaceHolder]**](OsPlaceHolder.md) |  | [optional] 
**supported** | **bool** | An internal property that is used to distinguish between the pre-canned OS configuration file entries and user provided entries.     | [optional] [readonly] 
**catalog** | [**OsCatalog**](.md) |  | [optional] 
**distributions** | [**list[HclOperatingSystem]**](HclOperatingSystem.md) | A reference to a hclOperatingSystem resource. When the $expand query parameter is specified, the referenced resource is returned inline. This captures the operating system for which this configuration file is defined.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


