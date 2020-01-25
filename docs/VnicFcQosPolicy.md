# VnicFcQosPolicy

A Fibre Channel Quality of Service (QoS) policy assigns a system class to the outgoing traffic for a vHBA. This system class determines the quality of service for the outgoing traffic. For certain adapters you can also specify additional controls like burst and rate on the outgoing traffic. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cos** | **int** | Class of Service to be associated to the traffic on the virtual interface.   | [optional] 
**max_data_field_size** | **int** | The maximum size of the Fibre Channel frame payload bytes that the virtual interface supports.   | [optional] 
**rate_limit** | **int** | The value in Mbps to use for limiting the data rate on the virtual interface. Setting this to zero will turn rate limiting off.    | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


