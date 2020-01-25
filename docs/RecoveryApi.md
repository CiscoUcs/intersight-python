# intersight.RecoveryApi

All URIs are relative to *https://intersight.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_recovery_backup_config_policy**](RecoveryApi.md#create_recovery_backup_config_policy) | **POST** /recovery/BackupConfigPolicies | Create a &#39;recovery.BackupConfigPolicy&#39; resource.
[**create_recovery_backup_profile**](RecoveryApi.md#create_recovery_backup_profile) | **POST** /recovery/BackupProfiles | Create a &#39;recovery.BackupProfile&#39; resource.
[**create_recovery_on_demand_backup**](RecoveryApi.md#create_recovery_on_demand_backup) | **POST** /recovery/OnDemandBackups | Create a &#39;recovery.OnDemandBackup&#39; resource.
[**create_recovery_restore**](RecoveryApi.md#create_recovery_restore) | **POST** /recovery/Restores | Create a &#39;recovery.Restore&#39; resource.
[**create_recovery_schedule_config_policy**](RecoveryApi.md#create_recovery_schedule_config_policy) | **POST** /recovery/ScheduleConfigPolicies | Create a &#39;recovery.ScheduleConfigPolicy&#39; resource.
[**delete_recovery_backup_config_policy**](RecoveryApi.md#delete_recovery_backup_config_policy) | **DELETE** /recovery/BackupConfigPolicies/{Moid} | Delete a &#39;recovery.BackupConfigPolicy&#39; resource.
[**delete_recovery_backup_profile**](RecoveryApi.md#delete_recovery_backup_profile) | **DELETE** /recovery/BackupProfiles/{Moid} | Delete a &#39;recovery.BackupProfile&#39; resource.
[**delete_recovery_on_demand_backup**](RecoveryApi.md#delete_recovery_on_demand_backup) | **DELETE** /recovery/OnDemandBackups/{Moid} | Delete a &#39;recovery.OnDemandBackup&#39; resource.
[**delete_recovery_restore**](RecoveryApi.md#delete_recovery_restore) | **DELETE** /recovery/Restores/{Moid} | Delete a &#39;recovery.Restore&#39; resource.
[**delete_recovery_schedule_config_policy**](RecoveryApi.md#delete_recovery_schedule_config_policy) | **DELETE** /recovery/ScheduleConfigPolicies/{Moid} | Delete a &#39;recovery.ScheduleConfigPolicy&#39; resource.
[**get_recovery_backup_config_policy_by_moid**](RecoveryApi.md#get_recovery_backup_config_policy_by_moid) | **GET** /recovery/BackupConfigPolicies/{Moid} | Read a &#39;recovery.BackupConfigPolicy&#39; resource.
[**get_recovery_backup_config_policy_list**](RecoveryApi.md#get_recovery_backup_config_policy_list) | **GET** /recovery/BackupConfigPolicies | Read a &#39;recovery.BackupConfigPolicy&#39; resource.
[**get_recovery_backup_profile_by_moid**](RecoveryApi.md#get_recovery_backup_profile_by_moid) | **GET** /recovery/BackupProfiles/{Moid} | Read a &#39;recovery.BackupProfile&#39; resource.
[**get_recovery_backup_profile_list**](RecoveryApi.md#get_recovery_backup_profile_list) | **GET** /recovery/BackupProfiles | Read a &#39;recovery.BackupProfile&#39; resource.
[**get_recovery_config_result_by_moid**](RecoveryApi.md#get_recovery_config_result_by_moid) | **GET** /recovery/ConfigResults/{Moid} | Read a &#39;recovery.ConfigResult&#39; resource.
[**get_recovery_config_result_entry_by_moid**](RecoveryApi.md#get_recovery_config_result_entry_by_moid) | **GET** /recovery/ConfigResultEntries/{Moid} | Read a &#39;recovery.ConfigResultEntry&#39; resource.
[**get_recovery_config_result_entry_list**](RecoveryApi.md#get_recovery_config_result_entry_list) | **GET** /recovery/ConfigResultEntries | Read a &#39;recovery.ConfigResultEntry&#39; resource.
[**get_recovery_config_result_list**](RecoveryApi.md#get_recovery_config_result_list) | **GET** /recovery/ConfigResults | Read a &#39;recovery.ConfigResult&#39; resource.
[**get_recovery_on_demand_backup_by_moid**](RecoveryApi.md#get_recovery_on_demand_backup_by_moid) | **GET** /recovery/OnDemandBackups/{Moid} | Read a &#39;recovery.OnDemandBackup&#39; resource.
[**get_recovery_on_demand_backup_list**](RecoveryApi.md#get_recovery_on_demand_backup_list) | **GET** /recovery/OnDemandBackups | Read a &#39;recovery.OnDemandBackup&#39; resource.
[**get_recovery_restore_by_moid**](RecoveryApi.md#get_recovery_restore_by_moid) | **GET** /recovery/Restores/{Moid} | Read a &#39;recovery.Restore&#39; resource.
[**get_recovery_restore_list**](RecoveryApi.md#get_recovery_restore_list) | **GET** /recovery/Restores | Read a &#39;recovery.Restore&#39; resource.
[**get_recovery_schedule_config_policy_by_moid**](RecoveryApi.md#get_recovery_schedule_config_policy_by_moid) | **GET** /recovery/ScheduleConfigPolicies/{Moid} | Read a &#39;recovery.ScheduleConfigPolicy&#39; resource.
[**get_recovery_schedule_config_policy_list**](RecoveryApi.md#get_recovery_schedule_config_policy_list) | **GET** /recovery/ScheduleConfigPolicies | Read a &#39;recovery.ScheduleConfigPolicy&#39; resource.
[**patch_recovery_backup_config_policy**](RecoveryApi.md#patch_recovery_backup_config_policy) | **PATCH** /recovery/BackupConfigPolicies/{Moid} | Update a &#39;recovery.BackupConfigPolicy&#39; resource.
[**patch_recovery_backup_profile**](RecoveryApi.md#patch_recovery_backup_profile) | **PATCH** /recovery/BackupProfiles/{Moid} | Update a &#39;recovery.BackupProfile&#39; resource.
[**patch_recovery_on_demand_backup**](RecoveryApi.md#patch_recovery_on_demand_backup) | **PATCH** /recovery/OnDemandBackups/{Moid} | Update a &#39;recovery.OnDemandBackup&#39; resource.
[**patch_recovery_schedule_config_policy**](RecoveryApi.md#patch_recovery_schedule_config_policy) | **PATCH** /recovery/ScheduleConfigPolicies/{Moid} | Update a &#39;recovery.ScheduleConfigPolicy&#39; resource.
[**update_recovery_backup_config_policy**](RecoveryApi.md#update_recovery_backup_config_policy) | **POST** /recovery/BackupConfigPolicies/{Moid} | Update a &#39;recovery.BackupConfigPolicy&#39; resource.
[**update_recovery_backup_profile**](RecoveryApi.md#update_recovery_backup_profile) | **POST** /recovery/BackupProfiles/{Moid} | Update a &#39;recovery.BackupProfile&#39; resource.
[**update_recovery_on_demand_backup**](RecoveryApi.md#update_recovery_on_demand_backup) | **POST** /recovery/OnDemandBackups/{Moid} | Update a &#39;recovery.OnDemandBackup&#39; resource.
[**update_recovery_schedule_config_policy**](RecoveryApi.md#update_recovery_schedule_config_policy) | **POST** /recovery/ScheduleConfigPolicies/{Moid} | Update a &#39;recovery.ScheduleConfigPolicy&#39; resource.


# **create_recovery_backup_config_policy**
> RecoveryBackupConfigPolicy create_recovery_backup_config_policy(recovery_backup_config_policy)

Create a 'recovery.BackupConfigPolicy' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
recovery_backup_config_policy = intersight.RecoveryBackupConfigPolicy() # RecoveryBackupConfigPolicy | The 'recovery.BackupConfigPolicy' resource to create.

try:
    # Create a 'recovery.BackupConfigPolicy' resource.
    api_response = api_instance.create_recovery_backup_config_policy(recovery_backup_config_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->create_recovery_backup_config_policy: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
recovery_backup_config_policy = intersight.RecoveryBackupConfigPolicy() # RecoveryBackupConfigPolicy | The 'recovery.BackupConfigPolicy' resource to create.

try:
    # Create a 'recovery.BackupConfigPolicy' resource.
    api_response = api_instance.create_recovery_backup_config_policy(recovery_backup_config_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->create_recovery_backup_config_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recovery_backup_config_policy** | [**RecoveryBackupConfigPolicy**](RecoveryBackupConfigPolicy.md)| The &#39;recovery.BackupConfigPolicy&#39; resource to create. | 

### Return type

[**RecoveryBackupConfigPolicy**](RecoveryBackupConfigPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;recovery.BackupConfigPolicy&#39; resource was created as requested. The &#39;recovery.BackupConfigPolicy&#39; resource is created before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;recovery.BackupConfigPolicy&#39; resource is asynchronously being created as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_recovery_backup_profile**
> RecoveryBackupProfile create_recovery_backup_profile(recovery_backup_profile)

Create a 'recovery.BackupProfile' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
recovery_backup_profile = intersight.RecoveryBackupProfile() # RecoveryBackupProfile | The 'recovery.BackupProfile' resource to create.

try:
    # Create a 'recovery.BackupProfile' resource.
    api_response = api_instance.create_recovery_backup_profile(recovery_backup_profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->create_recovery_backup_profile: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
recovery_backup_profile = intersight.RecoveryBackupProfile() # RecoveryBackupProfile | The 'recovery.BackupProfile' resource to create.

try:
    # Create a 'recovery.BackupProfile' resource.
    api_response = api_instance.create_recovery_backup_profile(recovery_backup_profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->create_recovery_backup_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recovery_backup_profile** | [**RecoveryBackupProfile**](RecoveryBackupProfile.md)| The &#39;recovery.BackupProfile&#39; resource to create. | 

### Return type

[**RecoveryBackupProfile**](RecoveryBackupProfile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;recovery.BackupProfile&#39; resource was created as requested. The &#39;recovery.BackupProfile&#39; resource is created before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;recovery.BackupProfile&#39; resource is asynchronously being created as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_recovery_on_demand_backup**
> RecoveryOnDemandBackup create_recovery_on_demand_backup(recovery_on_demand_backup)

Create a 'recovery.OnDemandBackup' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
recovery_on_demand_backup = intersight.RecoveryOnDemandBackup() # RecoveryOnDemandBackup | The 'recovery.OnDemandBackup' resource to create.

try:
    # Create a 'recovery.OnDemandBackup' resource.
    api_response = api_instance.create_recovery_on_demand_backup(recovery_on_demand_backup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->create_recovery_on_demand_backup: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
recovery_on_demand_backup = intersight.RecoveryOnDemandBackup() # RecoveryOnDemandBackup | The 'recovery.OnDemandBackup' resource to create.

try:
    # Create a 'recovery.OnDemandBackup' resource.
    api_response = api_instance.create_recovery_on_demand_backup(recovery_on_demand_backup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->create_recovery_on_demand_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recovery_on_demand_backup** | [**RecoveryOnDemandBackup**](RecoveryOnDemandBackup.md)| The &#39;recovery.OnDemandBackup&#39; resource to create. | 

### Return type

[**RecoveryOnDemandBackup**](RecoveryOnDemandBackup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;recovery.OnDemandBackup&#39; resource was created as requested. The &#39;recovery.OnDemandBackup&#39; resource is created before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;recovery.OnDemandBackup&#39; resource is asynchronously being created as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_recovery_restore**
> RecoveryRestore create_recovery_restore(recovery_restore)

Create a 'recovery.Restore' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
recovery_restore = intersight.RecoveryRestore() # RecoveryRestore | The 'recovery.Restore' resource to create.

try:
    # Create a 'recovery.Restore' resource.
    api_response = api_instance.create_recovery_restore(recovery_restore)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->create_recovery_restore: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
recovery_restore = intersight.RecoveryRestore() # RecoveryRestore | The 'recovery.Restore' resource to create.

try:
    # Create a 'recovery.Restore' resource.
    api_response = api_instance.create_recovery_restore(recovery_restore)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->create_recovery_restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recovery_restore** | [**RecoveryRestore**](RecoveryRestore.md)| The &#39;recovery.Restore&#39; resource to create. | 

### Return type

[**RecoveryRestore**](RecoveryRestore.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;recovery.Restore&#39; resource was created as requested. The &#39;recovery.Restore&#39; resource is created before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;recovery.Restore&#39; resource is asynchronously being created as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_recovery_schedule_config_policy**
> RecoveryScheduleConfigPolicy create_recovery_schedule_config_policy(recovery_schedule_config_policy)

Create a 'recovery.ScheduleConfigPolicy' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
recovery_schedule_config_policy = intersight.RecoveryScheduleConfigPolicy() # RecoveryScheduleConfigPolicy | The 'recovery.ScheduleConfigPolicy' resource to create.

try:
    # Create a 'recovery.ScheduleConfigPolicy' resource.
    api_response = api_instance.create_recovery_schedule_config_policy(recovery_schedule_config_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->create_recovery_schedule_config_policy: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
recovery_schedule_config_policy = intersight.RecoveryScheduleConfigPolicy() # RecoveryScheduleConfigPolicy | The 'recovery.ScheduleConfigPolicy' resource to create.

try:
    # Create a 'recovery.ScheduleConfigPolicy' resource.
    api_response = api_instance.create_recovery_schedule_config_policy(recovery_schedule_config_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->create_recovery_schedule_config_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recovery_schedule_config_policy** | [**RecoveryScheduleConfigPolicy**](RecoveryScheduleConfigPolicy.md)| The &#39;recovery.ScheduleConfigPolicy&#39; resource to create. | 

### Return type

[**RecoveryScheduleConfigPolicy**](RecoveryScheduleConfigPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;recovery.ScheduleConfigPolicy&#39; resource was created as requested. The &#39;recovery.ScheduleConfigPolicy&#39; resource is created before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;recovery.ScheduleConfigPolicy&#39; resource is asynchronously being created as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recovery_backup_config_policy**
> delete_recovery_backup_config_policy(moid)

Delete a 'recovery.BackupConfigPolicy' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Delete a 'recovery.BackupConfigPolicy' resource.
    api_instance.delete_recovery_backup_config_policy(moid)
except ApiException as e:
    print("Exception when calling RecoveryApi->delete_recovery_backup_config_policy: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Delete a 'recovery.BackupConfigPolicy' resource.
    api_instance.delete_recovery_backup_config_policy(moid)
except ApiException as e:
    print("Exception when calling RecoveryApi->delete_recovery_backup_config_policy: %s\n" % e)
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

# **delete_recovery_backup_profile**
> delete_recovery_backup_profile(moid)

Delete a 'recovery.BackupProfile' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Delete a 'recovery.BackupProfile' resource.
    api_instance.delete_recovery_backup_profile(moid)
except ApiException as e:
    print("Exception when calling RecoveryApi->delete_recovery_backup_profile: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Delete a 'recovery.BackupProfile' resource.
    api_instance.delete_recovery_backup_profile(moid)
except ApiException as e:
    print("Exception when calling RecoveryApi->delete_recovery_backup_profile: %s\n" % e)
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

# **delete_recovery_on_demand_backup**
> delete_recovery_on_demand_backup(moid)

Delete a 'recovery.OnDemandBackup' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Delete a 'recovery.OnDemandBackup' resource.
    api_instance.delete_recovery_on_demand_backup(moid)
except ApiException as e:
    print("Exception when calling RecoveryApi->delete_recovery_on_demand_backup: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Delete a 'recovery.OnDemandBackup' resource.
    api_instance.delete_recovery_on_demand_backup(moid)
except ApiException as e:
    print("Exception when calling RecoveryApi->delete_recovery_on_demand_backup: %s\n" % e)
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

# **delete_recovery_restore**
> delete_recovery_restore(moid)

Delete a 'recovery.Restore' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Delete a 'recovery.Restore' resource.
    api_instance.delete_recovery_restore(moid)
except ApiException as e:
    print("Exception when calling RecoveryApi->delete_recovery_restore: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Delete a 'recovery.Restore' resource.
    api_instance.delete_recovery_restore(moid)
except ApiException as e:
    print("Exception when calling RecoveryApi->delete_recovery_restore: %s\n" % e)
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

# **delete_recovery_schedule_config_policy**
> delete_recovery_schedule_config_policy(moid)

Delete a 'recovery.ScheduleConfigPolicy' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Delete a 'recovery.ScheduleConfigPolicy' resource.
    api_instance.delete_recovery_schedule_config_policy(moid)
except ApiException as e:
    print("Exception when calling RecoveryApi->delete_recovery_schedule_config_policy: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Delete a 'recovery.ScheduleConfigPolicy' resource.
    api_instance.delete_recovery_schedule_config_policy(moid)
except ApiException as e:
    print("Exception when calling RecoveryApi->delete_recovery_schedule_config_policy: %s\n" % e)
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

# **get_recovery_backup_config_policy_by_moid**
> RecoveryBackupConfigPolicy get_recovery_backup_config_policy_by_moid(moid)

Read a 'recovery.BackupConfigPolicy' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'recovery.BackupConfigPolicy' resource.
    api_response = api_instance.get_recovery_backup_config_policy_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_backup_config_policy_by_moid: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'recovery.BackupConfigPolicy' resource.
    api_response = api_instance.get_recovery_backup_config_policy_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_backup_config_policy_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**RecoveryBackupConfigPolicy**](RecoveryBackupConfigPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;recovery.BackupConfigPolicy&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recovery_backup_config_policy_list**
> RecoveryBackupConfigPolicyList get_recovery_backup_config_policy_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'recovery.BackupConfigPolicy' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
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
    # Read a 'recovery.BackupConfigPolicy' resource.
    api_response = api_instance.get_recovery_backup_config_policy_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_backup_config_policy_list: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
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
    # Read a 'recovery.BackupConfigPolicy' resource.
    api_response = api_instance.get_recovery_backup_config_policy_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_backup_config_policy_list: %s\n" % e)
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

[**RecoveryBackupConfigPolicyList**](RecoveryBackupConfigPolicyList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;recovery.BackupConfigPolicy&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recovery_backup_profile_by_moid**
> RecoveryBackupProfile get_recovery_backup_profile_by_moid(moid)

Read a 'recovery.BackupProfile' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'recovery.BackupProfile' resource.
    api_response = api_instance.get_recovery_backup_profile_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_backup_profile_by_moid: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'recovery.BackupProfile' resource.
    api_response = api_instance.get_recovery_backup_profile_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_backup_profile_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**RecoveryBackupProfile**](RecoveryBackupProfile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;recovery.BackupProfile&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recovery_backup_profile_list**
> RecoveryBackupProfileList get_recovery_backup_profile_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'recovery.BackupProfile' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
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
    # Read a 'recovery.BackupProfile' resource.
    api_response = api_instance.get_recovery_backup_profile_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_backup_profile_list: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
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
    # Read a 'recovery.BackupProfile' resource.
    api_response = api_instance.get_recovery_backup_profile_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_backup_profile_list: %s\n" % e)
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

[**RecoveryBackupProfileList**](RecoveryBackupProfileList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;recovery.BackupProfile&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recovery_config_result_by_moid**
> RecoveryConfigResult get_recovery_config_result_by_moid(moid)

Read a 'recovery.ConfigResult' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'recovery.ConfigResult' resource.
    api_response = api_instance.get_recovery_config_result_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_config_result_by_moid: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'recovery.ConfigResult' resource.
    api_response = api_instance.get_recovery_config_result_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_config_result_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**RecoveryConfigResult**](RecoveryConfigResult.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;recovery.ConfigResult&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recovery_config_result_entry_by_moid**
> RecoveryConfigResultEntry get_recovery_config_result_entry_by_moid(moid)

Read a 'recovery.ConfigResultEntry' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'recovery.ConfigResultEntry' resource.
    api_response = api_instance.get_recovery_config_result_entry_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_config_result_entry_by_moid: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'recovery.ConfigResultEntry' resource.
    api_response = api_instance.get_recovery_config_result_entry_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_config_result_entry_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**RecoveryConfigResultEntry**](RecoveryConfigResultEntry.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;recovery.ConfigResultEntry&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recovery_config_result_entry_list**
> RecoveryConfigResultEntryList get_recovery_config_result_entry_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'recovery.ConfigResultEntry' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
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
    # Read a 'recovery.ConfigResultEntry' resource.
    api_response = api_instance.get_recovery_config_result_entry_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_config_result_entry_list: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
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
    # Read a 'recovery.ConfigResultEntry' resource.
    api_response = api_instance.get_recovery_config_result_entry_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_config_result_entry_list: %s\n" % e)
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

[**RecoveryConfigResultEntryList**](RecoveryConfigResultEntryList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;recovery.ConfigResultEntry&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recovery_config_result_list**
> RecoveryConfigResultList get_recovery_config_result_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'recovery.ConfigResult' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
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
    # Read a 'recovery.ConfigResult' resource.
    api_response = api_instance.get_recovery_config_result_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_config_result_list: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
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
    # Read a 'recovery.ConfigResult' resource.
    api_response = api_instance.get_recovery_config_result_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_config_result_list: %s\n" % e)
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

[**RecoveryConfigResultList**](RecoveryConfigResultList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;recovery.ConfigResult&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recovery_on_demand_backup_by_moid**
> RecoveryOnDemandBackup get_recovery_on_demand_backup_by_moid(moid)

Read a 'recovery.OnDemandBackup' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'recovery.OnDemandBackup' resource.
    api_response = api_instance.get_recovery_on_demand_backup_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_on_demand_backup_by_moid: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'recovery.OnDemandBackup' resource.
    api_response = api_instance.get_recovery_on_demand_backup_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_on_demand_backup_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**RecoveryOnDemandBackup**](RecoveryOnDemandBackup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;recovery.OnDemandBackup&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recovery_on_demand_backup_list**
> RecoveryOnDemandBackupList get_recovery_on_demand_backup_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'recovery.OnDemandBackup' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
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
    # Read a 'recovery.OnDemandBackup' resource.
    api_response = api_instance.get_recovery_on_demand_backup_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_on_demand_backup_list: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
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
    # Read a 'recovery.OnDemandBackup' resource.
    api_response = api_instance.get_recovery_on_demand_backup_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_on_demand_backup_list: %s\n" % e)
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

[**RecoveryOnDemandBackupList**](RecoveryOnDemandBackupList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;recovery.OnDemandBackup&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recovery_restore_by_moid**
> RecoveryRestore get_recovery_restore_by_moid(moid)

Read a 'recovery.Restore' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'recovery.Restore' resource.
    api_response = api_instance.get_recovery_restore_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_restore_by_moid: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'recovery.Restore' resource.
    api_response = api_instance.get_recovery_restore_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_restore_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**RecoveryRestore**](RecoveryRestore.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;recovery.Restore&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recovery_restore_list**
> RecoveryRestoreList get_recovery_restore_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'recovery.Restore' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
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
    # Read a 'recovery.Restore' resource.
    api_response = api_instance.get_recovery_restore_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_restore_list: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
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
    # Read a 'recovery.Restore' resource.
    api_response = api_instance.get_recovery_restore_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_restore_list: %s\n" % e)
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

[**RecoveryRestoreList**](RecoveryRestoreList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;recovery.Restore&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recovery_schedule_config_policy_by_moid**
> RecoveryScheduleConfigPolicy get_recovery_schedule_config_policy_by_moid(moid)

Read a 'recovery.ScheduleConfigPolicy' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'recovery.ScheduleConfigPolicy' resource.
    api_response = api_instance.get_recovery_schedule_config_policy_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_schedule_config_policy_by_moid: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'recovery.ScheduleConfigPolicy' resource.
    api_response = api_instance.get_recovery_schedule_config_policy_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_schedule_config_policy_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**RecoveryScheduleConfigPolicy**](RecoveryScheduleConfigPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;recovery.ScheduleConfigPolicy&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recovery_schedule_config_policy_list**
> RecoveryScheduleConfigPolicyList get_recovery_schedule_config_policy_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'recovery.ScheduleConfigPolicy' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
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
    # Read a 'recovery.ScheduleConfigPolicy' resource.
    api_response = api_instance.get_recovery_schedule_config_policy_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_schedule_config_policy_list: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
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
    # Read a 'recovery.ScheduleConfigPolicy' resource.
    api_response = api_instance.get_recovery_schedule_config_policy_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->get_recovery_schedule_config_policy_list: %s\n" % e)
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

[**RecoveryScheduleConfigPolicyList**](RecoveryScheduleConfigPolicyList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;recovery.ScheduleConfigPolicy&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_recovery_backup_config_policy**
> RecoveryBackupConfigPolicy patch_recovery_backup_config_policy(moid, recovery_backup_config_policy)

Update a 'recovery.BackupConfigPolicy' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
recovery_backup_config_policy = intersight.RecoveryBackupConfigPolicy() # RecoveryBackupConfigPolicy | The 'recovery.BackupConfigPolicy' resource to update.

try:
    # Update a 'recovery.BackupConfigPolicy' resource.
    api_response = api_instance.patch_recovery_backup_config_policy(moid, recovery_backup_config_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->patch_recovery_backup_config_policy: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
recovery_backup_config_policy = intersight.RecoveryBackupConfigPolicy() # RecoveryBackupConfigPolicy | The 'recovery.BackupConfigPolicy' resource to update.

try:
    # Update a 'recovery.BackupConfigPolicy' resource.
    api_response = api_instance.patch_recovery_backup_config_policy(moid, recovery_backup_config_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->patch_recovery_backup_config_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **recovery_backup_config_policy** | [**RecoveryBackupConfigPolicy**](RecoveryBackupConfigPolicy.md)| The &#39;recovery.BackupConfigPolicy&#39; resource to update. | 

### Return type

[**RecoveryBackupConfigPolicy**](RecoveryBackupConfigPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;recovery.BackupConfigPolicy&#39; resource was patched as requested. The &#39;recovery.BackupConfigPolicy&#39; resource is patched before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;recovery.BackupConfigPolicy&#39; resource is asynchronously being patched as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_recovery_backup_profile**
> RecoveryBackupProfile patch_recovery_backup_profile(moid, recovery_backup_profile)

Update a 'recovery.BackupProfile' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
recovery_backup_profile = intersight.RecoveryBackupProfile() # RecoveryBackupProfile | The 'recovery.BackupProfile' resource to update.

try:
    # Update a 'recovery.BackupProfile' resource.
    api_response = api_instance.patch_recovery_backup_profile(moid, recovery_backup_profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->patch_recovery_backup_profile: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
recovery_backup_profile = intersight.RecoveryBackupProfile() # RecoveryBackupProfile | The 'recovery.BackupProfile' resource to update.

try:
    # Update a 'recovery.BackupProfile' resource.
    api_response = api_instance.patch_recovery_backup_profile(moid, recovery_backup_profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->patch_recovery_backup_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **recovery_backup_profile** | [**RecoveryBackupProfile**](RecoveryBackupProfile.md)| The &#39;recovery.BackupProfile&#39; resource to update. | 

### Return type

[**RecoveryBackupProfile**](RecoveryBackupProfile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;recovery.BackupProfile&#39; resource was patched as requested. The &#39;recovery.BackupProfile&#39; resource is patched before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;recovery.BackupProfile&#39; resource is asynchronously being patched as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_recovery_on_demand_backup**
> RecoveryOnDemandBackup patch_recovery_on_demand_backup(moid, recovery_on_demand_backup)

Update a 'recovery.OnDemandBackup' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
recovery_on_demand_backup = intersight.RecoveryOnDemandBackup() # RecoveryOnDemandBackup | The 'recovery.OnDemandBackup' resource to update.

try:
    # Update a 'recovery.OnDemandBackup' resource.
    api_response = api_instance.patch_recovery_on_demand_backup(moid, recovery_on_demand_backup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->patch_recovery_on_demand_backup: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
recovery_on_demand_backup = intersight.RecoveryOnDemandBackup() # RecoveryOnDemandBackup | The 'recovery.OnDemandBackup' resource to update.

try:
    # Update a 'recovery.OnDemandBackup' resource.
    api_response = api_instance.patch_recovery_on_demand_backup(moid, recovery_on_demand_backup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->patch_recovery_on_demand_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **recovery_on_demand_backup** | [**RecoveryOnDemandBackup**](RecoveryOnDemandBackup.md)| The &#39;recovery.OnDemandBackup&#39; resource to update. | 

### Return type

[**RecoveryOnDemandBackup**](RecoveryOnDemandBackup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;recovery.OnDemandBackup&#39; resource was patched as requested. The &#39;recovery.OnDemandBackup&#39; resource is patched before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;recovery.OnDemandBackup&#39; resource is asynchronously being patched as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_recovery_schedule_config_policy**
> RecoveryScheduleConfigPolicy patch_recovery_schedule_config_policy(moid, recovery_schedule_config_policy)

Update a 'recovery.ScheduleConfigPolicy' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
recovery_schedule_config_policy = intersight.RecoveryScheduleConfigPolicy() # RecoveryScheduleConfigPolicy | The 'recovery.ScheduleConfigPolicy' resource to update.

try:
    # Update a 'recovery.ScheduleConfigPolicy' resource.
    api_response = api_instance.patch_recovery_schedule_config_policy(moid, recovery_schedule_config_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->patch_recovery_schedule_config_policy: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
recovery_schedule_config_policy = intersight.RecoveryScheduleConfigPolicy() # RecoveryScheduleConfigPolicy | The 'recovery.ScheduleConfigPolicy' resource to update.

try:
    # Update a 'recovery.ScheduleConfigPolicy' resource.
    api_response = api_instance.patch_recovery_schedule_config_policy(moid, recovery_schedule_config_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->patch_recovery_schedule_config_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **recovery_schedule_config_policy** | [**RecoveryScheduleConfigPolicy**](RecoveryScheduleConfigPolicy.md)| The &#39;recovery.ScheduleConfigPolicy&#39; resource to update. | 

### Return type

[**RecoveryScheduleConfigPolicy**](RecoveryScheduleConfigPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;recovery.ScheduleConfigPolicy&#39; resource was patched as requested. The &#39;recovery.ScheduleConfigPolicy&#39; resource is patched before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;recovery.ScheduleConfigPolicy&#39; resource is asynchronously being patched as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recovery_backup_config_policy**
> RecoveryBackupConfigPolicy update_recovery_backup_config_policy(moid, recovery_backup_config_policy)

Update a 'recovery.BackupConfigPolicy' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
recovery_backup_config_policy = intersight.RecoveryBackupConfigPolicy() # RecoveryBackupConfigPolicy | The 'recovery.BackupConfigPolicy' resource to update.

try:
    # Update a 'recovery.BackupConfigPolicy' resource.
    api_response = api_instance.update_recovery_backup_config_policy(moid, recovery_backup_config_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->update_recovery_backup_config_policy: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
recovery_backup_config_policy = intersight.RecoveryBackupConfigPolicy() # RecoveryBackupConfigPolicy | The 'recovery.BackupConfigPolicy' resource to update.

try:
    # Update a 'recovery.BackupConfigPolicy' resource.
    api_response = api_instance.update_recovery_backup_config_policy(moid, recovery_backup_config_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->update_recovery_backup_config_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **recovery_backup_config_policy** | [**RecoveryBackupConfigPolicy**](RecoveryBackupConfigPolicy.md)| The &#39;recovery.BackupConfigPolicy&#39; resource to update. | 

### Return type

[**RecoveryBackupConfigPolicy**](RecoveryBackupConfigPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;recovery.BackupConfigPolicy&#39; resource was modified as requested. The &#39;recovery.BackupConfigPolicy&#39; resource is modified before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;recovery.BackupConfigPolicy&#39; resource is asynchronously being modified as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recovery_backup_profile**
> RecoveryBackupProfile update_recovery_backup_profile(moid, recovery_backup_profile)

Update a 'recovery.BackupProfile' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
recovery_backup_profile = intersight.RecoveryBackupProfile() # RecoveryBackupProfile | The 'recovery.BackupProfile' resource to update.

try:
    # Update a 'recovery.BackupProfile' resource.
    api_response = api_instance.update_recovery_backup_profile(moid, recovery_backup_profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->update_recovery_backup_profile: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
recovery_backup_profile = intersight.RecoveryBackupProfile() # RecoveryBackupProfile | The 'recovery.BackupProfile' resource to update.

try:
    # Update a 'recovery.BackupProfile' resource.
    api_response = api_instance.update_recovery_backup_profile(moid, recovery_backup_profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->update_recovery_backup_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **recovery_backup_profile** | [**RecoveryBackupProfile**](RecoveryBackupProfile.md)| The &#39;recovery.BackupProfile&#39; resource to update. | 

### Return type

[**RecoveryBackupProfile**](RecoveryBackupProfile.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;recovery.BackupProfile&#39; resource was modified as requested. The &#39;recovery.BackupProfile&#39; resource is modified before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;recovery.BackupProfile&#39; resource is asynchronously being modified as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recovery_on_demand_backup**
> RecoveryOnDemandBackup update_recovery_on_demand_backup(moid, recovery_on_demand_backup)

Update a 'recovery.OnDemandBackup' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
recovery_on_demand_backup = intersight.RecoveryOnDemandBackup() # RecoveryOnDemandBackup | The 'recovery.OnDemandBackup' resource to update.

try:
    # Update a 'recovery.OnDemandBackup' resource.
    api_response = api_instance.update_recovery_on_demand_backup(moid, recovery_on_demand_backup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->update_recovery_on_demand_backup: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
recovery_on_demand_backup = intersight.RecoveryOnDemandBackup() # RecoveryOnDemandBackup | The 'recovery.OnDemandBackup' resource to update.

try:
    # Update a 'recovery.OnDemandBackup' resource.
    api_response = api_instance.update_recovery_on_demand_backup(moid, recovery_on_demand_backup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->update_recovery_on_demand_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **recovery_on_demand_backup** | [**RecoveryOnDemandBackup**](RecoveryOnDemandBackup.md)| The &#39;recovery.OnDemandBackup&#39; resource to update. | 

### Return type

[**RecoveryOnDemandBackup**](RecoveryOnDemandBackup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;recovery.OnDemandBackup&#39; resource was modified as requested. The &#39;recovery.OnDemandBackup&#39; resource is modified before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;recovery.OnDemandBackup&#39; resource is asynchronously being modified as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recovery_schedule_config_policy**
> RecoveryScheduleConfigPolicy update_recovery_schedule_config_policy(moid, recovery_schedule_config_policy)

Update a 'recovery.ScheduleConfigPolicy' resource.

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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
recovery_schedule_config_policy = intersight.RecoveryScheduleConfigPolicy() # RecoveryScheduleConfigPolicy | The 'recovery.ScheduleConfigPolicy' resource to update.

try:
    # Update a 'recovery.ScheduleConfigPolicy' resource.
    api_response = api_instance.update_recovery_schedule_config_policy(moid, recovery_schedule_config_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->update_recovery_schedule_config_policy: %s\n" % e)
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
api_instance = intersight.RecoveryApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
recovery_schedule_config_policy = intersight.RecoveryScheduleConfigPolicy() # RecoveryScheduleConfigPolicy | The 'recovery.ScheduleConfigPolicy' resource to update.

try:
    # Update a 'recovery.ScheduleConfigPolicy' resource.
    api_response = api_instance.update_recovery_schedule_config_policy(moid, recovery_schedule_config_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryApi->update_recovery_schedule_config_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **recovery_schedule_config_policy** | [**RecoveryScheduleConfigPolicy**](RecoveryScheduleConfigPolicy.md)| The &#39;recovery.ScheduleConfigPolicy&#39; resource to update. | 

### Return type

[**RecoveryScheduleConfigPolicy**](RecoveryScheduleConfigPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;recovery.ScheduleConfigPolicy&#39; resource was modified as requested. The &#39;recovery.ScheduleConfigPolicy&#39; resource is modified before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;recovery.ScheduleConfigPolicy&#39; resource is asynchronously being modified as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

