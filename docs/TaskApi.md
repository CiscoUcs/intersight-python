# intersight.TaskApi

All URIs are relative to *https://intersight.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task_pure_storage_scoped_inventory**](TaskApi.md#create_task_pure_storage_scoped_inventory) | **POST** /task/PureStorageScopedInventories | Create a &#39;task.PureStorageScopedInventory&#39; resource.


# **create_task_pure_storage_scoped_inventory**
> TaskPureStorageScopedInventory create_task_pure_storage_scoped_inventory(task_pure_storage_scoped_inventory)

Create a 'task.PureStorageScopedInventory' resource.

### Example

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import intersight
from intersight.rest import ApiException
from pprint import pprint
configuration = intersight.Configuration()
# Configure API key authorization: cookieAuth
configuration.api_key['X-Starship-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Starship-Token'] = 'Bearer'
configuration = intersight.Configuration()
# Configure OAuth2 access token for authorization: oAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://intersight.com/api/v1
configuration.host = "https://intersight.com/api/v1"
# Create an instance of the API class
api_instance = intersight.TaskApi(intersight.ApiClient(configuration))
task_pure_storage_scoped_inventory = intersight.TaskPureStorageScopedInventory() # TaskPureStorageScopedInventory | The 'task.PureStorageScopedInventory' resource to create.

try:
    # Create a 'task.PureStorageScopedInventory' resource.
    api_response = api_instance.create_task_pure_storage_scoped_inventory(task_pure_storage_scoped_inventory)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->create_task_pure_storage_scoped_inventory: %s\n" % e)
```

* OAuth Authentication (oAuth2):
```python
from __future__ import print_function
import time
import intersight
from intersight.rest import ApiException
from pprint import pprint
configuration = intersight.Configuration()
# Configure API key authorization: cookieAuth
configuration.api_key['X-Starship-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Starship-Token'] = 'Bearer'
configuration = intersight.Configuration()
# Configure OAuth2 access token for authorization: oAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://intersight.com/api/v1
configuration.host = "https://intersight.com/api/v1"
# Create an instance of the API class
api_instance = intersight.TaskApi(intersight.ApiClient(configuration))
task_pure_storage_scoped_inventory = intersight.TaskPureStorageScopedInventory() # TaskPureStorageScopedInventory | The 'task.PureStorageScopedInventory' resource to create.

try:
    # Create a 'task.PureStorageScopedInventory' resource.
    api_response = api_instance.create_task_pure_storage_scoped_inventory(task_pure_storage_scoped_inventory)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->create_task_pure_storage_scoped_inventory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_pure_storage_scoped_inventory** | [**TaskPureStorageScopedInventory**](TaskPureStorageScopedInventory.md)| The &#39;task.PureStorageScopedInventory&#39; resource to create. | 

### Return type

[**TaskPureStorageScopedInventory**](TaskPureStorageScopedInventory.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;task.PureStorageScopedInventory&#39; resource was created as requested. The &#39;task.PureStorageScopedInventory&#39; resource is created before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;task.PureStorageScopedInventory&#39; resource is asynchronously being created as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

