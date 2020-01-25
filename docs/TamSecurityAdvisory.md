# TamSecurityAdvisory

Intersight representation of a Cisco PSIRT (https://tools.cisco.com/security/center/publicationListing.x) advisory definition. It includes the description of the security advisory and a corresponding reference to the published advisory. It also includes the Intersight data sources needed to evaluate the applicability of this advisory for relevant Intersight managed objects. A PSIRT definition is evaluated against all managed object referenced using the included data sources. Only Cisco TAC and Intersight devops engineers have the ability to create PSIRT definitions in Intersight. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**list[TamAction]**](TamAction.md) |  | [optional] 
**advisory_id** | **str** | Cisco generated identifier for the published security advisory.    | [optional] 
**api_data_sources** | [**list[TamApiDataSource]**](TamApiDataSource.md) |  | [optional] 
**base_score** | **float** | CVSS version 3 base score for the security Advisory.    | [optional] 
**cve_ids** | **list[str]** |  | [optional] 
**date_published** | **datetime** | Date when the security advisory was first published by Cisco.    | [optional] 
**date_updated** | **datetime** | Date when the security advisory was last updated by Cisco.    | [optional] 
**environmental_score** | **float** | CVSS version 3 environmental score for the security Advisory.    | [optional] 
**external_url** | **str** | A link to an external URL describing security Advisory in more details.    | [optional] 
**recommendation** | **str** | Recommended action to resolve the security advisory.    | [optional] 
**status** | **str** | Cisco assigned status of the published advisory based on whether the investigation is complete or on-going.    | [optional] [default to 'interim']
**temporal_score** | **float** | CVSS version 3 temporal score for the security Advisory.    | [optional] 
**version** | **str** | Cisco assigned advisory version after latest revision.     | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


