# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1295
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class MemoryPersistentMemoryNamespace(object):
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
        'device_mo_id': 'str',
        'dn': 'str',
        'rn': 'str',
        'capacity': 'str',
        'health_state': 'str',
        'label_version': 'str',
        'mode': 'str',
        'name': 'str',
        'uuid': 'str',
        'memory_persistent_memory_region': 'MemoryPersistentMemoryRegionRef',
        'registered_device': 'AssetDeviceRegistrationRef'
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
        'device_mo_id': 'DeviceMoId',
        'dn': 'Dn',
        'rn': 'Rn',
        'capacity': 'Capacity',
        'health_state': 'HealthState',
        'label_version': 'LabelVersion',
        'mode': 'Mode',
        'name': 'Name',
        'uuid': 'Uuid',
        'memory_persistent_memory_region': 'MemoryPersistentMemoryRegion',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, device_mo_id=None, dn=None, rn=None, capacity=None, health_state=None, label_version=None, mode=None, name=None, uuid=None, memory_persistent_memory_region=None, registered_device=None):
        """
        MemoryPersistentMemoryNamespace - a model defined in Swagger
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
        self._device_mo_id = None
        self._dn = None
        self._rn = None
        self._capacity = None
        self._health_state = None
        self._label_version = None
        self._mode = None
        self._name = None
        self._uuid = None
        self._memory_persistent_memory_region = None
        self._registered_device = None

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
        if device_mo_id is not None:
          self.device_mo_id = device_mo_id
        if dn is not None:
          self.dn = dn
        if rn is not None:
          self.rn = rn
        if capacity is not None:
          self.capacity = capacity
        if health_state is not None:
          self.health_state = health_state
        if label_version is not None:
          self.label_version = label_version
        if mode is not None:
          self.mode = mode
        if name is not None:
          self.name = name
        if uuid is not None:
          self.uuid = uuid
        if memory_persistent_memory_region is not None:
          self.memory_persistent_memory_region = memory_persistent_memory_region
        if registered_device is not None:
          self.registered_device = registered_device

    @property
    def account_moid(self):
        """
        Gets the account_moid of this MemoryPersistentMemoryNamespace.
        The Account ID for this managed object.  

        :return: The account_moid of this MemoryPersistentMemoryNamespace.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this MemoryPersistentMemoryNamespace.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this MemoryPersistentMemoryNamespace.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this MemoryPersistentMemoryNamespace.
        The time when this managed object was created.  

        :return: The create_time of this MemoryPersistentMemoryNamespace.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this MemoryPersistentMemoryNamespace.
        The time when this managed object was created.  

        :param create_time: The create_time of this MemoryPersistentMemoryNamespace.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this MemoryPersistentMemoryNamespace.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this MemoryPersistentMemoryNamespace.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this MemoryPersistentMemoryNamespace.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this MemoryPersistentMemoryNamespace.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this MemoryPersistentMemoryNamespace.
        The time when this managed object was last modified.  

        :return: The mod_time of this MemoryPersistentMemoryNamespace.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this MemoryPersistentMemoryNamespace.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this MemoryPersistentMemoryNamespace.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this MemoryPersistentMemoryNamespace.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this MemoryPersistentMemoryNamespace.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this MemoryPersistentMemoryNamespace.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this MemoryPersistentMemoryNamespace.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this MemoryPersistentMemoryNamespace.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this MemoryPersistentMemoryNamespace.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this MemoryPersistentMemoryNamespace.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this MemoryPersistentMemoryNamespace.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this MemoryPersistentMemoryNamespace.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this MemoryPersistentMemoryNamespace.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this MemoryPersistentMemoryNamespace.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this MemoryPersistentMemoryNamespace.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this MemoryPersistentMemoryNamespace.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this MemoryPersistentMemoryNamespace.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this MemoryPersistentMemoryNamespace.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this MemoryPersistentMemoryNamespace.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this MemoryPersistentMemoryNamespace.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this MemoryPersistentMemoryNamespace.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this MemoryPersistentMemoryNamespace.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this MemoryPersistentMemoryNamespace.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this MemoryPersistentMemoryNamespace.
        The versioning info for this managed object.   

        :return: The version_context of this MemoryPersistentMemoryNamespace.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this MemoryPersistentMemoryNamespace.
        The versioning info for this managed object.   

        :param version_context: The version_context of this MemoryPersistentMemoryNamespace.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this MemoryPersistentMemoryNamespace.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this MemoryPersistentMemoryNamespace.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this MemoryPersistentMemoryNamespace.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this MemoryPersistentMemoryNamespace.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this MemoryPersistentMemoryNamespace.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this MemoryPersistentMemoryNamespace.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this MemoryPersistentMemoryNamespace.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this MemoryPersistentMemoryNamespace.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this MemoryPersistentMemoryNamespace.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this MemoryPersistentMemoryNamespace.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this MemoryPersistentMemoryNamespace.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this MemoryPersistentMemoryNamespace.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this MemoryPersistentMemoryNamespace.

        :return: The device_mo_id of this MemoryPersistentMemoryNamespace.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this MemoryPersistentMemoryNamespace.

        :param device_mo_id: The device_mo_id of this MemoryPersistentMemoryNamespace.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this MemoryPersistentMemoryNamespace.
        The Distinguished Name unambiguously identifies an object in the system.  

        :return: The dn of this MemoryPersistentMemoryNamespace.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this MemoryPersistentMemoryNamespace.
        The Distinguished Name unambiguously identifies an object in the system.  

        :param dn: The dn of this MemoryPersistentMemoryNamespace.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this MemoryPersistentMemoryNamespace.
        The Relative Name uniquely identifies an object within a given context.   

        :return: The rn of this MemoryPersistentMemoryNamespace.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this MemoryPersistentMemoryNamespace.
        The Relative Name uniquely identifies an object within a given context.   

        :param rn: The rn of this MemoryPersistentMemoryNamespace.
        :type: str
        """

        self._rn = rn

    @property
    def capacity(self):
        """
        Gets the capacity of this MemoryPersistentMemoryNamespace.
        This represents the capacity in GB of a Persistent Memory Namespace.  

        :return: The capacity of this MemoryPersistentMemoryNamespace.
        :rtype: str
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this MemoryPersistentMemoryNamespace.
        This represents the capacity in GB of a Persistent Memory Namespace.  

        :param capacity: The capacity of this MemoryPersistentMemoryNamespace.
        :type: str
        """

        self._capacity = capacity

    @property
    def health_state(self):
        """
        Gets the health_state of this MemoryPersistentMemoryNamespace.
        This represents the health state of a Persistent Memory Namespace.  

        :return: The health_state of this MemoryPersistentMemoryNamespace.
        :rtype: str
        """
        return self._health_state

    @health_state.setter
    def health_state(self, health_state):
        """
        Sets the health_state of this MemoryPersistentMemoryNamespace.
        This represents the health state of a Persistent Memory Namespace.  

        :param health_state: The health_state of this MemoryPersistentMemoryNamespace.
        :type: str
        """

        self._health_state = health_state

    @property
    def label_version(self):
        """
        Gets the label_version of this MemoryPersistentMemoryNamespace.
        This represents the label version of a Persistent Memory Namespace.  

        :return: The label_version of this MemoryPersistentMemoryNamespace.
        :rtype: str
        """
        return self._label_version

    @label_version.setter
    def label_version(self, label_version):
        """
        Sets the label_version of this MemoryPersistentMemoryNamespace.
        This represents the label version of a Persistent Memory Namespace.  

        :param label_version: The label_version of this MemoryPersistentMemoryNamespace.
        :type: str
        """

        self._label_version = label_version

    @property
    def mode(self):
        """
        Gets the mode of this MemoryPersistentMemoryNamespace.
        This represents the mode of a Persistent Memory Namespace.  

        :return: The mode of this MemoryPersistentMemoryNamespace.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this MemoryPersistentMemoryNamespace.
        This represents the mode of a Persistent Memory Namespace.  

        :param mode: The mode of this MemoryPersistentMemoryNamespace.
        :type: str
        """

        self._mode = mode

    @property
    def name(self):
        """
        Gets the name of this MemoryPersistentMemoryNamespace.
        This represents the name of a Persistent Memory Namespace.  

        :return: The name of this MemoryPersistentMemoryNamespace.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MemoryPersistentMemoryNamespace.
        This represents the name of a Persistent Memory Namespace.  

        :param name: The name of this MemoryPersistentMemoryNamespace.
        :type: str
        """

        self._name = name

    @property
    def uuid(self):
        """
        Gets the uuid of this MemoryPersistentMemoryNamespace.
        This represents the uuid of a Persistent Memory Namespace.   

        :return: The uuid of this MemoryPersistentMemoryNamespace.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this MemoryPersistentMemoryNamespace.
        This represents the uuid of a Persistent Memory Namespace.   

        :param uuid: The uuid of this MemoryPersistentMemoryNamespace.
        :type: str
        """

        self._uuid = uuid

    @property
    def memory_persistent_memory_region(self):
        """
        Gets the memory_persistent_memory_region of this MemoryPersistentMemoryNamespace.
        A collection of references to the [memory.PersistentMemoryRegion](mo://memory.PersistentMemoryRegion) Managed Object.  When this managed object is deleted, the referenced [memory.PersistentMemoryRegion](mo://memory.PersistentMemoryRegion) MO unsets its reference to this deleted MO. 

        :return: The memory_persistent_memory_region of this MemoryPersistentMemoryNamespace.
        :rtype: MemoryPersistentMemoryRegionRef
        """
        return self._memory_persistent_memory_region

    @memory_persistent_memory_region.setter
    def memory_persistent_memory_region(self, memory_persistent_memory_region):
        """
        Sets the memory_persistent_memory_region of this MemoryPersistentMemoryNamespace.
        A collection of references to the [memory.PersistentMemoryRegion](mo://memory.PersistentMemoryRegion) Managed Object.  When this managed object is deleted, the referenced [memory.PersistentMemoryRegion](mo://memory.PersistentMemoryRegion) MO unsets its reference to this deleted MO. 

        :param memory_persistent_memory_region: The memory_persistent_memory_region of this MemoryPersistentMemoryNamespace.
        :type: MemoryPersistentMemoryRegionRef
        """

        self._memory_persistent_memory_region = memory_persistent_memory_region

    @property
    def registered_device(self):
        """
        Gets the registered_device of this MemoryPersistentMemoryNamespace.
        The Device to which this Managed Object is associated. 

        :return: The registered_device of this MemoryPersistentMemoryNamespace.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this MemoryPersistentMemoryNamespace.
        The Device to which this Managed Object is associated. 

        :param registered_device: The registered_device of this MemoryPersistentMemoryNamespace.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

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
        if not isinstance(other, MemoryPersistentMemoryNamespace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
