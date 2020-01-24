# ContentTextParameterAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_delimiter** | **bool** | Data to be extracted from text content can be simple type or complex type or collection of simple/complex types. Complex types are group of simple or complex type.  Delimiter is required to stop parsing list and complex data types.  isDelimiter specifies whether given TextParameter is a delimiter or regular rule to capture the text data.    | [optional] 
**is_next_capture_on_same_line** | **bool** | Set to true of the next value to capture resides on the same text line of current match. By default textFSM engine gets the next text line on finding the first match.    | [optional] 
**regex_line** | **str** | Regular expression of the line containing the data to be extracted from text content.     | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


