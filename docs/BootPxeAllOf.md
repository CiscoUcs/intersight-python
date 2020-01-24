# BootPxeAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface_name** | **str** | The name of the underlying virtual ethernet interface used by the PXE boot device.   | [optional] 
**interface_source** | **str** | Lists the supported Interface Source for PXE device. Supported values are \&quot;name\&quot; and \&quot;mac\&quot;.   | [optional] [default to 'name']
**ip_type** | **str** | The IP Address family type to use during the PXE Boot process.   | [optional] [default to 'None']
**mac_address** | **str** | The MAC Address of the underlying virtual ethernet interface used by the PXE boot device.   | [optional] 
**port** | **int** | The logical port id of the ethernet interface used by the PXE device. Port is a deprecated property. Default value is changed to &#39;-1&#39; as this is invalid port. New or modified pxe device has the port value always set to &#39;-1&#39;.   | [optional] [readonly] 
**slot** | **str** | The slot ID of the adapter on which the underlying virtual ethernet interface is present. Supported values are ( 1 - 255, \&quot;MLOM\&quot;, \&quot;L\&quot;, \&quot;L1\&quot;, \&quot;L2\&quot;, \&quot;OCP\&quot;).    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


