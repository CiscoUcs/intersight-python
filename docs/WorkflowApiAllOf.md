# WorkflowApiAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The optional request body that is sent as part of this API request.  The request body can contain a golang template that can be populated with task input parameters and previous API output parameters.    | [optional] 
**content_type** | **str** | Intersight Orchestrator, with the support of response parser specification, can extract the values from API responses and map them to task output parameters. The value extraction is supported for response content types XML and JSON.  The type of the content that gets passed as payload and response in this API.    | [optional] [default to 'json']
**name** | **str** | A reference name for this API request within the batch API request.  This name shall be used to map the API output parameters to subsequent API input parameters within a batch API task.    | [optional] 
**outcomes** | [**object**](.md) | All the possible outcomes of this API are captured here. Outcomes property is a collection property of type workflow.Outcome objects.  The outcomes can be mapped to the message to be shown. The outcomes are evaluated in the order they are given. At the end of the outcomes list, an catchall success/fail outcome can be added with condition as &#39;true&#39;.  This is an optional property and if not specified the task will be marked as success.    | [optional] 
**response_spec** | [**ContentGrammar**](ContentGrammar.md) |  | [optional] 
**skip_on_condition** | **str** | The skip expression, if provided, allows the batch API executor to skip the api execution when the given expression evaluates to true.  The expression is given as such a golang template that has to be evaluated to a final content true/false. The expression is an optional and in case not provided, the API will always be executed.    | [optional] 
**timeout** | **int** | The duration in seconds by which the API response is expected from the API target.  If the end point does not respond for the API request within this timeout duration, the task will be marked as failed.     | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


