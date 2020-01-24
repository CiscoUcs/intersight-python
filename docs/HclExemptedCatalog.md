# HclExemptedCatalog

Collection used to store exempted products (ie. adapters, storage controllers, etc). These products should be ignored for HCL validation purposes. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | Reason for the exemption.   | [optional] 
**name** | **str** | A unique descriptive name of the exemption.   | [optional] 
**os_vendor** | **str** | Vendor of the Operating System.   | [optional] 
**os_version** | **str** | Version of the Operating system.   | [optional] 
**processor_name** | **str** | Name of the processor supported for the server.   | [optional] 
**product_models** | **list[str]** |  | [optional] 
**product_type** | **str** | Type of the product/adapter say PT for Pass Through controllers.   | [optional] 
**server_pid** | **str** | Three part ID representing the server model as returned by UCSM/CIMC XML APIs.   | [optional] 
**ucs_version** | **str** | Version of the UCS software.   | [optional] 
**version_type** | **str** | Type of the UCS version indicating whether it is a UCSM release vesion or a IMC release.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


