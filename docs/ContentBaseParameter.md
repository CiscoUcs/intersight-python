# ContentBaseParameter

A Baseparameter is an abstract definition of specific value to be extracted from a given API or device response.  The BaseParameter object provides the name, type and content specific path, such as XPath or JSONPath, that points to the location of the parameter value in the content. Additional parameters necessary to extract data based on content type needs to extend BaseParameter. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_single_value** | **bool** | The flag that allows single values in content to be extracted as a single element collection in case the parameter is of Collection type.  This flag is applicable for parameters of type Collection only.    | [optional] 
**complex_type** | **str** | The name of the complex type definition in case this is a complex parameter. The content.Grammar object must have a complex type, content.ComplexType, defined with the specified name in types collection property.    | [optional] 
**item_type** | **str** | The type of the collection item in case this is a collection parameter.    | [optional] [default to 'simple']
**name** | **str** | The name of the parameter.   | [optional] 
**path** | **str** | The content specific path information that identifies the parameter value within the content. The value is usually a XPath or JSONPath or a regular expression in case of text content.    | [optional] 
**type** | **str** | The type of the parameter. Accepted values are simple, complex, collection.     | [optional] [default to 'simple']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


