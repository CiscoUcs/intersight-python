# I18nMessage

An i18n message that can be translated in multiple languages to support internationalization.  An i18n message includes a unique message identifier, a text format string, a list of message parameters that can be used  to substitute parameters, and a translated string based on a user's locale. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The default (en-US) localized message. Default localized message will be stored and directly retrieved when the user&#39;s locale setting is en-US.    | [optional] [readonly] 
**message_id** | **str** | The unique message identitifer used to lookup text templates in a multi-language message catalog.   | [optional] [readonly] 
**message_params** | [**list[I18nMessageParam]**](I18nMessageParam.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


