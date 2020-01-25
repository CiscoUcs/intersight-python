# VmediaMappingAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_protocol** | **str** | Type of Authentication protocol when CIFS is used for communication with the remote server.   | [optional] [default to 'none']
**device_type** | **str** | Type of remote Virtual Media device.   | [optional] [default to 'cdd']
**host_name** | **str** | IP address or hostname of the remote server.   | [optional] 
**is_password_set** | **bool** |  | [optional] 
**mount_options** | **str** | Mount options for the Virtual Media mapping. The field can be left blank or filled in a comma separated list with the following options.\\n For NFS, supported options are ro, rw, nolock, noexec, soft, port&#x3D;VALUE, timeo&#x3D;VALUE, retry&#x3D;VALUE.\\n For CIFS, supported options are soft, nounix, noserverino, guest.\\n For HTTP/HTTPS, the only supported option is noauto.   | [optional] 
**mount_protocol** | **str** | Protocol to use to communicate with the remote server.   | [optional] [default to 'nfs']
**password** | **str** | Password associated with the username.   | [optional] 
**remote_file** | **str** | Name of the remote file. It should be of .img format for HDD Virtual Media mapping and .iso format for CDD Virtual Media mapping.   | [optional] 
**remote_path** | **str** | URL path to the location of the image on the remote server. The preferred format is &#39;/path/&#39;.   | [optional] 
**username** | **str** | Username to log in to the remote server.   | [optional] 
**volume_name** | **str** | Identity of the image for Virtual Media mapping.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


