# HyperflexCapabilityInfo

A capabilityInfo is like a feature set and/or feature limit for different components of a HyperFlex Cluster. A set of constraints defines the rules, and the corresponding value either determines if the feature would work on a HyperFlex cluster with specific component set, or corresponds to a limit for a set of HyperFlex components. For example, \"minUcsVersion\" for HyperFlex version \"4.0.1a\" corresponds to \"3.2.3\" or \"minHxdpVersion\" for HyperFlex Upgrade operation is \"4.0.1a\" etc. This data can be captured as a capability and at run-time, decision can be made to proceed with the intended operation or not, or proceed with the intended operation with a value catered to specific feature sets. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capability_constraints** | [**list[HclConstraint]**](HclConstraint.md) |  | [optional] 
**name** | **str** | Name of the capability or feature set consisting of a collection of constraint rules and value.   | [optional] 
**value** | **str** | Capability Value which is valid only iff all specified constraints match.    | [optional] [readonly] 
**app_catalog** | [**HyperflexAppCatalog**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


