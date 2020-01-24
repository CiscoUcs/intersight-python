# SoftwarerepositoryFile

A file that resides either in an external repository or has been imported to the local repository. If the file is available in the local repository, it is marked as cached. If not, it represents a pointer to a file in an external repository. Instances of this MO will be implicitly created as part of the file import operation. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | User provided description about the file. Cisco provided description for image inventoried from a Cisco repository.   | [optional] 
**download_count** | **int** | The number of times this file has been downloaded from the local repository. It is used by the repository monitoring process to determine the files that are to be evicted from the cache.   | [optional] [readonly] 
**import_action** | **str** | The action to be performed on the imported file. If &#39;PreCache&#39; is set, the image will be cached in Appliance. Applicable in Intersight appliance deployment. If &#39;Evict&#39; is set, the cached file will be removed. Applicable in Intersight appliance deployment. If &#39;GeneratePreSignedUploadUrl&#39; is set, generates pre signed URL (s) for the file to be imported into the repository. Applicable for local machine source. The URL (s) will be populated under LocalMachine file server. If &#39;CompleteImportProcess&#39; is set, the ImportState is marked as &#39;Imported&#39;. Applicable for local machine source. If &#39;Cancel&#39; is set, the ImportState is marked as &#39;Failed&#39;. Applicable for local machine source.    | [optional] [default to 'None']
**import_state** | **str** | The state  of this file in the repository or Appliance. The importState is updated during the import operation and as part of the repository monitoring process.   | [optional] [readonly] [default to 'ReadyForImport']
**imported_time** | **datetime** | The time at which this image or file was imported/cached into the repositry. if the &#39;ImportState&#39; is &#39;Imported&#39;, the time at which this image or file was imported. if the &#39;ImportState&#39; is &#39;Cached&#39;, the time at which this image or file was cached.   | [optional] [readonly] 
**last_access_time** | **datetime** | The time at which this file was last downloaded from the local repository. It is used by the repository monitoring process to determine the files that are to be evicted from the cache.   | [optional] [readonly] 
**md5sum** | **str** | The md5sum checksum of the file. This information is available for all Cisco distributed images and files imported to the local repository.   | [optional] 
**name** | **str** | The name of the file. It is populated as part of the image import operation.    | [optional] 
**release_date** | **datetime** | The date on which the file was released or distributed by its vendor.   | [optional] 
**sha512sum** | **str** | The sha512sum of the file. This information is available for all Cisco distributed images and files imported to the local repository.   | [optional] 
**size** | **int** | The size (in bytes) of the file. This information is available for all Cisco distributed images and files imported to the local repository.   | [optional] 
**software_advisory_url** | **str** | The software advisory, if any, provided by the vendor for this file.   | [optional] 
**source** | [**SoftwarerepositoryFileServer**](SoftwarerepositoryFileServer.md) |  | [optional] 
**version** | **str** | Vendor provided version for the file.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


