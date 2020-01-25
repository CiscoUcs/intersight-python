# SoftwarerepositoryLocalMachineAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** | When import action in file MO is updated with &#39;GeneratePreSignedDownloadUrl&#39;, Intersight shall return a presigned URL in this property as part of the PATCH response. The user is expected to subsequently download the file using this URL.   | [optional] [readonly] 
**part_size** | **int** | Chunk size (in bytes) of the each part of file to be uploaded.   | [optional] 
**upload_id** | **str** | When the import action in file MO is updated with &#39;GeneratePreSignedUploadUrl&#39;, Intersight shall return a upload Id in this property as part of the PATCH response.   | [optional] 
**upload_url** | **str** | When a file MO is created with &#39;LocalMachine&#39; as the source, Intersight shall return a presigned URL in this property as part of the POST response. The user is expected to subsequently upload the file content using this URL. Once this upload has been completed, the user is expected to PATCH the Uploader object&#39;s transfer state to success.   | [optional] [readonly] 
**upload_urls** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


