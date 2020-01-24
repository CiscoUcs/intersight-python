# intersight.LicenseApi

All URIs are relative to *https://intersight.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_license_license_info**](LicenseApi.md#create_license_license_info) | **POST** /license/LicenseInfos | Create a &#39;license.LicenseInfo&#39; resource.
[**get_license_account_license_data_by_moid**](LicenseApi.md#get_license_account_license_data_by_moid) | **GET** /license/AccountLicenseData/{Moid} | Read a &#39;license.AccountLicenseData&#39; resource.
[**get_license_account_license_data_list**](LicenseApi.md#get_license_account_license_data_list) | **GET** /license/AccountLicenseData | Read a &#39;license.AccountLicenseData&#39; resource.
[**get_license_customer_op_by_moid**](LicenseApi.md#get_license_customer_op_by_moid) | **GET** /license/CustomerOps/{Moid} | Read a &#39;license.CustomerOp&#39; resource.
[**get_license_customer_op_list**](LicenseApi.md#get_license_customer_op_list) | **GET** /license/CustomerOps | Read a &#39;license.CustomerOp&#39; resource.
[**get_license_license_info_by_moid**](LicenseApi.md#get_license_license_info_by_moid) | **GET** /license/LicenseInfos/{Moid} | Read a &#39;license.LicenseInfo&#39; resource.
[**get_license_license_info_list**](LicenseApi.md#get_license_license_info_list) | **GET** /license/LicenseInfos | Read a &#39;license.LicenseInfo&#39; resource.
[**get_license_smartlicense_token_by_moid**](LicenseApi.md#get_license_smartlicense_token_by_moid) | **GET** /license/SmartlicenseTokens/{Moid} | Read a &#39;license.SmartlicenseToken&#39; resource.
[**get_license_smartlicense_token_list**](LicenseApi.md#get_license_smartlicense_token_list) | **GET** /license/SmartlicenseTokens | Read a &#39;license.SmartlicenseToken&#39; resource.
[**patch_license_account_license_data**](LicenseApi.md#patch_license_account_license_data) | **PATCH** /license/AccountLicenseData/{Moid} | Update a &#39;license.AccountLicenseData&#39; resource.
[**patch_license_customer_op**](LicenseApi.md#patch_license_customer_op) | **PATCH** /license/CustomerOps/{Moid} | Update a &#39;license.CustomerOp&#39; resource.
[**patch_license_license_info**](LicenseApi.md#patch_license_license_info) | **PATCH** /license/LicenseInfos/{Moid} | Update a &#39;license.LicenseInfo&#39; resource.
[**patch_license_smartlicense_token**](LicenseApi.md#patch_license_smartlicense_token) | **PATCH** /license/SmartlicenseTokens/{Moid} | Update a &#39;license.SmartlicenseToken&#39; resource.
[**update_license_account_license_data**](LicenseApi.md#update_license_account_license_data) | **POST** /license/AccountLicenseData/{Moid} | Update a &#39;license.AccountLicenseData&#39; resource.
[**update_license_customer_op**](LicenseApi.md#update_license_customer_op) | **POST** /license/CustomerOps/{Moid} | Update a &#39;license.CustomerOp&#39; resource.
[**update_license_license_info**](LicenseApi.md#update_license_license_info) | **POST** /license/LicenseInfos/{Moid} | Update a &#39;license.LicenseInfo&#39; resource.
[**update_license_smartlicense_token**](LicenseApi.md#update_license_smartlicense_token) | **POST** /license/SmartlicenseTokens/{Moid} | Update a &#39;license.SmartlicenseToken&#39; resource.


# **create_license_license_info**
> LicenseLicenseInfo create_license_license_info(license_license_info)

Create a 'license.LicenseInfo' resource.

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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
license_license_info = intersight.LicenseLicenseInfo() # LicenseLicenseInfo | The 'license.LicenseInfo' resource to create.

try:
    # Create a 'license.LicenseInfo' resource.
    api_response = api_instance.create_license_license_info(license_license_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->create_license_license_info: %s\n" % e)
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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
license_license_info = intersight.LicenseLicenseInfo() # LicenseLicenseInfo | The 'license.LicenseInfo' resource to create.

try:
    # Create a 'license.LicenseInfo' resource.
    api_response = api_instance.create_license_license_info(license_license_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->create_license_license_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_license_info** | [**LicenseLicenseInfo**](LicenseLicenseInfo.md)| The &#39;license.LicenseInfo&#39; resource to create. | 

### Return type

[**LicenseLicenseInfo**](LicenseLicenseInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;license.LicenseInfo&#39; resource was created as requested. The &#39;license.LicenseInfo&#39; resource is created before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;license.LicenseInfo&#39; resource is asynchronously being created as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_account_license_data_by_moid**
> LicenseAccountLicenseData get_license_account_license_data_by_moid(moid)

Read a 'license.AccountLicenseData' resource.

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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'license.AccountLicenseData' resource.
    api_response = api_instance.get_license_account_license_data_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_account_license_data_by_moid: %s\n" % e)
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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'license.AccountLicenseData' resource.
    api_response = api_instance.get_license_account_license_data_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_account_license_data_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**LicenseAccountLicenseData**](LicenseAccountLicenseData.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;license.AccountLicenseData&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_account_license_data_list**
> LicenseAccountLicenseDataList get_license_account_license_data_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'license.AccountLicenseData' resource.

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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
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
    # Read a 'license.AccountLicenseData' resource.
    api_response = api_instance.get_license_account_license_data_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_account_license_data_list: %s\n" % e)
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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
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
    # Read a 'license.AccountLicenseData' resource.
    api_response = api_instance.get_license_account_license_data_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_account_license_data_list: %s\n" % e)
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

[**LicenseAccountLicenseDataList**](LicenseAccountLicenseDataList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;license.AccountLicenseData&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_customer_op_by_moid**
> LicenseCustomerOp get_license_customer_op_by_moid(moid)

Read a 'license.CustomerOp' resource.

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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'license.CustomerOp' resource.
    api_response = api_instance.get_license_customer_op_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_customer_op_by_moid: %s\n" % e)
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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'license.CustomerOp' resource.
    api_response = api_instance.get_license_customer_op_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_customer_op_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**LicenseCustomerOp**](LicenseCustomerOp.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;license.CustomerOp&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_customer_op_list**
> LicenseCustomerOpList get_license_customer_op_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'license.CustomerOp' resource.

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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
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
    # Read a 'license.CustomerOp' resource.
    api_response = api_instance.get_license_customer_op_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_customer_op_list: %s\n" % e)
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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
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
    # Read a 'license.CustomerOp' resource.
    api_response = api_instance.get_license_customer_op_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_customer_op_list: %s\n" % e)
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

[**LicenseCustomerOpList**](LicenseCustomerOpList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;license.CustomerOp&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_license_info_by_moid**
> LicenseLicenseInfo get_license_license_info_by_moid(moid)

Read a 'license.LicenseInfo' resource.

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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'license.LicenseInfo' resource.
    api_response = api_instance.get_license_license_info_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_license_info_by_moid: %s\n" % e)
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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'license.LicenseInfo' resource.
    api_response = api_instance.get_license_license_info_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_license_info_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**LicenseLicenseInfo**](LicenseLicenseInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;license.LicenseInfo&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_license_info_list**
> LicenseLicenseInfoList get_license_license_info_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'license.LicenseInfo' resource.

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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
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
    # Read a 'license.LicenseInfo' resource.
    api_response = api_instance.get_license_license_info_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_license_info_list: %s\n" % e)
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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
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
    # Read a 'license.LicenseInfo' resource.
    api_response = api_instance.get_license_license_info_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_license_info_list: %s\n" % e)
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

[**LicenseLicenseInfoList**](LicenseLicenseInfoList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;license.LicenseInfo&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_smartlicense_token_by_moid**
> LicenseSmartlicenseToken get_license_smartlicense_token_by_moid(moid)

Read a 'license.SmartlicenseToken' resource.

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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'license.SmartlicenseToken' resource.
    api_response = api_instance.get_license_smartlicense_token_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_smartlicense_token_by_moid: %s\n" % e)
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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'license.SmartlicenseToken' resource.
    api_response = api_instance.get_license_smartlicense_token_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_smartlicense_token_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**LicenseSmartlicenseToken**](LicenseSmartlicenseToken.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;license.SmartlicenseToken&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_smartlicense_token_list**
> LicenseSmartlicenseTokenList get_license_smartlicense_token_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'license.SmartlicenseToken' resource.

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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
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
    # Read a 'license.SmartlicenseToken' resource.
    api_response = api_instance.get_license_smartlicense_token_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_smartlicense_token_list: %s\n" % e)
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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
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
    # Read a 'license.SmartlicenseToken' resource.
    api_response = api_instance.get_license_smartlicense_token_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_smartlicense_token_list: %s\n" % e)
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

[**LicenseSmartlicenseTokenList**](LicenseSmartlicenseTokenList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;license.SmartlicenseToken&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_license_account_license_data**
> LicenseAccountLicenseData patch_license_account_license_data(moid, license_account_license_data)

Update a 'license.AccountLicenseData' resource.

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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
license_account_license_data = intersight.LicenseAccountLicenseData() # LicenseAccountLicenseData | The 'license.AccountLicenseData' resource to update.

try:
    # Update a 'license.AccountLicenseData' resource.
    api_response = api_instance.patch_license_account_license_data(moid, license_account_license_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->patch_license_account_license_data: %s\n" % e)
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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
license_account_license_data = intersight.LicenseAccountLicenseData() # LicenseAccountLicenseData | The 'license.AccountLicenseData' resource to update.

try:
    # Update a 'license.AccountLicenseData' resource.
    api_response = api_instance.patch_license_account_license_data(moid, license_account_license_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->patch_license_account_license_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **license_account_license_data** | [**LicenseAccountLicenseData**](LicenseAccountLicenseData.md)| The &#39;license.AccountLicenseData&#39; resource to update. | 

### Return type

[**LicenseAccountLicenseData**](LicenseAccountLicenseData.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;license.AccountLicenseData&#39; resource was patched as requested. The &#39;license.AccountLicenseData&#39; resource is patched before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;license.AccountLicenseData&#39; resource is asynchronously being patched as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_license_customer_op**
> LicenseCustomerOp patch_license_customer_op(moid, license_customer_op)

Update a 'license.CustomerOp' resource.

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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
license_customer_op = intersight.LicenseCustomerOp() # LicenseCustomerOp | The 'license.CustomerOp' resource to update.

try:
    # Update a 'license.CustomerOp' resource.
    api_response = api_instance.patch_license_customer_op(moid, license_customer_op)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->patch_license_customer_op: %s\n" % e)
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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
license_customer_op = intersight.LicenseCustomerOp() # LicenseCustomerOp | The 'license.CustomerOp' resource to update.

try:
    # Update a 'license.CustomerOp' resource.
    api_response = api_instance.patch_license_customer_op(moid, license_customer_op)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->patch_license_customer_op: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **license_customer_op** | [**LicenseCustomerOp**](LicenseCustomerOp.md)| The &#39;license.CustomerOp&#39; resource to update. | 

### Return type

[**LicenseCustomerOp**](LicenseCustomerOp.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;license.CustomerOp&#39; resource was patched as requested. The &#39;license.CustomerOp&#39; resource is patched before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;license.CustomerOp&#39; resource is asynchronously being patched as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_license_license_info**
> LicenseLicenseInfo patch_license_license_info(moid, license_license_info)

Update a 'license.LicenseInfo' resource.

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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
license_license_info = intersight.LicenseLicenseInfo() # LicenseLicenseInfo | The 'license.LicenseInfo' resource to update.

try:
    # Update a 'license.LicenseInfo' resource.
    api_response = api_instance.patch_license_license_info(moid, license_license_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->patch_license_license_info: %s\n" % e)
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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
license_license_info = intersight.LicenseLicenseInfo() # LicenseLicenseInfo | The 'license.LicenseInfo' resource to update.

try:
    # Update a 'license.LicenseInfo' resource.
    api_response = api_instance.patch_license_license_info(moid, license_license_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->patch_license_license_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **license_license_info** | [**LicenseLicenseInfo**](LicenseLicenseInfo.md)| The &#39;license.LicenseInfo&#39; resource to update. | 

### Return type

[**LicenseLicenseInfo**](LicenseLicenseInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;license.LicenseInfo&#39; resource was patched as requested. The &#39;license.LicenseInfo&#39; resource is patched before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;license.LicenseInfo&#39; resource is asynchronously being patched as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_license_smartlicense_token**
> LicenseSmartlicenseToken patch_license_smartlicense_token(moid, license_smartlicense_token)

Update a 'license.SmartlicenseToken' resource.

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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
license_smartlicense_token = intersight.LicenseSmartlicenseToken() # LicenseSmartlicenseToken | The 'license.SmartlicenseToken' resource to update.

try:
    # Update a 'license.SmartlicenseToken' resource.
    api_response = api_instance.patch_license_smartlicense_token(moid, license_smartlicense_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->patch_license_smartlicense_token: %s\n" % e)
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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
license_smartlicense_token = intersight.LicenseSmartlicenseToken() # LicenseSmartlicenseToken | The 'license.SmartlicenseToken' resource to update.

try:
    # Update a 'license.SmartlicenseToken' resource.
    api_response = api_instance.patch_license_smartlicense_token(moid, license_smartlicense_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->patch_license_smartlicense_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **license_smartlicense_token** | [**LicenseSmartlicenseToken**](LicenseSmartlicenseToken.md)| The &#39;license.SmartlicenseToken&#39; resource to update. | 

### Return type

[**LicenseSmartlicenseToken**](LicenseSmartlicenseToken.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;license.SmartlicenseToken&#39; resource was patched as requested. The &#39;license.SmartlicenseToken&#39; resource is patched before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;license.SmartlicenseToken&#39; resource is asynchronously being patched as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_license_account_license_data**
> LicenseAccountLicenseData update_license_account_license_data(moid, license_account_license_data)

Update a 'license.AccountLicenseData' resource.

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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
license_account_license_data = intersight.LicenseAccountLicenseData() # LicenseAccountLicenseData | The 'license.AccountLicenseData' resource to update.

try:
    # Update a 'license.AccountLicenseData' resource.
    api_response = api_instance.update_license_account_license_data(moid, license_account_license_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->update_license_account_license_data: %s\n" % e)
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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
license_account_license_data = intersight.LicenseAccountLicenseData() # LicenseAccountLicenseData | The 'license.AccountLicenseData' resource to update.

try:
    # Update a 'license.AccountLicenseData' resource.
    api_response = api_instance.update_license_account_license_data(moid, license_account_license_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->update_license_account_license_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **license_account_license_data** | [**LicenseAccountLicenseData**](LicenseAccountLicenseData.md)| The &#39;license.AccountLicenseData&#39; resource to update. | 

### Return type

[**LicenseAccountLicenseData**](LicenseAccountLicenseData.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;license.AccountLicenseData&#39; resource was modified as requested. The &#39;license.AccountLicenseData&#39; resource is modified before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;license.AccountLicenseData&#39; resource is asynchronously being modified as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_license_customer_op**
> LicenseCustomerOp update_license_customer_op(moid, license_customer_op)

Update a 'license.CustomerOp' resource.

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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
license_customer_op = intersight.LicenseCustomerOp() # LicenseCustomerOp | The 'license.CustomerOp' resource to update.

try:
    # Update a 'license.CustomerOp' resource.
    api_response = api_instance.update_license_customer_op(moid, license_customer_op)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->update_license_customer_op: %s\n" % e)
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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
license_customer_op = intersight.LicenseCustomerOp() # LicenseCustomerOp | The 'license.CustomerOp' resource to update.

try:
    # Update a 'license.CustomerOp' resource.
    api_response = api_instance.update_license_customer_op(moid, license_customer_op)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->update_license_customer_op: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **license_customer_op** | [**LicenseCustomerOp**](LicenseCustomerOp.md)| The &#39;license.CustomerOp&#39; resource to update. | 

### Return type

[**LicenseCustomerOp**](LicenseCustomerOp.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;license.CustomerOp&#39; resource was modified as requested. The &#39;license.CustomerOp&#39; resource is modified before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;license.CustomerOp&#39; resource is asynchronously being modified as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_license_license_info**
> LicenseLicenseInfo update_license_license_info(moid, license_license_info)

Update a 'license.LicenseInfo' resource.

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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
license_license_info = intersight.LicenseLicenseInfo() # LicenseLicenseInfo | The 'license.LicenseInfo' resource to update.

try:
    # Update a 'license.LicenseInfo' resource.
    api_response = api_instance.update_license_license_info(moid, license_license_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->update_license_license_info: %s\n" % e)
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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
license_license_info = intersight.LicenseLicenseInfo() # LicenseLicenseInfo | The 'license.LicenseInfo' resource to update.

try:
    # Update a 'license.LicenseInfo' resource.
    api_response = api_instance.update_license_license_info(moid, license_license_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->update_license_license_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **license_license_info** | [**LicenseLicenseInfo**](LicenseLicenseInfo.md)| The &#39;license.LicenseInfo&#39; resource to update. | 

### Return type

[**LicenseLicenseInfo**](LicenseLicenseInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;license.LicenseInfo&#39; resource was modified as requested. The &#39;license.LicenseInfo&#39; resource is modified before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;license.LicenseInfo&#39; resource is asynchronously being modified as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_license_smartlicense_token**
> LicenseSmartlicenseToken update_license_smartlicense_token(moid, license_smartlicense_token)

Update a 'license.SmartlicenseToken' resource.

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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
license_smartlicense_token = intersight.LicenseSmartlicenseToken() # LicenseSmartlicenseToken | The 'license.SmartlicenseToken' resource to update.

try:
    # Update a 'license.SmartlicenseToken' resource.
    api_response = api_instance.update_license_smartlicense_token(moid, license_smartlicense_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->update_license_smartlicense_token: %s\n" % e)
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
api_instance = intersight.LicenseApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
license_smartlicense_token = intersight.LicenseSmartlicenseToken() # LicenseSmartlicenseToken | The 'license.SmartlicenseToken' resource to update.

try:
    # Update a 'license.SmartlicenseToken' resource.
    api_response = api_instance.update_license_smartlicense_token(moid, license_smartlicense_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->update_license_smartlicense_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **license_smartlicense_token** | [**LicenseSmartlicenseToken**](LicenseSmartlicenseToken.md)| The &#39;license.SmartlicenseToken&#39; resource to update. | 

### Return type

[**LicenseSmartlicenseToken**](LicenseSmartlicenseToken.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;license.SmartlicenseToken&#39; resource was modified as requested. The &#39;license.SmartlicenseToken&#39; resource is modified before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;license.SmartlicenseToken&#39; resource is asynchronously being modified as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

