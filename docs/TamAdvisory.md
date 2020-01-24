# TamAdvisory

An Intersight Advisory. An advisory represents an identification of a potential issue and may also include  a recommendation for resolving the said issue. Advisories may be of different kind and severity. for e.g. It could be a security vulnerability or a performance issue or a hardware issue with different recommendations for resolving them. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Brief description of the advisory details.   | [optional] 
**name** | **str** | A user defined name for the Intersight Advisory.   | [optional] 
**severity** | [**TamSeverity**](TamSeverity.md) |  | [optional] 
**state** | **str** | Current state of the advisory. Indicates if the user is interested in getting updates for the advisory.    | [optional] [default to 'active']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


