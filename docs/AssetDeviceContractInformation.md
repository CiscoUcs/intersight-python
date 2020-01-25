# AssetDeviceContractInformation

Contains information about the Cisco device identified by a unique identifier like serial number. It also contains information about warranty, contract status, validity of the device. In future this object could be expanded to store Case, RMA, device topology details. We observe new asset.DeviceRegisteration and use it as a trigger for creating an instance of this object. Currently the data is restricted to Cisco Standalone IMC servers and Fabric Interconnects. Support for more product lines will be added in future. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | [**AssetContractInformation**](AssetContractInformation.md) |  | [optional] 
**contract_status** | **str** | Calculated contract status that is derived based on the service line status and contract end date. It is different from serviceLineStatus property. serviceLineStatus gives us ACTIVE, OVERDUE, EXPIRED. These are transformed into Active, Expiring Soon and Not Covered.   | [optional] [readonly] [default to 'Not Covered']
**covered_product_line_end_date** | **str** | End date of the covered product line. The coverage end date is fetched from Cisco SN2INFO API.   | [optional] [readonly] 
**device_id** | **str** | Unique identifier of the Cisco device. This information is used to query Cisco APIx SN2INFO and CCWR databases.   | [optional] [readonly] 
**device_type** | **str** | Type used to classify the device in Cisco Intersight. Currently supported values are Server and FabricInterconnect. This will be expanded to support more types in future.   | [optional] [readonly] [default to 'None']
**end_customer** | [**AssetCustomerInformation**](AssetCustomerInformation.md) |  | [optional] 
**end_user_global_ultimate** | [**AssetGlobalUltimate**](AssetGlobalUltimate.md) |  | [optional] 
**is_valid** | **bool** | Validates if the device is a genuine Cisco device. Validated is done using the Cisco SN2INFO APIs.   | [optional] [readonly] 
**item_type** | **str** | Item type of this specific Cisco device. example \&quot;Chassis\&quot;.   | [optional] [readonly] 
**maintenance_purchase_order_number** | **str** | Maintenance purchase order number for the Cisco device.   | [optional] [readonly] 
**maintenance_sales_order_number** | **str** | Maintenance sales order number for the Cisco device.   | [optional] [readonly] 
**platform_type** | **str** | The platform type of the Cisco device.   | [optional] [readonly] [default to '']
**product** | [**AssetProductInformation**](AssetProductInformation.md) |  | [optional] 
**purchase_order_number** | **str** | Purchase order number for the Cisco device. It is a unique number assigned for every purchase.   | [optional] [readonly] 
**reseller_global_ultimate** | [**AssetGlobalUltimate**](AssetGlobalUltimate.md) |  | [optional] 
**sales_order_number** | **str** | Sales order number for the Cisco device. It is a unique number assigned for every sale.   | [optional] [readonly] 
**service_description** | **str** | The type of service contract that covers the Cisco device.   | [optional] [readonly] 
**service_end_date** | **datetime** | End date for the Cisco service contract that covers this Cisco device.   | [optional] [readonly] 
**service_level** | **str** | The type of service contract that covers the Cisco device.   | [optional] [readonly] 
**service_sku** | **str** | The SKU of the service contract that covers the Cisco device.   | [optional] [readonly] 
**service_start_date** | **datetime** | Start date for the Cisco service contract that covers this Cisco device.   | [optional] [readonly] 
**state_contract** | **str** | Internal property used for triggering and tracking actions for contract information.    | [optional] [default to 'Update']
**warranty_end_date** | **str** | End date for the warranty that covers the Cisco device.   | [optional] [readonly] 
**warranty_type** | **str** | Type of warranty that covers the Cisco device.    | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistration**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


