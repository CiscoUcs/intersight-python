# intersight.ApplianceApi

All URIs are relative to *https://intersight.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_appliance_backup**](ApplianceApi.md#create_appliance_backup) | **POST** /appliance/Backups | Create a &#39;appliance.Backup&#39; resource.
[**create_appliance_backup_policy**](ApplianceApi.md#create_appliance_backup_policy) | **POST** /appliance/BackupPolicies | Create a &#39;appliance.BackupPolicy&#39; resource.
[**create_appliance_data_export_policy**](ApplianceApi.md#create_appliance_data_export_policy) | **POST** /appliance/DataExportPolicies | Create a &#39;appliance.DataExportPolicy&#39; resource.
[**create_appliance_device_claim**](ApplianceApi.md#create_appliance_device_claim) | **POST** /appliance/DeviceClaims | Create a &#39;appliance.DeviceClaim&#39; resource.
[**create_appliance_diag_setting**](ApplianceApi.md#create_appliance_diag_setting) | **POST** /appliance/DiagSettings | Create a &#39;appliance.DiagSetting&#39; resource.
[**create_appliance_restore**](ApplianceApi.md#create_appliance_restore) | **POST** /appliance/Restores | Create a &#39;appliance.Restore&#39; resource.
[**delete_appliance_backup**](ApplianceApi.md#delete_appliance_backup) | **DELETE** /appliance/Backups/{Moid} | Delete a &#39;appliance.Backup&#39; resource.
[**delete_appliance_restore**](ApplianceApi.md#delete_appliance_restore) | **DELETE** /appliance/Restores/{Moid} | Delete a &#39;appliance.Restore&#39; resource.
[**get_appliance_backup_by_moid**](ApplianceApi.md#get_appliance_backup_by_moid) | **GET** /appliance/Backups/{Moid} | Read a &#39;appliance.Backup&#39; resource.
[**get_appliance_backup_list**](ApplianceApi.md#get_appliance_backup_list) | **GET** /appliance/Backups | Read a &#39;appliance.Backup&#39; resource.
[**get_appliance_backup_policy_by_moid**](ApplianceApi.md#get_appliance_backup_policy_by_moid) | **GET** /appliance/BackupPolicies/{Moid} | Read a &#39;appliance.BackupPolicy&#39; resource.
[**get_appliance_backup_policy_list**](ApplianceApi.md#get_appliance_backup_policy_list) | **GET** /appliance/BackupPolicies | Read a &#39;appliance.BackupPolicy&#39; resource.
[**get_appliance_certificate_setting_by_moid**](ApplianceApi.md#get_appliance_certificate_setting_by_moid) | **GET** /appliance/CertificateSettings/{Moid} | Read a &#39;appliance.CertificateSetting&#39; resource.
[**get_appliance_certificate_setting_list**](ApplianceApi.md#get_appliance_certificate_setting_list) | **GET** /appliance/CertificateSettings | Read a &#39;appliance.CertificateSetting&#39; resource.
[**get_appliance_data_export_policy_by_moid**](ApplianceApi.md#get_appliance_data_export_policy_by_moid) | **GET** /appliance/DataExportPolicies/{Moid} | Read a &#39;appliance.DataExportPolicy&#39; resource.
[**get_appliance_data_export_policy_list**](ApplianceApi.md#get_appliance_data_export_policy_list) | **GET** /appliance/DataExportPolicies | Read a &#39;appliance.DataExportPolicy&#39; resource.
[**get_appliance_device_claim_by_moid**](ApplianceApi.md#get_appliance_device_claim_by_moid) | **GET** /appliance/DeviceClaims/{Moid} | Read a &#39;appliance.DeviceClaim&#39; resource.
[**get_appliance_device_claim_list**](ApplianceApi.md#get_appliance_device_claim_list) | **GET** /appliance/DeviceClaims | Read a &#39;appliance.DeviceClaim&#39; resource.
[**get_appliance_diag_setting_by_moid**](ApplianceApi.md#get_appliance_diag_setting_by_moid) | **GET** /appliance/DiagSettings/{Moid} | Read a &#39;appliance.DiagSetting&#39; resource.
[**get_appliance_diag_setting_list**](ApplianceApi.md#get_appliance_diag_setting_list) | **GET** /appliance/DiagSettings | Read a &#39;appliance.DiagSetting&#39; resource.
[**get_appliance_image_bundle_by_moid**](ApplianceApi.md#get_appliance_image_bundle_by_moid) | **GET** /appliance/ImageBundles/{Moid} | Read a &#39;appliance.ImageBundle&#39; resource.
[**get_appliance_image_bundle_list**](ApplianceApi.md#get_appliance_image_bundle_list) | **GET** /appliance/ImageBundles | Read a &#39;appliance.ImageBundle&#39; resource.
[**get_appliance_node_info_by_moid**](ApplianceApi.md#get_appliance_node_info_by_moid) | **GET** /appliance/NodeInfos/{Moid} | Read a &#39;appliance.NodeInfo&#39; resource.
[**get_appliance_node_info_list**](ApplianceApi.md#get_appliance_node_info_list) | **GET** /appliance/NodeInfos | Read a &#39;appliance.NodeInfo&#39; resource.
[**get_appliance_restore_by_moid**](ApplianceApi.md#get_appliance_restore_by_moid) | **GET** /appliance/Restores/{Moid} | Read a &#39;appliance.Restore&#39; resource.
[**get_appliance_restore_list**](ApplianceApi.md#get_appliance_restore_list) | **GET** /appliance/Restores | Read a &#39;appliance.Restore&#39; resource.
[**get_appliance_setup_info_by_moid**](ApplianceApi.md#get_appliance_setup_info_by_moid) | **GET** /appliance/SetupInfos/{Moid} | Read a &#39;appliance.SetupInfo&#39; resource.
[**get_appliance_setup_info_list**](ApplianceApi.md#get_appliance_setup_info_list) | **GET** /appliance/SetupInfos | Read a &#39;appliance.SetupInfo&#39; resource.
[**get_appliance_system_info_by_moid**](ApplianceApi.md#get_appliance_system_info_by_moid) | **GET** /appliance/SystemInfos/{Moid} | Read a &#39;appliance.SystemInfo&#39; resource.
[**get_appliance_system_info_list**](ApplianceApi.md#get_appliance_system_info_list) | **GET** /appliance/SystemInfos | Read a &#39;appliance.SystemInfo&#39; resource.
[**get_appliance_upgrade_by_moid**](ApplianceApi.md#get_appliance_upgrade_by_moid) | **GET** /appliance/Upgrades/{Moid} | Read a &#39;appliance.Upgrade&#39; resource.
[**get_appliance_upgrade_list**](ApplianceApi.md#get_appliance_upgrade_list) | **GET** /appliance/Upgrades | Read a &#39;appliance.Upgrade&#39; resource.
[**get_appliance_upgrade_policy_by_moid**](ApplianceApi.md#get_appliance_upgrade_policy_by_moid) | **GET** /appliance/UpgradePolicies/{Moid} | Read a &#39;appliance.UpgradePolicy&#39; resource.
[**get_appliance_upgrade_policy_list**](ApplianceApi.md#get_appliance_upgrade_policy_list) | **GET** /appliance/UpgradePolicies | Read a &#39;appliance.UpgradePolicy&#39; resource.
[**patch_appliance_backup_policy**](ApplianceApi.md#patch_appliance_backup_policy) | **PATCH** /appliance/BackupPolicies/{Moid} | Update a &#39;appliance.BackupPolicy&#39; resource.
[**patch_appliance_certificate_setting**](ApplianceApi.md#patch_appliance_certificate_setting) | **PATCH** /appliance/CertificateSettings/{Moid} | Update a &#39;appliance.CertificateSetting&#39; resource.
[**patch_appliance_data_export_policy**](ApplianceApi.md#patch_appliance_data_export_policy) | **PATCH** /appliance/DataExportPolicies/{Moid} | Update a &#39;appliance.DataExportPolicy&#39; resource.
[**patch_appliance_diag_setting**](ApplianceApi.md#patch_appliance_diag_setting) | **PATCH** /appliance/DiagSettings/{Moid} | Update a &#39;appliance.DiagSetting&#39; resource.
[**patch_appliance_setup_info**](ApplianceApi.md#patch_appliance_setup_info) | **PATCH** /appliance/SetupInfos/{Moid} | Update a &#39;appliance.SetupInfo&#39; resource.
[**patch_appliance_upgrade**](ApplianceApi.md#patch_appliance_upgrade) | **PATCH** /appliance/Upgrades/{Moid} | Update a &#39;appliance.Upgrade&#39; resource.
[**patch_appliance_upgrade_policy**](ApplianceApi.md#patch_appliance_upgrade_policy) | **PATCH** /appliance/UpgradePolicies/{Moid} | Update a &#39;appliance.UpgradePolicy&#39; resource.
[**update_appliance_backup_policy**](ApplianceApi.md#update_appliance_backup_policy) | **POST** /appliance/BackupPolicies/{Moid} | Update a &#39;appliance.BackupPolicy&#39; resource.
[**update_appliance_certificate_setting**](ApplianceApi.md#update_appliance_certificate_setting) | **POST** /appliance/CertificateSettings/{Moid} | Update a &#39;appliance.CertificateSetting&#39; resource.
[**update_appliance_data_export_policy**](ApplianceApi.md#update_appliance_data_export_policy) | **POST** /appliance/DataExportPolicies/{Moid} | Update a &#39;appliance.DataExportPolicy&#39; resource.
[**update_appliance_diag_setting**](ApplianceApi.md#update_appliance_diag_setting) | **POST** /appliance/DiagSettings/{Moid} | Update a &#39;appliance.DiagSetting&#39; resource.
[**update_appliance_setup_info**](ApplianceApi.md#update_appliance_setup_info) | **POST** /appliance/SetupInfos/{Moid} | Update a &#39;appliance.SetupInfo&#39; resource.
[**update_appliance_upgrade**](ApplianceApi.md#update_appliance_upgrade) | **POST** /appliance/Upgrades/{Moid} | Update a &#39;appliance.Upgrade&#39; resource.
[**update_appliance_upgrade_policy**](ApplianceApi.md#update_appliance_upgrade_policy) | **POST** /appliance/UpgradePolicies/{Moid} | Update a &#39;appliance.UpgradePolicy&#39; resource.


# **create_appliance_backup**
> ApplianceBackup create_appliance_backup(appliance_backup)

Create a 'appliance.Backup' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
appliance_backup = intersight.ApplianceBackup() # ApplianceBackup | The 'appliance.Backup' resource to create.

try:
    # Create a 'appliance.Backup' resource.
    api_response = api_instance.create_appliance_backup(appliance_backup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->create_appliance_backup: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
appliance_backup = intersight.ApplianceBackup() # ApplianceBackup | The 'appliance.Backup' resource to create.

try:
    # Create a 'appliance.Backup' resource.
    api_response = api_instance.create_appliance_backup(appliance_backup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->create_appliance_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_backup** | [**ApplianceBackup**](ApplianceBackup.md)| The &#39;appliance.Backup&#39; resource to create. | 

### Return type

[**ApplianceBackup**](ApplianceBackup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.Backup&#39; resource was created as requested. The &#39;appliance.Backup&#39; resource is created before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.Backup&#39; resource is asynchronously being created as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_appliance_backup_policy**
> ApplianceBackupPolicy create_appliance_backup_policy(appliance_backup_policy)

Create a 'appliance.BackupPolicy' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
appliance_backup_policy = intersight.ApplianceBackupPolicy() # ApplianceBackupPolicy | The 'appliance.BackupPolicy' resource to create.

try:
    # Create a 'appliance.BackupPolicy' resource.
    api_response = api_instance.create_appliance_backup_policy(appliance_backup_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->create_appliance_backup_policy: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
appliance_backup_policy = intersight.ApplianceBackupPolicy() # ApplianceBackupPolicy | The 'appliance.BackupPolicy' resource to create.

try:
    # Create a 'appliance.BackupPolicy' resource.
    api_response = api_instance.create_appliance_backup_policy(appliance_backup_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->create_appliance_backup_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_backup_policy** | [**ApplianceBackupPolicy**](ApplianceBackupPolicy.md)| The &#39;appliance.BackupPolicy&#39; resource to create. | 

### Return type

[**ApplianceBackupPolicy**](ApplianceBackupPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.BackupPolicy&#39; resource was created as requested. The &#39;appliance.BackupPolicy&#39; resource is created before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.BackupPolicy&#39; resource is asynchronously being created as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_appliance_data_export_policy**
> ApplianceDataExportPolicy create_appliance_data_export_policy(appliance_data_export_policy)

Create a 'appliance.DataExportPolicy' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
appliance_data_export_policy = intersight.ApplianceDataExportPolicy() # ApplianceDataExportPolicy | The 'appliance.DataExportPolicy' resource to create.

try:
    # Create a 'appliance.DataExportPolicy' resource.
    api_response = api_instance.create_appliance_data_export_policy(appliance_data_export_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->create_appliance_data_export_policy: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
appliance_data_export_policy = intersight.ApplianceDataExportPolicy() # ApplianceDataExportPolicy | The 'appliance.DataExportPolicy' resource to create.

try:
    # Create a 'appliance.DataExportPolicy' resource.
    api_response = api_instance.create_appliance_data_export_policy(appliance_data_export_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->create_appliance_data_export_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_data_export_policy** | [**ApplianceDataExportPolicy**](ApplianceDataExportPolicy.md)| The &#39;appliance.DataExportPolicy&#39; resource to create. | 

### Return type

[**ApplianceDataExportPolicy**](ApplianceDataExportPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.DataExportPolicy&#39; resource was created as requested. The &#39;appliance.DataExportPolicy&#39; resource is created before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.DataExportPolicy&#39; resource is asynchronously being created as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_appliance_device_claim**
> ApplianceDeviceClaim create_appliance_device_claim(appliance_device_claim)

Create a 'appliance.DeviceClaim' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
appliance_device_claim = intersight.ApplianceDeviceClaim() # ApplianceDeviceClaim | The 'appliance.DeviceClaim' resource to create.

try:
    # Create a 'appliance.DeviceClaim' resource.
    api_response = api_instance.create_appliance_device_claim(appliance_device_claim)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->create_appliance_device_claim: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
appliance_device_claim = intersight.ApplianceDeviceClaim() # ApplianceDeviceClaim | The 'appliance.DeviceClaim' resource to create.

try:
    # Create a 'appliance.DeviceClaim' resource.
    api_response = api_instance.create_appliance_device_claim(appliance_device_claim)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->create_appliance_device_claim: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_device_claim** | [**ApplianceDeviceClaim**](ApplianceDeviceClaim.md)| The &#39;appliance.DeviceClaim&#39; resource to create. | 

### Return type

[**ApplianceDeviceClaim**](ApplianceDeviceClaim.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.DeviceClaim&#39; resource was created as requested. The &#39;appliance.DeviceClaim&#39; resource is created before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.DeviceClaim&#39; resource is asynchronously being created as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_appliance_diag_setting**
> ApplianceDiagSetting create_appliance_diag_setting(appliance_diag_setting)

Create a 'appliance.DiagSetting' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
appliance_diag_setting = intersight.ApplianceDiagSetting() # ApplianceDiagSetting | The 'appliance.DiagSetting' resource to create.

try:
    # Create a 'appliance.DiagSetting' resource.
    api_response = api_instance.create_appliance_diag_setting(appliance_diag_setting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->create_appliance_diag_setting: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
appliance_diag_setting = intersight.ApplianceDiagSetting() # ApplianceDiagSetting | The 'appliance.DiagSetting' resource to create.

try:
    # Create a 'appliance.DiagSetting' resource.
    api_response = api_instance.create_appliance_diag_setting(appliance_diag_setting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->create_appliance_diag_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_diag_setting** | [**ApplianceDiagSetting**](ApplianceDiagSetting.md)| The &#39;appliance.DiagSetting&#39; resource to create. | 

### Return type

[**ApplianceDiagSetting**](ApplianceDiagSetting.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.DiagSetting&#39; resource was created as requested. The &#39;appliance.DiagSetting&#39; resource is created before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.DiagSetting&#39; resource is asynchronously being created as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_appliance_restore**
> ApplianceRestore create_appliance_restore(appliance_restore)

Create a 'appliance.Restore' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
appliance_restore = intersight.ApplianceRestore() # ApplianceRestore | The 'appliance.Restore' resource to create.

try:
    # Create a 'appliance.Restore' resource.
    api_response = api_instance.create_appliance_restore(appliance_restore)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->create_appliance_restore: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
appliance_restore = intersight.ApplianceRestore() # ApplianceRestore | The 'appliance.Restore' resource to create.

try:
    # Create a 'appliance.Restore' resource.
    api_response = api_instance.create_appliance_restore(appliance_restore)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->create_appliance_restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_restore** | [**ApplianceRestore**](ApplianceRestore.md)| The &#39;appliance.Restore&#39; resource to create. | 

### Return type

[**ApplianceRestore**](ApplianceRestore.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.Restore&#39; resource was created as requested. The &#39;appliance.Restore&#39; resource is created before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.Restore&#39; resource is asynchronously being created as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_appliance_backup**
> delete_appliance_backup(moid)

Delete a 'appliance.Backup' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Delete a 'appliance.Backup' resource.
    api_instance.delete_appliance_backup(moid)
except ApiException as e:
    print("Exception when calling ApplianceApi->delete_appliance_backup: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Delete a 'appliance.Backup' resource.
    api_instance.delete_appliance_backup(moid)
except ApiException as e:
    print("Exception when calling ApplianceApi->delete_appliance_backup: %s\n" % e)
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

# **delete_appliance_restore**
> delete_appliance_restore(moid)

Delete a 'appliance.Restore' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Delete a 'appliance.Restore' resource.
    api_instance.delete_appliance_restore(moid)
except ApiException as e:
    print("Exception when calling ApplianceApi->delete_appliance_restore: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Delete a 'appliance.Restore' resource.
    api_instance.delete_appliance_restore(moid)
except ApiException as e:
    print("Exception when calling ApplianceApi->delete_appliance_restore: %s\n" % e)
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

# **get_appliance_backup_by_moid**
> ApplianceBackup get_appliance_backup_by_moid(moid)

Read a 'appliance.Backup' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.Backup' resource.
    api_response = api_instance.get_appliance_backup_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_backup_by_moid: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.Backup' resource.
    api_response = api_instance.get_appliance_backup_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_backup_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**ApplianceBackup**](ApplianceBackup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.Backup&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_backup_list**
> ApplianceBackupList get_appliance_backup_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'appliance.Backup' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.Backup' resource.
    api_response = api_instance.get_appliance_backup_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_backup_list: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.Backup' resource.
    api_response = api_instance.get_appliance_backup_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_backup_list: %s\n" % e)
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

[**ApplianceBackupList**](ApplianceBackupList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.Backup&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_backup_policy_by_moid**
> ApplianceBackupPolicy get_appliance_backup_policy_by_moid(moid)

Read a 'appliance.BackupPolicy' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.BackupPolicy' resource.
    api_response = api_instance.get_appliance_backup_policy_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_backup_policy_by_moid: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.BackupPolicy' resource.
    api_response = api_instance.get_appliance_backup_policy_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_backup_policy_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**ApplianceBackupPolicy**](ApplianceBackupPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.BackupPolicy&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_backup_policy_list**
> ApplianceBackupPolicyList get_appliance_backup_policy_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'appliance.BackupPolicy' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.BackupPolicy' resource.
    api_response = api_instance.get_appliance_backup_policy_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_backup_policy_list: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.BackupPolicy' resource.
    api_response = api_instance.get_appliance_backup_policy_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_backup_policy_list: %s\n" % e)
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

[**ApplianceBackupPolicyList**](ApplianceBackupPolicyList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.BackupPolicy&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_certificate_setting_by_moid**
> ApplianceCertificateSetting get_appliance_certificate_setting_by_moid(moid)

Read a 'appliance.CertificateSetting' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.CertificateSetting' resource.
    api_response = api_instance.get_appliance_certificate_setting_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_certificate_setting_by_moid: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.CertificateSetting' resource.
    api_response = api_instance.get_appliance_certificate_setting_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_certificate_setting_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**ApplianceCertificateSetting**](ApplianceCertificateSetting.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.CertificateSetting&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_certificate_setting_list**
> ApplianceCertificateSettingList get_appliance_certificate_setting_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'appliance.CertificateSetting' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.CertificateSetting' resource.
    api_response = api_instance.get_appliance_certificate_setting_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_certificate_setting_list: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.CertificateSetting' resource.
    api_response = api_instance.get_appliance_certificate_setting_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_certificate_setting_list: %s\n" % e)
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

[**ApplianceCertificateSettingList**](ApplianceCertificateSettingList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.CertificateSetting&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_data_export_policy_by_moid**
> ApplianceDataExportPolicy get_appliance_data_export_policy_by_moid(moid)

Read a 'appliance.DataExportPolicy' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.DataExportPolicy' resource.
    api_response = api_instance.get_appliance_data_export_policy_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_data_export_policy_by_moid: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.DataExportPolicy' resource.
    api_response = api_instance.get_appliance_data_export_policy_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_data_export_policy_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**ApplianceDataExportPolicy**](ApplianceDataExportPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.DataExportPolicy&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_data_export_policy_list**
> ApplianceDataExportPolicyList get_appliance_data_export_policy_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'appliance.DataExportPolicy' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.DataExportPolicy' resource.
    api_response = api_instance.get_appliance_data_export_policy_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_data_export_policy_list: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.DataExportPolicy' resource.
    api_response = api_instance.get_appliance_data_export_policy_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_data_export_policy_list: %s\n" % e)
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

[**ApplianceDataExportPolicyList**](ApplianceDataExportPolicyList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.DataExportPolicy&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_device_claim_by_moid**
> ApplianceDeviceClaim get_appliance_device_claim_by_moid(moid)

Read a 'appliance.DeviceClaim' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.DeviceClaim' resource.
    api_response = api_instance.get_appliance_device_claim_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_device_claim_by_moid: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.DeviceClaim' resource.
    api_response = api_instance.get_appliance_device_claim_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_device_claim_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**ApplianceDeviceClaim**](ApplianceDeviceClaim.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.DeviceClaim&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_device_claim_list**
> ApplianceDeviceClaimList get_appliance_device_claim_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'appliance.DeviceClaim' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.DeviceClaim' resource.
    api_response = api_instance.get_appliance_device_claim_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_device_claim_list: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.DeviceClaim' resource.
    api_response = api_instance.get_appliance_device_claim_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_device_claim_list: %s\n" % e)
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

[**ApplianceDeviceClaimList**](ApplianceDeviceClaimList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.DeviceClaim&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_diag_setting_by_moid**
> ApplianceDiagSetting get_appliance_diag_setting_by_moid(moid)

Read a 'appliance.DiagSetting' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.DiagSetting' resource.
    api_response = api_instance.get_appliance_diag_setting_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_diag_setting_by_moid: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.DiagSetting' resource.
    api_response = api_instance.get_appliance_diag_setting_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_diag_setting_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**ApplianceDiagSetting**](ApplianceDiagSetting.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.DiagSetting&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_diag_setting_list**
> ApplianceDiagSettingList get_appliance_diag_setting_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'appliance.DiagSetting' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.DiagSetting' resource.
    api_response = api_instance.get_appliance_diag_setting_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_diag_setting_list: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.DiagSetting' resource.
    api_response = api_instance.get_appliance_diag_setting_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_diag_setting_list: %s\n" % e)
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

[**ApplianceDiagSettingList**](ApplianceDiagSettingList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.DiagSetting&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_image_bundle_by_moid**
> ApplianceImageBundle get_appliance_image_bundle_by_moid(moid)

Read a 'appliance.ImageBundle' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.ImageBundle' resource.
    api_response = api_instance.get_appliance_image_bundle_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_image_bundle_by_moid: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.ImageBundle' resource.
    api_response = api_instance.get_appliance_image_bundle_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_image_bundle_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**ApplianceImageBundle**](ApplianceImageBundle.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.ImageBundle&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_image_bundle_list**
> ApplianceImageBundleList get_appliance_image_bundle_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'appliance.ImageBundle' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.ImageBundle' resource.
    api_response = api_instance.get_appliance_image_bundle_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_image_bundle_list: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.ImageBundle' resource.
    api_response = api_instance.get_appliance_image_bundle_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_image_bundle_list: %s\n" % e)
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

[**ApplianceImageBundleList**](ApplianceImageBundleList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.ImageBundle&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_node_info_by_moid**
> ApplianceNodeInfo get_appliance_node_info_by_moid(moid)

Read a 'appliance.NodeInfo' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.NodeInfo' resource.
    api_response = api_instance.get_appliance_node_info_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_node_info_by_moid: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.NodeInfo' resource.
    api_response = api_instance.get_appliance_node_info_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_node_info_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**ApplianceNodeInfo**](ApplianceNodeInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.NodeInfo&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_node_info_list**
> ApplianceNodeInfoList get_appliance_node_info_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'appliance.NodeInfo' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.NodeInfo' resource.
    api_response = api_instance.get_appliance_node_info_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_node_info_list: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.NodeInfo' resource.
    api_response = api_instance.get_appliance_node_info_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_node_info_list: %s\n" % e)
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

[**ApplianceNodeInfoList**](ApplianceNodeInfoList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.NodeInfo&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_restore_by_moid**
> ApplianceRestore get_appliance_restore_by_moid(moid)

Read a 'appliance.Restore' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.Restore' resource.
    api_response = api_instance.get_appliance_restore_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_restore_by_moid: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.Restore' resource.
    api_response = api_instance.get_appliance_restore_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_restore_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**ApplianceRestore**](ApplianceRestore.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.Restore&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_restore_list**
> ApplianceRestoreList get_appliance_restore_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'appliance.Restore' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.Restore' resource.
    api_response = api_instance.get_appliance_restore_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_restore_list: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.Restore' resource.
    api_response = api_instance.get_appliance_restore_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_restore_list: %s\n" % e)
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

[**ApplianceRestoreList**](ApplianceRestoreList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.Restore&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_setup_info_by_moid**
> ApplianceSetupInfo get_appliance_setup_info_by_moid(moid)

Read a 'appliance.SetupInfo' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.SetupInfo' resource.
    api_response = api_instance.get_appliance_setup_info_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_setup_info_by_moid: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.SetupInfo' resource.
    api_response = api_instance.get_appliance_setup_info_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_setup_info_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**ApplianceSetupInfo**](ApplianceSetupInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.SetupInfo&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_setup_info_list**
> ApplianceSetupInfoList get_appliance_setup_info_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'appliance.SetupInfo' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.SetupInfo' resource.
    api_response = api_instance.get_appliance_setup_info_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_setup_info_list: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.SetupInfo' resource.
    api_response = api_instance.get_appliance_setup_info_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_setup_info_list: %s\n" % e)
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

[**ApplianceSetupInfoList**](ApplianceSetupInfoList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.SetupInfo&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_system_info_by_moid**
> ApplianceSystemInfo get_appliance_system_info_by_moid(moid)

Read a 'appliance.SystemInfo' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.SystemInfo' resource.
    api_response = api_instance.get_appliance_system_info_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_system_info_by_moid: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.SystemInfo' resource.
    api_response = api_instance.get_appliance_system_info_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_system_info_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**ApplianceSystemInfo**](ApplianceSystemInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.SystemInfo&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_system_info_list**
> ApplianceSystemInfoList get_appliance_system_info_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'appliance.SystemInfo' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.SystemInfo' resource.
    api_response = api_instance.get_appliance_system_info_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_system_info_list: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.SystemInfo' resource.
    api_response = api_instance.get_appliance_system_info_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_system_info_list: %s\n" % e)
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

[**ApplianceSystemInfoList**](ApplianceSystemInfoList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.SystemInfo&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_upgrade_by_moid**
> ApplianceUpgrade get_appliance_upgrade_by_moid(moid)

Read a 'appliance.Upgrade' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.Upgrade' resource.
    api_response = api_instance.get_appliance_upgrade_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_upgrade_by_moid: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.Upgrade' resource.
    api_response = api_instance.get_appliance_upgrade_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_upgrade_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**ApplianceUpgrade**](ApplianceUpgrade.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.Upgrade&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_upgrade_list**
> ApplianceUpgradeList get_appliance_upgrade_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'appliance.Upgrade' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.Upgrade' resource.
    api_response = api_instance.get_appliance_upgrade_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_upgrade_list: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.Upgrade' resource.
    api_response = api_instance.get_appliance_upgrade_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_upgrade_list: %s\n" % e)
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

[**ApplianceUpgradeList**](ApplianceUpgradeList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.Upgrade&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_upgrade_policy_by_moid**
> ApplianceUpgradePolicy get_appliance_upgrade_policy_by_moid(moid)

Read a 'appliance.UpgradePolicy' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.UpgradePolicy' resource.
    api_response = api_instance.get_appliance_upgrade_policy_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_upgrade_policy_by_moid: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.

try:
    # Read a 'appliance.UpgradePolicy' resource.
    api_response = api_instance.get_appliance_upgrade_policy_by_moid(moid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_upgrade_policy_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 

### Return type

[**ApplianceUpgradePolicy**](ApplianceUpgradePolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.UpgradePolicy&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_upgrade_policy_list**
> ApplianceUpgradePolicyList get_appliance_upgrade_policy_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)

Read a 'appliance.UpgradePolicy' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.UpgradePolicy' resource.
    api_response = api_instance.get_appliance_upgrade_policy_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_upgrade_policy_list: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
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
    # Read a 'appliance.UpgradePolicy' resource.
    api_response = api_instance.get_appliance_upgrade_policy_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->get_appliance_upgrade_policy_list: %s\n" % e)
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

[**ApplianceUpgradePolicyList**](ApplianceUpgradePolicyList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.UpgradePolicy&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_appliance_backup_policy**
> ApplianceBackupPolicy patch_appliance_backup_policy(moid, appliance_backup_policy)

Update a 'appliance.BackupPolicy' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_backup_policy = intersight.ApplianceBackupPolicy() # ApplianceBackupPolicy | The 'appliance.BackupPolicy' resource to update.

try:
    # Update a 'appliance.BackupPolicy' resource.
    api_response = api_instance.patch_appliance_backup_policy(moid, appliance_backup_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->patch_appliance_backup_policy: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_backup_policy = intersight.ApplianceBackupPolicy() # ApplianceBackupPolicy | The 'appliance.BackupPolicy' resource to update.

try:
    # Update a 'appliance.BackupPolicy' resource.
    api_response = api_instance.patch_appliance_backup_policy(moid, appliance_backup_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->patch_appliance_backup_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **appliance_backup_policy** | [**ApplianceBackupPolicy**](ApplianceBackupPolicy.md)| The &#39;appliance.BackupPolicy&#39; resource to update. | 

### Return type

[**ApplianceBackupPolicy**](ApplianceBackupPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.BackupPolicy&#39; resource was patched as requested. The &#39;appliance.BackupPolicy&#39; resource is patched before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.BackupPolicy&#39; resource is asynchronously being patched as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_appliance_certificate_setting**
> ApplianceCertificateSetting patch_appliance_certificate_setting(moid, appliance_certificate_setting)

Update a 'appliance.CertificateSetting' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_certificate_setting = intersight.ApplianceCertificateSetting() # ApplianceCertificateSetting | The 'appliance.CertificateSetting' resource to update.

try:
    # Update a 'appliance.CertificateSetting' resource.
    api_response = api_instance.patch_appliance_certificate_setting(moid, appliance_certificate_setting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->patch_appliance_certificate_setting: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_certificate_setting = intersight.ApplianceCertificateSetting() # ApplianceCertificateSetting | The 'appliance.CertificateSetting' resource to update.

try:
    # Update a 'appliance.CertificateSetting' resource.
    api_response = api_instance.patch_appliance_certificate_setting(moid, appliance_certificate_setting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->patch_appliance_certificate_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **appliance_certificate_setting** | [**ApplianceCertificateSetting**](ApplianceCertificateSetting.md)| The &#39;appliance.CertificateSetting&#39; resource to update. | 

### Return type

[**ApplianceCertificateSetting**](ApplianceCertificateSetting.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.CertificateSetting&#39; resource was patched as requested. The &#39;appliance.CertificateSetting&#39; resource is patched before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.CertificateSetting&#39; resource is asynchronously being patched as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_appliance_data_export_policy**
> ApplianceDataExportPolicy patch_appliance_data_export_policy(moid, appliance_data_export_policy)

Update a 'appliance.DataExportPolicy' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_data_export_policy = intersight.ApplianceDataExportPolicy() # ApplianceDataExportPolicy | The 'appliance.DataExportPolicy' resource to update.

try:
    # Update a 'appliance.DataExportPolicy' resource.
    api_response = api_instance.patch_appliance_data_export_policy(moid, appliance_data_export_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->patch_appliance_data_export_policy: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_data_export_policy = intersight.ApplianceDataExportPolicy() # ApplianceDataExportPolicy | The 'appliance.DataExportPolicy' resource to update.

try:
    # Update a 'appliance.DataExportPolicy' resource.
    api_response = api_instance.patch_appliance_data_export_policy(moid, appliance_data_export_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->patch_appliance_data_export_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **appliance_data_export_policy** | [**ApplianceDataExportPolicy**](ApplianceDataExportPolicy.md)| The &#39;appliance.DataExportPolicy&#39; resource to update. | 

### Return type

[**ApplianceDataExportPolicy**](ApplianceDataExportPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.DataExportPolicy&#39; resource was patched as requested. The &#39;appliance.DataExportPolicy&#39; resource is patched before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.DataExportPolicy&#39; resource is asynchronously being patched as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_appliance_diag_setting**
> ApplianceDiagSetting patch_appliance_diag_setting(moid, appliance_diag_setting)

Update a 'appliance.DiagSetting' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_diag_setting = intersight.ApplianceDiagSetting() # ApplianceDiagSetting | The 'appliance.DiagSetting' resource to update.

try:
    # Update a 'appliance.DiagSetting' resource.
    api_response = api_instance.patch_appliance_diag_setting(moid, appliance_diag_setting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->patch_appliance_diag_setting: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_diag_setting = intersight.ApplianceDiagSetting() # ApplianceDiagSetting | The 'appliance.DiagSetting' resource to update.

try:
    # Update a 'appliance.DiagSetting' resource.
    api_response = api_instance.patch_appliance_diag_setting(moid, appliance_diag_setting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->patch_appliance_diag_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **appliance_diag_setting** | [**ApplianceDiagSetting**](ApplianceDiagSetting.md)| The &#39;appliance.DiagSetting&#39; resource to update. | 

### Return type

[**ApplianceDiagSetting**](ApplianceDiagSetting.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.DiagSetting&#39; resource was patched as requested. The &#39;appliance.DiagSetting&#39; resource is patched before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.DiagSetting&#39; resource is asynchronously being patched as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_appliance_setup_info**
> ApplianceSetupInfo patch_appliance_setup_info(moid, appliance_setup_info)

Update a 'appliance.SetupInfo' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_setup_info = intersight.ApplianceSetupInfo() # ApplianceSetupInfo | The 'appliance.SetupInfo' resource to update.

try:
    # Update a 'appliance.SetupInfo' resource.
    api_response = api_instance.patch_appliance_setup_info(moid, appliance_setup_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->patch_appliance_setup_info: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_setup_info = intersight.ApplianceSetupInfo() # ApplianceSetupInfo | The 'appliance.SetupInfo' resource to update.

try:
    # Update a 'appliance.SetupInfo' resource.
    api_response = api_instance.patch_appliance_setup_info(moid, appliance_setup_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->patch_appliance_setup_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **appliance_setup_info** | [**ApplianceSetupInfo**](ApplianceSetupInfo.md)| The &#39;appliance.SetupInfo&#39; resource to update. | 

### Return type

[**ApplianceSetupInfo**](ApplianceSetupInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.SetupInfo&#39; resource was patched as requested. The &#39;appliance.SetupInfo&#39; resource is patched before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.SetupInfo&#39; resource is asynchronously being patched as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_appliance_upgrade**
> ApplianceUpgrade patch_appliance_upgrade(moid, appliance_upgrade)

Update a 'appliance.Upgrade' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_upgrade = intersight.ApplianceUpgrade() # ApplianceUpgrade | The 'appliance.Upgrade' resource to update.

try:
    # Update a 'appliance.Upgrade' resource.
    api_response = api_instance.patch_appliance_upgrade(moid, appliance_upgrade)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->patch_appliance_upgrade: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_upgrade = intersight.ApplianceUpgrade() # ApplianceUpgrade | The 'appliance.Upgrade' resource to update.

try:
    # Update a 'appliance.Upgrade' resource.
    api_response = api_instance.patch_appliance_upgrade(moid, appliance_upgrade)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->patch_appliance_upgrade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **appliance_upgrade** | [**ApplianceUpgrade**](ApplianceUpgrade.md)| The &#39;appliance.Upgrade&#39; resource to update. | 

### Return type

[**ApplianceUpgrade**](ApplianceUpgrade.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.Upgrade&#39; resource was patched as requested. The &#39;appliance.Upgrade&#39; resource is patched before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.Upgrade&#39; resource is asynchronously being patched as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_appliance_upgrade_policy**
> ApplianceUpgradePolicy patch_appliance_upgrade_policy(moid, appliance_upgrade_policy)

Update a 'appliance.UpgradePolicy' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_upgrade_policy = intersight.ApplianceUpgradePolicy() # ApplianceUpgradePolicy | The 'appliance.UpgradePolicy' resource to update.

try:
    # Update a 'appliance.UpgradePolicy' resource.
    api_response = api_instance.patch_appliance_upgrade_policy(moid, appliance_upgrade_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->patch_appliance_upgrade_policy: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_upgrade_policy = intersight.ApplianceUpgradePolicy() # ApplianceUpgradePolicy | The 'appliance.UpgradePolicy' resource to update.

try:
    # Update a 'appliance.UpgradePolicy' resource.
    api_response = api_instance.patch_appliance_upgrade_policy(moid, appliance_upgrade_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->patch_appliance_upgrade_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **appliance_upgrade_policy** | [**ApplianceUpgradePolicy**](ApplianceUpgradePolicy.md)| The &#39;appliance.UpgradePolicy&#39; resource to update. | 

### Return type

[**ApplianceUpgradePolicy**](ApplianceUpgradePolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.UpgradePolicy&#39; resource was patched as requested. The &#39;appliance.UpgradePolicy&#39; resource is patched before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.UpgradePolicy&#39; resource is asynchronously being patched as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_appliance_backup_policy**
> ApplianceBackupPolicy update_appliance_backup_policy(moid, appliance_backup_policy)

Update a 'appliance.BackupPolicy' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_backup_policy = intersight.ApplianceBackupPolicy() # ApplianceBackupPolicy | The 'appliance.BackupPolicy' resource to update.

try:
    # Update a 'appliance.BackupPolicy' resource.
    api_response = api_instance.update_appliance_backup_policy(moid, appliance_backup_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->update_appliance_backup_policy: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_backup_policy = intersight.ApplianceBackupPolicy() # ApplianceBackupPolicy | The 'appliance.BackupPolicy' resource to update.

try:
    # Update a 'appliance.BackupPolicy' resource.
    api_response = api_instance.update_appliance_backup_policy(moid, appliance_backup_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->update_appliance_backup_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **appliance_backup_policy** | [**ApplianceBackupPolicy**](ApplianceBackupPolicy.md)| The &#39;appliance.BackupPolicy&#39; resource to update. | 

### Return type

[**ApplianceBackupPolicy**](ApplianceBackupPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.BackupPolicy&#39; resource was modified as requested. The &#39;appliance.BackupPolicy&#39; resource is modified before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.BackupPolicy&#39; resource is asynchronously being modified as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_appliance_certificate_setting**
> ApplianceCertificateSetting update_appliance_certificate_setting(moid, appliance_certificate_setting)

Update a 'appliance.CertificateSetting' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_certificate_setting = intersight.ApplianceCertificateSetting() # ApplianceCertificateSetting | The 'appliance.CertificateSetting' resource to update.

try:
    # Update a 'appliance.CertificateSetting' resource.
    api_response = api_instance.update_appliance_certificate_setting(moid, appliance_certificate_setting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->update_appliance_certificate_setting: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_certificate_setting = intersight.ApplianceCertificateSetting() # ApplianceCertificateSetting | The 'appliance.CertificateSetting' resource to update.

try:
    # Update a 'appliance.CertificateSetting' resource.
    api_response = api_instance.update_appliance_certificate_setting(moid, appliance_certificate_setting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->update_appliance_certificate_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **appliance_certificate_setting** | [**ApplianceCertificateSetting**](ApplianceCertificateSetting.md)| The &#39;appliance.CertificateSetting&#39; resource to update. | 

### Return type

[**ApplianceCertificateSetting**](ApplianceCertificateSetting.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.CertificateSetting&#39; resource was modified as requested. The &#39;appliance.CertificateSetting&#39; resource is modified before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.CertificateSetting&#39; resource is asynchronously being modified as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_appliance_data_export_policy**
> ApplianceDataExportPolicy update_appliance_data_export_policy(moid, appliance_data_export_policy)

Update a 'appliance.DataExportPolicy' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_data_export_policy = intersight.ApplianceDataExportPolicy() # ApplianceDataExportPolicy | The 'appliance.DataExportPolicy' resource to update.

try:
    # Update a 'appliance.DataExportPolicy' resource.
    api_response = api_instance.update_appliance_data_export_policy(moid, appliance_data_export_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->update_appliance_data_export_policy: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_data_export_policy = intersight.ApplianceDataExportPolicy() # ApplianceDataExportPolicy | The 'appliance.DataExportPolicy' resource to update.

try:
    # Update a 'appliance.DataExportPolicy' resource.
    api_response = api_instance.update_appliance_data_export_policy(moid, appliance_data_export_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->update_appliance_data_export_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **appliance_data_export_policy** | [**ApplianceDataExportPolicy**](ApplianceDataExportPolicy.md)| The &#39;appliance.DataExportPolicy&#39; resource to update. | 

### Return type

[**ApplianceDataExportPolicy**](ApplianceDataExportPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.DataExportPolicy&#39; resource was modified as requested. The &#39;appliance.DataExportPolicy&#39; resource is modified before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.DataExportPolicy&#39; resource is asynchronously being modified as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_appliance_diag_setting**
> ApplianceDiagSetting update_appliance_diag_setting(moid, appliance_diag_setting)

Update a 'appliance.DiagSetting' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_diag_setting = intersight.ApplianceDiagSetting() # ApplianceDiagSetting | The 'appliance.DiagSetting' resource to update.

try:
    # Update a 'appliance.DiagSetting' resource.
    api_response = api_instance.update_appliance_diag_setting(moid, appliance_diag_setting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->update_appliance_diag_setting: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_diag_setting = intersight.ApplianceDiagSetting() # ApplianceDiagSetting | The 'appliance.DiagSetting' resource to update.

try:
    # Update a 'appliance.DiagSetting' resource.
    api_response = api_instance.update_appliance_diag_setting(moid, appliance_diag_setting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->update_appliance_diag_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **appliance_diag_setting** | [**ApplianceDiagSetting**](ApplianceDiagSetting.md)| The &#39;appliance.DiagSetting&#39; resource to update. | 

### Return type

[**ApplianceDiagSetting**](ApplianceDiagSetting.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.DiagSetting&#39; resource was modified as requested. The &#39;appliance.DiagSetting&#39; resource is modified before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.DiagSetting&#39; resource is asynchronously being modified as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_appliance_setup_info**
> ApplianceSetupInfo update_appliance_setup_info(moid, appliance_setup_info)

Update a 'appliance.SetupInfo' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_setup_info = intersight.ApplianceSetupInfo() # ApplianceSetupInfo | The 'appliance.SetupInfo' resource to update.

try:
    # Update a 'appliance.SetupInfo' resource.
    api_response = api_instance.update_appliance_setup_info(moid, appliance_setup_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->update_appliance_setup_info: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_setup_info = intersight.ApplianceSetupInfo() # ApplianceSetupInfo | The 'appliance.SetupInfo' resource to update.

try:
    # Update a 'appliance.SetupInfo' resource.
    api_response = api_instance.update_appliance_setup_info(moid, appliance_setup_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->update_appliance_setup_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **appliance_setup_info** | [**ApplianceSetupInfo**](ApplianceSetupInfo.md)| The &#39;appliance.SetupInfo&#39; resource to update. | 

### Return type

[**ApplianceSetupInfo**](ApplianceSetupInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.SetupInfo&#39; resource was modified as requested. The &#39;appliance.SetupInfo&#39; resource is modified before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.SetupInfo&#39; resource is asynchronously being modified as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_appliance_upgrade**
> ApplianceUpgrade update_appliance_upgrade(moid, appliance_upgrade)

Update a 'appliance.Upgrade' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_upgrade = intersight.ApplianceUpgrade() # ApplianceUpgrade | The 'appliance.Upgrade' resource to update.

try:
    # Update a 'appliance.Upgrade' resource.
    api_response = api_instance.update_appliance_upgrade(moid, appliance_upgrade)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->update_appliance_upgrade: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_upgrade = intersight.ApplianceUpgrade() # ApplianceUpgrade | The 'appliance.Upgrade' resource to update.

try:
    # Update a 'appliance.Upgrade' resource.
    api_response = api_instance.update_appliance_upgrade(moid, appliance_upgrade)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->update_appliance_upgrade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **appliance_upgrade** | [**ApplianceUpgrade**](ApplianceUpgrade.md)| The &#39;appliance.Upgrade&#39; resource to update. | 

### Return type

[**ApplianceUpgrade**](ApplianceUpgrade.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.Upgrade&#39; resource was modified as requested. The &#39;appliance.Upgrade&#39; resource is modified before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.Upgrade&#39; resource is asynchronously being modified as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_appliance_upgrade_policy**
> ApplianceUpgradePolicy update_appliance_upgrade_policy(moid, appliance_upgrade_policy)

Update a 'appliance.UpgradePolicy' resource.

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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_upgrade_policy = intersight.ApplianceUpgradePolicy() # ApplianceUpgradePolicy | The 'appliance.UpgradePolicy' resource to update.

try:
    # Update a 'appliance.UpgradePolicy' resource.
    api_response = api_instance.update_appliance_upgrade_policy(moid, appliance_upgrade_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->update_appliance_upgrade_policy: %s\n" % e)
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
api_instance = intersight.ApplianceApi(intersight.ApiClient(configuration))
moid = 'moid_example' # str | The unique Moid identifier of a resource instance.
appliance_upgrade_policy = intersight.ApplianceUpgradePolicy() # ApplianceUpgradePolicy | The 'appliance.UpgradePolicy' resource to update.

try:
    # Update a 'appliance.UpgradePolicy' resource.
    api_response = api_instance.update_appliance_upgrade_policy(moid, appliance_upgrade_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplianceApi->update_appliance_upgrade_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. | 
 **appliance_upgrade_policy** | [**ApplianceUpgradePolicy**](ApplianceUpgradePolicy.md)| The &#39;appliance.UpgradePolicy&#39; resource to update. | 

### Return type

[**ApplianceUpgradePolicy**](ApplianceUpgradePolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.UpgradePolicy&#39; resource was modified as requested. The &#39;appliance.UpgradePolicy&#39; resource is modified before this response is sent back and the resource is returned in the body of the message.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.UpgradePolicy&#39; resource is asynchronously being modified as requested.  |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request.  |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error.  |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

