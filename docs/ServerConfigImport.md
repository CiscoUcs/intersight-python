# ServerConfigImport

Configuration import action will import the existing configuration from physical server and generate Intersight policies and server profile from it. At end of successful import, server will be assigned to the generated profile which has policies associated with it. No server profile or policies will be generated if configuration import fails. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the imported profile.   | [optional] 
**policy_prefix** | **str** | Policy prefix for the policies of the imported server profile.   | [optional] 
**policy_types** | **list[str]** |  | [optional] 
**profile_name** | **str** | Profile name for the imported server profile.    | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 
**server** | [**ComputeRackUnit**](.md) |  | [optional] 
**server_profile** | [**ServerProfile**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


