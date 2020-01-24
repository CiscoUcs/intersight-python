# WorkflowWaitTask

A WaitTask will remain in progress until marked success or failed by an external trigger. The timeout for wait task is 180 days, so a workflow can wait for task status update for upto 180 days. Currently the only supported means to update the task status is through an API that provides the status of the task runtime instance. Once the wait task status has been set the workflow will continue with the execution based on the task status. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


