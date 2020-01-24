# TamQueryEntry

Contains a set of queries, each with an integer priority. the queries are executed in the order of specified priority. The result of each query is used as an input to the query next in priority order. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name is used to unique identify and result of the given query which can be used by subsequent queries as input data source.   | [optional] 
**priority** | **int** | An integer value depicting the priority of the query among the queries that are part of the same QueryEntry collection.   | [optional] 
**query** | **str** | A SparkSQL query to be used on a given data source.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


