# MoMoRefAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**moid** | **str** | The Moid of the referenced REST resource.   | [optional] [readonly] 
**object_type** | **str** | The Object Type of the referenced REST resource.   | [readonly] 
**selector** | **str** | An OData $filter expression which describes the REST resource to be referenced. This field may be set instead of &#39;moid&#39; by clients. If &#39;moid&#39; is set this field is ignored. If &#39;selector&#39; is set and &#39;moid&#39; is empty/absent from the request, Intersight will determine the Moid of the resource matching the filter expression and populate it in the MoRef that is part of the object instance being inserted/updated to fulfill the REST request. An error is returned if the filter matches zero or more than one REST resource. An example filter string is: Serial eq &#39;3AA8B7T11&#39;.     | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


