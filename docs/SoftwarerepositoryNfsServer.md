# SoftwarerepositoryNfsServer

An external file repository accessible through the NFS protocol. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_options** | **str** | For NFS, leave the field blank or enter one or more comma seperated options from the following.For Example, \&quot; \&quot; , \&quot; ro \&quot; , \&quot; ro , rw \&quot; . * ro. * rw. * nolock. * noexec. * soft. * PORT&#x3D;VALUE. * timeo&#x3D;VALUE. * retry&#x3D;VALUE.    | [optional] [readonly] 
**remote_file** | **str** | Filename of the image in the NFS server. For example:ucs-c220m5-huu-3.1.2c.iso.   | [optional] 
**remote_ip** | **str** | Hostname or IP Address of the NFS server.   | [optional] 
**remote_share** | **str** | Remote directory where the image is present. For example:/share/subfolder.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


