# ApplianceBackupBase

BackupBase is the parent type of Backup, Restore, and BackupPolicy managed objects. BackupBase holds the common information required for copying the file from the Intersight Appliance to the remote file server and vice versa. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | Backup filename to backup or restore.   | [optional] 
**protocol** | **str** | Communication protocol used by the file server (e.g. scp or sftp).   | [optional] [default to 'scp']
**remote_host** | **str** | Hostname of the remote file server.   | [optional] 
**remote_path** | **str** | File server directory to copy the file.   | [optional] 
**remote_port** | **int** | Remote TCP port on the file server (e.g. 22 for scp).   | [optional] 
**username** | **str** | Username to authenticate the fileserver.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


