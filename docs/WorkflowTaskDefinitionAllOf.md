# WorkflowTaskDefinitionAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_version** | **bool** | When true this will be the task version that is used when a specific task definition version is not specified. The very first task definition created with a name will be set as the default version, after that user can explicitly set any version of the task definition as the default version.   | [optional] 
**description** | **str** | The task definition description to describe what this task will do when executed.   | [optional] 
**internal_properties** | [**WorkflowInternalProperties**](WorkflowInternalProperties.md) |  | [optional] 
**label** | **str** | A user friendly short name to identify the task definition.   | [optional] 
**license_entitlement** | **str** | License entitlement required to run this task. It is determined by license requirement of features.   | [optional] [readonly] [default to 'Base']
**name** | **str** | The name of the task definition. The name should follow this convention &lt;Verb or Action&gt;&lt;Category&gt;&lt;Vendor&gt;&lt;Product&gt;&lt;Noun or object&gt; Verb or Action is a required portion of the name and this must be part of the pre-approved verb list. Category is an optional field and this will refer to the broad category of the task referring to the type of resource or endpoint. If there is no specific category then use \&quot;Generic\&quot; if required. Vendor is an optional field and this will refer to the specific vendor this task applies to. If the task is generic and not tied to a vendor, then do not specify anything. Product is an optional field, this will contain the vendor product and model when desired. Noun or object is a required field and  this will contain the noun or object on which the action is being performed. Examples SendEmail  - This is a task in Generic category for sending email. NewStorageVolume - This is a vendor agnostic task under Storage device category for creating a new volume.   | [optional] 
**properties** | [**WorkflowProperties**](WorkflowProperties.md) |  | [optional] 
**version** | **int** | The version of the task definition so we can support multiple versions of a task definition.    | [optional] 
**catalog** | [**WorkflowCatalog**](.md) |  | [optional] 
**implemented_tasks** | [**list[WorkflowTaskDefinition]**](WorkflowTaskDefinition.md) | A reference to a workflowTaskDefinition resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of all the implemented task for this TaskDefinition. When this list is populated it implies that this TaskDefinition has multiple implementations.  | [optional] 
**interface_task** | [**WorkflowTaskDefinition**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


