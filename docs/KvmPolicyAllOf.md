# KvmPolicyAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_local_server_video** | **bool** | If enabled, displays KVM session on any monitor attached to the server.   | [optional] 
**enable_video_encryption** | **bool** | If enabled, encrypts all video information sent through KVM.   | [optional] 
**enabled** | **bool** | State of the vKVM service on the endpoint.   | [optional] 
**maximum_sessions** | **int** | The maximum number of concurrent KVM sessions allowed.   | [optional] 
**remote_port** | **int** | The port used for KVM communication.    | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 
**profiles** | [**list[PolicyAbstractConfigProfile]**](PolicyAbstractConfigProfile.md) | A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the profile object.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


