# SnmpPolicy

Policy to configure SNMP settings on endpoint. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_community_string** | **str** | The default SNMPv1, SNMPv2c community name or SNMPv3 username to include on any trap messages sent to the SNMP host. The name can be 18 characters long.   | [optional] 
**community_access** | **str** | Controls access to the information in the inventory tables. Applicable only for SNMPv1 and SNMPv2c users.   | [optional] [default to 'Disabled']
**enabled** | **bool** | State of the SNMP Policy on the endpoint. If enabled, the endpoint sends SNMP traps to the designated host.   | [optional] 
**engine_id** | **str** | User-defined unique identification of the static engine.   | [optional] 
**snmp_port** | **int** | Port on which Cisco IMC SNMP agent runs.   | [optional] 
**snmp_traps** | [**list[SnmpTrap]**](SnmpTrap.md) |  | [optional] 
**snmp_users** | [**list[SnmpUser]**](SnmpUser.md) |  | [optional] 
**sys_contact** | **str** | Contact person responsible for the SNMP implementation. Enter a string up to 64 characters, such as an email address or a name and telephone number.   | [optional] 
**sys_location** | **str** | Location of host on which the SNMP agent (server) runs.   | [optional] 
**trap_community** | **str** | SNMP community group used for sending SNMP trap to other devices. Valid only for SNMPv2c users.    | [optional] 
**organization** | [**OrganizationOrganization**](.md) |  | [optional] 
**profiles** | [**list[PolicyAbstractConfigProfile]**](PolicyAbstractConfigProfile.md) | A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the profile object.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


