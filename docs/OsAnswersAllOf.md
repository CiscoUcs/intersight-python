# OsAnswersAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_answer_file_set** | **bool** | Indicates whether the value of the &#39;answerFile&#39; property has been set.   | [optional] [readonly] 
**answer_file** | **str** | If the source of the answers is a static file, the content of the file is stored as value in this property.  The value is mandatory only when the &#39;Source&#39; property has been set to &#39;File&#39;.    | [optional] 
**hostname** | **str** | Hostname to be configured for the server in the OS.    | [optional] 
**ip_config_type** | **str** | IP configuration type. Values are Static or Dynamic configuration of IP.  In case of static IP configuration, IP address, gateway and other details need to be populated. In case of dynamic the IP configuration is obtained dynamically from DHCP.    | [optional] [default to 'static']
**ip_v4_config** | [**CommIpV4Interface**](CommIpV4Interface.md) |  | [optional] 
**is_root_password_set** | **bool** |  | [optional] 
**nameserver** | **str** | IP address of the name server to be configured in the OS.    | [optional] 
**product_key** | **str** | The product key to be used for a specific version of Windows installation.    | [optional] 
**root_password** | **str** | Password to be configured for the root / administrator user in the OS.    | [optional] 
**source** | **str** | Answer values can be provided from three sources - Embedded in OS image, static file, or as placeholder values for an answer file template.  Source of the answers is given as value, Embedded/File/Template. &#39;Embedded&#39; option indicates that the answer file is embedded within the OS Image. &#39;File&#39; option indicates that the answers are provided as a file. &#39;Template&#39; indicates that the placeholders in the selected os.ConfigurationFile MO are replaced with values provided as os.Answers MO.     | [optional] [default to 'None']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


