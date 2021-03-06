# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1461
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WorkflowTaskMeta(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_moid': 'str',
        'create_time': 'datetime',
        'domain_group_moid': 'str',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'shared_scope': 'str',
        'tags': 'list[MoTag]',
        'version_context': 'MoVersionContext',
        'ancestors': 'list[MoBaseMoRef]',
        'parent': 'MoBaseMoRef',
        'permission_resources': 'list[MoBaseMoRef]',
        'action_type': 'str',
        'description': 'str',
        'input_keys': 'list[str]',
        'internal': 'bool',
        'name': 'str',
        'output_keys': 'list[str]',
        'response_timeout_sec': 'int',
        'retry_count': 'int',
        'retry_delay_sec': 'int',
        'retry_logic': 'str',
        'src': 'str',
        'timeout_policy': 'str',
        'timeout_sec': 'int'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'create_time': 'CreateTime',
        'domain_group_moid': 'DomainGroupMoid',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'shared_scope': 'SharedScope',
        'tags': 'Tags',
        'version_context': 'VersionContext',
        'ancestors': 'Ancestors',
        'parent': 'Parent',
        'permission_resources': 'PermissionResources',
        'action_type': 'ActionType',
        'description': 'Description',
        'input_keys': 'InputKeys',
        'internal': 'Internal',
        'name': 'Name',
        'output_keys': 'OutputKeys',
        'response_timeout_sec': 'ResponseTimeoutSec',
        'retry_count': 'RetryCount',
        'retry_delay_sec': 'RetryDelaySec',
        'retry_logic': 'RetryLogic',
        'src': 'Src',
        'timeout_policy': 'TimeoutPolicy',
        'timeout_sec': 'TimeoutSec'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, action_type=None, description=None, input_keys=None, internal=None, name=None, output_keys=None, response_timeout_sec=None, retry_count=None, retry_delay_sec=None, retry_logic=None, src=None, timeout_policy=None, timeout_sec=None):
        """
        WorkflowTaskMeta - a model defined in Swagger
        """

        self._account_moid = None
        self._create_time = None
        self._domain_group_moid = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._shared_scope = None
        self._tags = None
        self._version_context = None
        self._ancestors = None
        self._parent = None
        self._permission_resources = None
        self._action_type = None
        self._description = None
        self._input_keys = None
        self._internal = None
        self._name = None
        self._output_keys = None
        self._response_timeout_sec = None
        self._retry_count = None
        self._retry_delay_sec = None
        self._retry_logic = None
        self._src = None
        self._timeout_policy = None
        self._timeout_sec = None

        if account_moid is not None:
          self.account_moid = account_moid
        if create_time is not None:
          self.create_time = create_time
        if domain_group_moid is not None:
          self.domain_group_moid = domain_group_moid
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if shared_scope is not None:
          self.shared_scope = shared_scope
        if tags is not None:
          self.tags = tags
        if version_context is not None:
          self.version_context = version_context
        if ancestors is not None:
          self.ancestors = ancestors
        if parent is not None:
          self.parent = parent
        if permission_resources is not None:
          self.permission_resources = permission_resources
        if action_type is not None:
          self.action_type = action_type
        if description is not None:
          self.description = description
        if input_keys is not None:
          self.input_keys = input_keys
        if internal is not None:
          self.internal = internal
        if name is not None:
          self.name = name
        if output_keys is not None:
          self.output_keys = output_keys
        if response_timeout_sec is not None:
          self.response_timeout_sec = response_timeout_sec
        if retry_count is not None:
          self.retry_count = retry_count
        if retry_delay_sec is not None:
          self.retry_delay_sec = retry_delay_sec
        if retry_logic is not None:
          self.retry_logic = retry_logic
        if src is not None:
          self.src = src
        if timeout_policy is not None:
          self.timeout_policy = timeout_policy
        if timeout_sec is not None:
          self.timeout_sec = timeout_sec

    @property
    def account_moid(self):
        """
        Gets the account_moid of this WorkflowTaskMeta.
        The Account ID for this managed object.

        :return: The account_moid of this WorkflowTaskMeta.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this WorkflowTaskMeta.
        The Account ID for this managed object.

        :param account_moid: The account_moid of this WorkflowTaskMeta.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this WorkflowTaskMeta.
        The time when this managed object was created.

        :return: The create_time of this WorkflowTaskMeta.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this WorkflowTaskMeta.
        The time when this managed object was created.

        :param create_time: The create_time of this WorkflowTaskMeta.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this WorkflowTaskMeta.
        The DomainGroup ID for this managed object.

        :return: The domain_group_moid of this WorkflowTaskMeta.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this WorkflowTaskMeta.
        The DomainGroup ID for this managed object.

        :param domain_group_moid: The domain_group_moid of this WorkflowTaskMeta.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this WorkflowTaskMeta.
        The time when this managed object was last modified.

        :return: The mod_time of this WorkflowTaskMeta.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this WorkflowTaskMeta.
        The time when this managed object was last modified.

        :param mod_time: The mod_time of this WorkflowTaskMeta.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this WorkflowTaskMeta.
        The unique identifier of this Managed Object instance.

        :return: The moid of this WorkflowTaskMeta.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this WorkflowTaskMeta.
        The unique identifier of this Managed Object instance.

        :param moid: The moid of this WorkflowTaskMeta.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this WorkflowTaskMeta.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

        :return: The object_type of this WorkflowTaskMeta.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this WorkflowTaskMeta.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

        :param object_type: The object_type of this WorkflowTaskMeta.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this WorkflowTaskMeta.
        The array of owners which represent effective ownership of this object.

        :return: The owners of this WorkflowTaskMeta.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this WorkflowTaskMeta.
        The array of owners which represent effective ownership of this object.

        :param owners: The owners of this WorkflowTaskMeta.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this WorkflowTaskMeta.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.

        :return: The shared_scope of this WorkflowTaskMeta.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this WorkflowTaskMeta.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.

        :param shared_scope: The shared_scope of this WorkflowTaskMeta.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this WorkflowTaskMeta.
        The array of tags, which allow to add key, value meta-data to managed objects.

        :return: The tags of this WorkflowTaskMeta.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this WorkflowTaskMeta.
        The array of tags, which allow to add key, value meta-data to managed objects.

        :param tags: The tags of this WorkflowTaskMeta.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this WorkflowTaskMeta.
        The versioning info for this managed object.

        :return: The version_context of this WorkflowTaskMeta.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this WorkflowTaskMeta.
        The versioning info for this managed object.

        :param version_context: The version_context of this WorkflowTaskMeta.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this WorkflowTaskMeta.
        The array containing the MO references of the ancestors in the object containment hierarchy.

        :return: The ancestors of this WorkflowTaskMeta.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this WorkflowTaskMeta.
        The array containing the MO references of the ancestors in the object containment hierarchy.

        :param ancestors: The ancestors of this WorkflowTaskMeta.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this WorkflowTaskMeta.
        The direct ancestor of this managed object in the containment hierarchy.

        :return: The parent of this WorkflowTaskMeta.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this WorkflowTaskMeta.
        The direct ancestor of this managed object in the containment hierarchy.

        :param parent: The parent of this WorkflowTaskMeta.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this WorkflowTaskMeta.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.

        :return: The permission_resources of this WorkflowTaskMeta.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this WorkflowTaskMeta.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.

        :param permission_resources: The permission_resources of this WorkflowTaskMeta.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def action_type(self):
        """
        Gets the action_type of this WorkflowTaskMeta.
        A task execution type to indicate if it is a system task.

        :return: The action_type of this WorkflowTaskMeta.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """
        Sets the action_type of this WorkflowTaskMeta.
        A task execution type to indicate if it is a system task.

        :param action_type: The action_type of this WorkflowTaskMeta.
        :type: str
        """

        self._action_type = action_type

    @property
    def description(self):
        """
        Gets the description of this WorkflowTaskMeta.
        A description of the task.

        :return: The description of this WorkflowTaskMeta.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WorkflowTaskMeta.
        A description of the task.

        :param description: The description of this WorkflowTaskMeta.
        :type: str
        """

        self._description = description

    @property
    def input_keys(self):
        """
        Gets the input_keys of this WorkflowTaskMeta.
        Input keys for the task which specifies parameters the task can take in as inputs.

        :return: The input_keys of this WorkflowTaskMeta.
        :rtype: list[str]
        """
        return self._input_keys

    @input_keys.setter
    def input_keys(self, input_keys):
        """
        Sets the input_keys of this WorkflowTaskMeta.
        Input keys for the task which specifies parameters the task can take in as inputs.

        :param input_keys: The input_keys of this WorkflowTaskMeta.
        :type: list[str]
        """

        self._input_keys = input_keys

    @property
    def internal(self):
        """
        Gets the internal of this WorkflowTaskMeta.
        Denotes whether or not this is an internal task.  Internal tasks will be hidden from the UI within a workflow.

        :return: The internal of this WorkflowTaskMeta.
        :rtype: bool
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """
        Sets the internal of this WorkflowTaskMeta.
        Denotes whether or not this is an internal task.  Internal tasks will be hidden from the UI within a workflow.

        :param internal: The internal of this WorkflowTaskMeta.
        :type: bool
        """

        self._internal = internal

    @property
    def name(self):
        """
        Gets the name of this WorkflowTaskMeta.
        A task name that should be unique in Conductor DB.

        :return: The name of this WorkflowTaskMeta.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WorkflowTaskMeta.
        A task name that should be unique in Conductor DB.

        :param name: The name of this WorkflowTaskMeta.
        :type: str
        """

        self._name = name

    @property
    def output_keys(self):
        """
        Gets the output_keys of this WorkflowTaskMeta.
        Output keys for the task which specifies parameters the task will output at the end of execution.

        :return: The output_keys of this WorkflowTaskMeta.
        :rtype: list[str]
        """
        return self._output_keys

    @output_keys.setter
    def output_keys(self, output_keys):
        """
        Sets the output_keys of this WorkflowTaskMeta.
        Output keys for the task which specifies parameters the task will output at the end of execution.

        :param output_keys: The output_keys of this WorkflowTaskMeta.
        :type: list[str]
        """

        self._output_keys = output_keys

    @property
    def response_timeout_sec(self):
        """
        Gets the response_timeout_sec of this WorkflowTaskMeta.
        The worker respnose timeout value.

        :return: The response_timeout_sec of this WorkflowTaskMeta.
        :rtype: int
        """
        return self._response_timeout_sec

    @response_timeout_sec.setter
    def response_timeout_sec(self, response_timeout_sec):
        """
        Sets the response_timeout_sec of this WorkflowTaskMeta.
        The worker respnose timeout value.

        :param response_timeout_sec: The response_timeout_sec of this WorkflowTaskMeta.
        :type: int
        """

        self._response_timeout_sec = response_timeout_sec

    @property
    def retry_count(self):
        """
        Gets the retry_count of this WorkflowTaskMeta.
        A number of reties for this task.

        :return: The retry_count of this WorkflowTaskMeta.
        :rtype: int
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        """
        Sets the retry_count of this WorkflowTaskMeta.
        A number of reties for this task.

        :param retry_count: The retry_count of this WorkflowTaskMeta.
        :type: int
        """

        self._retry_count = retry_count

    @property
    def retry_delay_sec(self):
        """
        Gets the retry_delay_sec of this WorkflowTaskMeta.
        The time on which the retry will be delayed.

        :return: The retry_delay_sec of this WorkflowTaskMeta.
        :rtype: int
        """
        return self._retry_delay_sec

    @retry_delay_sec.setter
    def retry_delay_sec(self, retry_delay_sec):
        """
        Sets the retry_delay_sec of this WorkflowTaskMeta.
        The time on which the retry will be delayed.

        :param retry_delay_sec: The retry_delay_sec of this WorkflowTaskMeta.
        :type: int
        """

        self._retry_delay_sec = retry_delay_sec

    @property
    def retry_logic(self):
        """
        Gets the retry_logic of this WorkflowTaskMeta.
        A logic which defines the way to handle retry (FIXED, EXPONENTIAL_BACKOFF).

        :return: The retry_logic of this WorkflowTaskMeta.
        :rtype: str
        """
        return self._retry_logic

    @retry_logic.setter
    def retry_logic(self, retry_logic):
        """
        Sets the retry_logic of this WorkflowTaskMeta.
        A logic which defines the way to handle retry (FIXED, EXPONENTIAL_BACKOFF).

        :param retry_logic: The retry_logic of this WorkflowTaskMeta.
        :type: str
        """

        self._retry_logic = retry_logic

    @property
    def src(self):
        """
        Gets the src of this WorkflowTaskMeta.
        A service owns the task metadata.

        :return: The src of this WorkflowTaskMeta.
        :rtype: str
        """
        return self._src

    @src.setter
    def src(self, src):
        """
        Sets the src of this WorkflowTaskMeta.
        A service owns the task metadata.

        :param src: The src of this WorkflowTaskMeta.
        :type: str
        """

        self._src = src

    @property
    def timeout_policy(self):
        """
        Gets the timeout_policy of this WorkflowTaskMeta.
        A policy which defines the way to handle timeout (RETRY, TIME_OUT_WF, ALERT_ONLY).

        :return: The timeout_policy of this WorkflowTaskMeta.
        :rtype: str
        """
        return self._timeout_policy

    @timeout_policy.setter
    def timeout_policy(self, timeout_policy):
        """
        Sets the timeout_policy of this WorkflowTaskMeta.
        A policy which defines the way to handle timeout (RETRY, TIME_OUT_WF, ALERT_ONLY).

        :param timeout_policy: The timeout_policy of this WorkflowTaskMeta.
        :type: str
        """

        self._timeout_policy = timeout_policy

    @property
    def timeout_sec(self):
        """
        Gets the timeout_sec of this WorkflowTaskMeta.
        A timeout value for the task in seconds.

        :return: The timeout_sec of this WorkflowTaskMeta.
        :rtype: int
        """
        return self._timeout_sec

    @timeout_sec.setter
    def timeout_sec(self, timeout_sec):
        """
        Sets the timeout_sec of this WorkflowTaskMeta.
        A timeout value for the task in seconds.

        :param timeout_sec: The timeout_sec of this WorkflowTaskMeta.
        :type: int
        """

        self._timeout_sec = timeout_sec

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, WorkflowTaskMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
