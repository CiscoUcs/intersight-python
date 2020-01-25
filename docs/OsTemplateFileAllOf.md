# OsTemplateFileAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the OS Template File that user uploads for unattended installation.   | [optional] 
**placeholders** | **list[str]** |  | [optional] 
**template_content** | **str** | The content of the entire template file is stored as value. The content can either be a static file content or a template content.  The template is expected to conform to the golang template syntax.  The placeholders, if any, would be populated and the values provided would be  used to populate this template.     | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


