# SearchSuggestItem

The Suggester service entry point to suggest Intersight REST resources using Elastic Search suggester API syntax. The suggest feature suggests similar looking terms based on a provided text by using a suggester.  See [Search API query syntax](/apidocs/introduction/query/#global-search-api) for details about the suggester query syntax. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complete_mo** | **bool** | Flag for returning complete objects that matched the global search criteria.   | [optional] 
**rawquery** | **str** | Additional filter parameters for global search. You can also specify OData select fields here. Maximum Query Length is limited to 10000.   | [optional] 
**skip** | **int** | Starting offset for the results to be returned from external search engine.   | [optional] 
**suggest_term** | **str** | Main search term used for global search across all Managed Objects that has search enabled. Search Term can be up to 200 characters long.   | [optional] 
**top** | **int** | Maximum number of results to be returned from external search engine.   | [optional] 
**type** | **str** | Object type filter of a Managed Object. Search will be restricted only on the specified object types.  Do not provide IndexMoTypes filter in the rawquery, if you specify values in this field.     | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


