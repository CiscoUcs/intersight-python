# intersight.OsApi

All URIs are relative to *https://intersight.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_os_configuration_file**](OsApi.md#create_os_configuration_file) | **POST** /os/ConfigurationFiles | Create a &#39;os.ConfigurationFile&#39; resource.
[**create_os_install**](OsApi.md#create_os_install) | **POST** /os/Installs | Create a &#39;os.Install&#39; resource.
[**create_os_os_support**](OsApi.md#create_os_os_support) | **POST** /os/OsSupports | Create a &#39;os.OsSupport&#39; resource.
[**create_os_template_file**](OsApi.md#create_os_template_file) | **POST** /os/TemplateFiles | Create a &#39;os.TemplateFile&#39; resource.
[**delete_os_configuration_file**](OsApi.md#delete_os_configuration_file) | **DELETE** /os/ConfigurationFiles/{Moid} | Delete a &#39;os.ConfigurationFile&#39; resource.
[**get_os_catalog_by_moid**](OsApi.md#get_os_catalog_by_moid) | **GET** /os/Catalogs/{Moid} | Read a &#39;os.Catalog&#39; resource.
[**get_os_catalog_list**](OsApi.md#get_os_catalog_list) | **GET** /os/Catalogs | Read a &#39;os.Catalog&#39; resource.
[**get_os_configuration_file_by_moid**](OsApi.md#get_os_configuration_file_by_moid) | **GET** /os/ConfigurationFiles/{Moid} | Read a &#39;os.ConfigurationFile&#39; resource.
[**get_os_configuration_file_list**](OsApi.md#get_os_configuration_file_list) | **GET** /os/ConfigurationFiles | Read a &#39;os.ConfigurationFile&#39; resource.
[**get_os_install_by_moid**](OsApi.md#get_os_install_by_moid) | **GET** /os/Installs/{Moid} | Read a &#39;os.Install&#39; resource.
[**get_os_install_list**](OsApi.md#get_os_install_list) | **GET** /os/Installs | Read a &#39;os.Install&#39; resource.


# **create_os_configuration_file**
> OsConfigurationFile create_os_configuration_file(os_configuration_file)

Create a 'os.ConfigurationFile' resource.

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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
os_configuration_file = intersight.OsConfigurationFile() # OsConfigurationFile | The 'os.ConfigurationFile' resource to create.

try:
    # Create a 'os.ConfigurationFile' resource.
    api_response = api_instance.create_os_configuration_file(os_configuration_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->create_os_configuration_file: %s\n" % e)
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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
os_configuration_file = intersight.OsConfigurationFile() # OsConfigurationFile | The 'os.ConfigurationFile' resource to create.

try:
    # Create a 'os.ConfigurationFile' resource.
    api_response = api_instance.create_os_configuration_file(os_configuration_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->create_os_configuration_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os_configuration_file** | [**OsConfigurationFile**](OsConfigurationFile.md)| The &#39;os.ConfigurationFile&#39; resource to create. | 

### Return type

[**OsConfigurationFile**](OsConfigurationFile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;os.ConfigurationFile&#39; resource was created as requested. The &#39;os.ConfigurationFile&#39; resource is created before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;os.ConfigurationFile&#39; resource is asynchronously being created as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_os_install**
> OsInstall create_os_install(os_install)

Create a 'os.Install' resource.

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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
os_install = intersight.OsInstall() # OsInstall | The 'os.Install' resource to create.

try:
    # Create a 'os.Install' resource.
    api_response = api_instance.create_os_install(os_install)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->create_os_install: %s\n" % e)
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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
os_install = intersight.OsInstall() # OsInstall | The 'os.Install' resource to create.

try:
    # Create a 'os.Install' resource.
    api_response = api_instance.create_os_install(os_install)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->create_os_install: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os_install** | [**OsInstall**](OsInstall.md)| The &#39;os.Install&#39; resource to create. | 

### Return type

[**OsInstall**](OsInstall.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;os.Install&#39; resource was created as requested. The &#39;os.Install&#39; resource is created before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;os.Install&#39; resource is asynchronously being created as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_os_os_support**
> OsOsSupport create_os_os_support(os_os_support)

Create a 'os.OsSupport' resource.

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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
os_os_support = intersight.OsOsSupport() # OsOsSupport | The 'os.OsSupport' resource to create.

try:
    # Create a 'os.OsSupport' resource.
    api_response = api_instance.create_os_os_support(os_os_support)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->create_os_os_support: %s\n" % e)
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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
os_os_support = intersight.OsOsSupport() # OsOsSupport | The 'os.OsSupport' resource to create.

try:
    # Create a 'os.OsSupport' resource.
    api_response = api_instance.create_os_os_support(os_os_support)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->create_os_os_support: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os_os_support** | [**OsOsSupport**](OsOsSupport.md)| The &#39;os.OsSupport&#39; resource to create. | 

### Return type

[**OsOsSupport**](OsOsSupport.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;os.OsSupport&#39; resource was created as requested. The &#39;os.OsSupport&#39; resource is created before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;os.OsSupport&#39; resource is asynchronously being created as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_os_template_file**
> OsTemplateFile create_os_template_file(os_template_file)

Create a 'os.TemplateFile' resource.

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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
os_template_file = intersight.OsTemplateFile() # OsTemplateFile | The 'os.TemplateFile' resource to create.

try:
    # Create a 'os.TemplateFile' resource.
    api_response = api_instance.create_os_template_file(os_template_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->create_os_template_file: %s\n" % e)
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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
os_template_file = intersight.OsTemplateFile() # OsTemplateFile | The 'os.TemplateFile' resource to create.

try:
    # Create a 'os.TemplateFile' resource.
    api_response = api_instance.create_os_template_file(os_template_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->create_os_template_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os_template_file** | [**OsTemplateFile**](OsTemplateFile.md)| The &#39;os.TemplateFile&#39; resource to create. | 

### Return type

[**OsTemplateFile**](OsTemplateFile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;os.TemplateFile&#39; resource was created as requested. The &#39;os.TemplateFile&#39; resource is created before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;os.TemplateFile&#39; resource is asynchronously being created as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_os_configuration_file**
> delete_os_configuration_file(moid)

Delete a 'os.ConfigurationFile' resource.

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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Delete a 'os.ConfigurationFile' resource.
    api_instance.delete_os_configuration_file(moid)
except ApiException as e:
    print("Exception when calling OsApi->delete_os_configuration_file: %s\n" % e)
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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Delete a 'os.ConfigurationFile' resource.
    api_instance.delete_os_configuration_file(moid)
except ApiException as e:
    print("Exception when calling OsApi->delete_os_configuration_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource has been deleted successfully. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The request has been accepted, the resource is being deleted asynchronously. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_catalog_by_moid**
> OsCatalog get_os_catalog_by_moid(moid)

Read a 'os.Catalog' resource.

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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'os.Catalog' resource.
    api_response = api_instance.get_os_catalog_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->get_os_catalog_by_moid: %s\n" % e)
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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'os.Catalog' resource.
    api_response = api_instance.get_os_catalog_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->get_os_catalog_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**OsCatalog**](OsCatalog.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;os.Catalog&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_catalog_list**
> OsCatalogList get_os_catalog_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'os.Catalog' resource.

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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
filter = '' # str | Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false).  (optional) (default to '')
orderby = '$orderby=CreationTime' # str | Determines what properties are used to sort the collection of resources. (optional)
top = 100 # int | Specifies the maximum number of resources to return in the response. (optional) (default to 100)
skip = 0 # int | Specifies the number of resources to skip in the response. (optional) (default to 0)
select = '' # str | Specifies a subset of properties to return. (optional) (default to '')
expand = '$expand=DisplayNames' # str | Specify additional attributes or related resources to return in addition to the primary resources. (optional)
apply = 'apply_example' # str | Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set.  (optional)
count = $count=true # bool | The $count query specifies the service should return the count of the matching resources, instead of returning the resources. (optional)
inlinecount = 'allpages' # str | The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. (optional) (default to 'allpages')
at = 'at=VersionType eq 'Configured'' # str | Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section.  (optional)

try:
    # Read a 'os.Catalog' resource.
    api_response = api_instance.get_os_catalog_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->get_os_catalog_list: %s\n" % e)
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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
filter = '' # str | Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false).  (optional) (default to '')
orderby = '$orderby=CreationTime' # str | Determines what properties are used to sort the collection of resources. (optional)
top = 100 # int | Specifies the maximum number of resources to return in the response. (optional) (default to 100)
skip = 0 # int | Specifies the number of resources to skip in the response. (optional) (default to 0)
select = '' # str | Specifies a subset of properties to return. (optional) (default to '')
expand = '$expand=DisplayNames' # str | Specify additional attributes or related resources to return in addition to the primary resources. (optional)
apply = 'apply_example' # str | Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set.  (optional)
count = $count=true # bool | The $count query specifies the service should return the count of the matching resources, instead of returning the resources. (optional)
inlinecount = 'allpages' # str | The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. (optional) (default to 'allpages')
at = 'at=VersionType eq 'Configured'' # str | Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section.  (optional)

try:
    # Read a 'os.Catalog' resource.
    api_response = api_instance.get_os_catalog_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->get_os_catalog_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false).  | [optional] [default to &#39;&#39;]
 **orderby** | **str**| Determines what properties are used to sort the collection of resources. | [optional] 
 **top** | **int**| Specifies the maximum number of resources to return in the response. | [optional] [default to 100]
 **skip** | **int**| Specifies the number of resources to skip in the response. | [optional] [default to 0]
 **select** | **str**| Specifies a subset of properties to return. | [optional] [default to &#39;&#39;]
 **expand** | **str**| Specify additional attributes or related resources to return in addition to the primary resources. | [optional] 
 **apply** | **str**| Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \&quot;$apply\&quot; query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \&quot;aggregate\&quot; and \&quot;groupby\&quot;. The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set.  | [optional] 
 **count** | **bool**| The $count query specifies the service should return the count of the matching resources, instead of returning the resources. | [optional] 
 **inlinecount** | **str**| The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. | [optional] [default to &#39;allpages&#39;]
 **at** | **str**| Similar to \&quot;$filter\&quot;, but \&quot;at\&quot; is specifically used to filter versioning information properties for resources to return. A URI with an \&quot;at\&quot; Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section.  | [optional] 

### Return type

[**OsCatalogList**](OsCatalogList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;os.Catalog&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_configuration_file_by_moid**
> OsConfigurationFile get_os_configuration_file_by_moid(moid)

Read a 'os.ConfigurationFile' resource.

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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'os.ConfigurationFile' resource.
    api_response = api_instance.get_os_configuration_file_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->get_os_configuration_file_by_moid: %s\n" % e)
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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'os.ConfigurationFile' resource.
    api_response = api_instance.get_os_configuration_file_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->get_os_configuration_file_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**OsConfigurationFile**](OsConfigurationFile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;os.ConfigurationFile&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_configuration_file_list**
> OsConfigurationFileList get_os_configuration_file_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'os.ConfigurationFile' resource.

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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
filter = '' # str | Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false).  (optional) (default to '')
orderby = '$orderby=CreationTime' # str | Determines what properties are used to sort the collection of resources. (optional)
top = 100 # int | Specifies the maximum number of resources to return in the response. (optional) (default to 100)
skip = 0 # int | Specifies the number of resources to skip in the response. (optional) (default to 0)
select = '' # str | Specifies a subset of properties to return. (optional) (default to '')
expand = '$expand=DisplayNames' # str | Specify additional attributes or related resources to return in addition to the primary resources. (optional)
apply = 'apply_example' # str | Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set.  (optional)
count = $count=true # bool | The $count query specifies the service should return the count of the matching resources, instead of returning the resources. (optional)
inlinecount = 'allpages' # str | The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. (optional) (default to 'allpages')
at = 'at=VersionType eq 'Configured'' # str | Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section.  (optional)

try:
    # Read a 'os.ConfigurationFile' resource.
    api_response = api_instance.get_os_configuration_file_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->get_os_configuration_file_list: %s\n" % e)
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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
filter = '' # str | Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false).  (optional) (default to '')
orderby = '$orderby=CreationTime' # str | Determines what properties are used to sort the collection of resources. (optional)
top = 100 # int | Specifies the maximum number of resources to return in the response. (optional) (default to 100)
skip = 0 # int | Specifies the number of resources to skip in the response. (optional) (default to 0)
select = '' # str | Specifies a subset of properties to return. (optional) (default to '')
expand = '$expand=DisplayNames' # str | Specify additional attributes or related resources to return in addition to the primary resources. (optional)
apply = 'apply_example' # str | Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set.  (optional)
count = $count=true # bool | The $count query specifies the service should return the count of the matching resources, instead of returning the resources. (optional)
inlinecount = 'allpages' # str | The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. (optional) (default to 'allpages')
at = 'at=VersionType eq 'Configured'' # str | Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section.  (optional)

try:
    # Read a 'os.ConfigurationFile' resource.
    api_response = api_instance.get_os_configuration_file_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->get_os_configuration_file_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false).  | [optional] [default to &#39;&#39;]
 **orderby** | **str**| Determines what properties are used to sort the collection of resources. | [optional] 
 **top** | **int**| Specifies the maximum number of resources to return in the response. | [optional] [default to 100]
 **skip** | **int**| Specifies the number of resources to skip in the response. | [optional] [default to 0]
 **select** | **str**| Specifies a subset of properties to return. | [optional] [default to &#39;&#39;]
 **expand** | **str**| Specify additional attributes or related resources to return in addition to the primary resources. | [optional] 
 **apply** | **str**| Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \&quot;$apply\&quot; query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \&quot;aggregate\&quot; and \&quot;groupby\&quot;. The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set.  | [optional] 
 **count** | **bool**| The $count query specifies the service should return the count of the matching resources, instead of returning the resources. | [optional] 
 **inlinecount** | **str**| The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. | [optional] [default to &#39;allpages&#39;]
 **at** | **str**| Similar to \&quot;$filter\&quot;, but \&quot;at\&quot; is specifically used to filter versioning information properties for resources to return. A URI with an \&quot;at\&quot; Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section.  | [optional] 

### Return type

[**OsConfigurationFileList**](OsConfigurationFileList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;os.ConfigurationFile&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_install_by_moid**
> OsInstall get_os_install_by_moid(moid)

Read a 'os.Install' resource.

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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'os.Install' resource.
    api_response = api_instance.get_os_install_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->get_os_install_by_moid: %s\n" % e)
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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'os.Install' resource.
    api_response = api_instance.get_os_install_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->get_os_install_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**OsInstall**](OsInstall.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;os.Install&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_install_list**
> OsInstallList get_os_install_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'os.Install' resource.

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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
filter = '' # str | Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false).  (optional) (default to '')
orderby = '$orderby=CreationTime' # str | Determines what properties are used to sort the collection of resources. (optional)
top = 100 # int | Specifies the maximum number of resources to return in the response. (optional) (default to 100)
skip = 0 # int | Specifies the number of resources to skip in the response. (optional) (default to 0)
select = '' # str | Specifies a subset of properties to return. (optional) (default to '')
expand = '$expand=DisplayNames' # str | Specify additional attributes or related resources to return in addition to the primary resources. (optional)
apply = 'apply_example' # str | Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set.  (optional)
count = $count=true # bool | The $count query specifies the service should return the count of the matching resources, instead of returning the resources. (optional)
inlinecount = 'allpages' # str | The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. (optional) (default to 'allpages')
at = 'at=VersionType eq 'Configured'' # str | Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section.  (optional)

try:
    # Read a 'os.Install' resource.
    api_response = api_instance.get_os_install_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->get_os_install_list: %s\n" % e)
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
api_instance = intersight.OsApi(intersight.ApiClient(configuration))
filter = '' # str | Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false).  (optional) (default to '')
orderby = '$orderby=CreationTime' # str | Determines what properties are used to sort the collection of resources. (optional)
top = 100 # int | Specifies the maximum number of resources to return in the response. (optional) (default to 100)
skip = 0 # int | Specifies the number of resources to skip in the response. (optional) (default to 0)
select = '' # str | Specifies a subset of properties to return. (optional) (default to '')
expand = '$expand=DisplayNames' # str | Specify additional attributes or related resources to return in addition to the primary resources. (optional)
apply = 'apply_example' # str | Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set.  (optional)
count = $count=true # bool | The $count query specifies the service should return the count of the matching resources, instead of returning the resources. (optional)
inlinecount = 'allpages' # str | The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. (optional) (default to 'allpages')
at = 'at=VersionType eq 'Configured'' # str | Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section.  (optional)

try:
    # Read a 'os.Install' resource.
    api_response = api_instance.get_os_install_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->get_os_install_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false).  | [optional] [default to &#39;&#39;]
 **orderby** | **str**| Determines what properties are used to sort the collection of resources. | [optional] 
 **top** | **int**| Specifies the maximum number of resources to return in the response. | [optional] [default to 100]
 **skip** | **int**| Specifies the number of resources to skip in the response. | [optional] [default to 0]
 **select** | **str**| Specifies a subset of properties to return. | [optional] [default to &#39;&#39;]
 **expand** | **str**| Specify additional attributes or related resources to return in addition to the primary resources. | [optional] 
 **apply** | **str**| Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \&quot;$apply\&quot; query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \&quot;aggregate\&quot; and \&quot;groupby\&quot;. The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set.  | [optional] 
 **count** | **bool**| The $count query specifies the service should return the count of the matching resources, instead of returning the resources. | [optional] 
 **inlinecount** | **str**| The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. | [optional] [default to &#39;allpages&#39;]
 **at** | **str**| Similar to \&quot;$filter\&quot;, but \&quot;at\&quot; is specifically used to filter versioning information properties for resources to return. A URI with an \&quot;at\&quot; Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section.  | [optional] 

### Return type

[**OsInstallList**](OsInstallList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;os.Install&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

