# ContentGrammar

Content handler framework supports extraction of required values from API/device responses. These responses may be of various content types such as XML, JSON, etc. The values of importance are modeled as parameters in the content handler framework.  The parameters can be of a scalar value type or a collection of values. A group of related parameters can be modeled as a single complex type parameter. These complex types will be very useful to extract a set of repeating group of related parameters.  A grammar specification defines the set of parameters that need to be extracted from the content. The grammar specification allows complex type definitions to be defined for any complex parameters. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_parameters** | [**list[ContentBaseParameter]**](ContentBaseParameter.md) |  | [optional] 
**parameters** | [**list[ContentBaseParameter]**](ContentBaseParameter.md) |  | [optional] 
**types** | [**list[ContentComplexType]**](ContentComplexType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


