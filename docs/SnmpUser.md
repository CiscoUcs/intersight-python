# SnmpUser

Complex type for a User based security model, for communication between an agent and manager. Applicable only for SNMPv3. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_auth_password_set** | **bool** | Indicates whether the value of the &#39;authPassword&#39; property has been set.   | [optional] [readonly] 
**auth_password** | **str** | Authorization password for the user.   | [optional] 
**auth_type** | **str** | Authorization protocol for authenticating the user.   | [optional] [default to 'NA']
**is_privacy_password_set** | **bool** |  | [optional] 
**name** | **str** | SNMP username. Must have a minimum of 1 and and a maximum of 31 characters.   | [optional] 
**privacy_password** | **str** | Privacy password for the user.   | [optional] 
**privacy_type** | **str** | Privacy protocol for the user.   | [optional] [default to 'NA']
**security_level** | **str** | Security mechanism used for communication between agent and manager.    | [optional] [default to 'AuthPriv']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


