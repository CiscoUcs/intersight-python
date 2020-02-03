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


class BootDeviceBootMode(object):
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
        'configured_boot_mode': 'str',
        'compute_rack_unit': 'ComputeRackUnitRef',
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
        'configured_boot_mode': 'ConfiguredBootMode',
        'compute_rack_unit': 'ComputeRackUnit',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, device_mo_id=None, dn=None, rn=None, configured_boot_mode=None, compute_rack_unit=None, registered_device=None):
        """
        BootDeviceBootMode - a model defined in Swagger
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
        self._configured_boot_mode = None
        self._compute_rack_unit = None
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
        if configured_boot_mode is not None:
          self.configured_boot_mode = configured_boot_mode
        if compute_rack_unit is not None:
          self.compute_rack_unit = compute_rack_unit
        if registered_device is not None:
          self.registered_device = registered_device

    @property
    def account_moid(self):
        """
        Gets the account_moid of this BootDeviceBootMode.
        The Account ID for this managed object.  

        :return: The account_moid of this BootDeviceBootMode.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this BootDeviceBootMode.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this BootDeviceBootMode.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this BootDeviceBootMode.
        The time when this managed object was created.  

        :return: The create_time of this BootDeviceBootMode.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this BootDeviceBootMode.
        The time when this managed object was created.  

        :param create_time: The create_time of this BootDeviceBootMode.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this BootDeviceBootMode.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this BootDeviceBootMode.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this BootDeviceBootMode.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this BootDeviceBootMode.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this BootDeviceBootMode.
        The time when this managed object was last modified.  

        :return: The mod_time of this BootDeviceBootMode.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this BootDeviceBootMode.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this BootDeviceBootMode.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this BootDeviceBootMode.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this BootDeviceBootMode.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this BootDeviceBootMode.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this BootDeviceBootMode.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this BootDeviceBootMode.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this BootDeviceBootMode.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this BootDeviceBootMode.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this BootDeviceBootMode.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this BootDeviceBootMode.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this BootDeviceBootMode.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this BootDeviceBootMode.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this BootDeviceBootMode.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this BootDeviceBootMode.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this BootDeviceBootMode.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this BootDeviceBootMode.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this BootDeviceBootMode.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this BootDeviceBootMode.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this BootDeviceBootMode.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this BootDeviceBootMode.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this BootDeviceBootMode.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this BootDeviceBootMode.
        The versioning info for this managed object.   

        :return: The version_context of this BootDeviceBootMode.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this BootDeviceBootMode.
        The versioning info for this managed object.   

        :param version_context: The version_context of this BootDeviceBootMode.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this BootDeviceBootMode.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this BootDeviceBootMode.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this BootDeviceBootMode.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this BootDeviceBootMode.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this BootDeviceBootMode.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this BootDeviceBootMode.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this BootDeviceBootMode.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this BootDeviceBootMode.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this BootDeviceBootMode.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this BootDeviceBootMode.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this BootDeviceBootMode.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this BootDeviceBootMode.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this BootDeviceBootMode.

        :return: The device_mo_id of this BootDeviceBootMode.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this BootDeviceBootMode.

        :param device_mo_id: The device_mo_id of this BootDeviceBootMode.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this BootDeviceBootMode.
        The Distinguished Name unambiguously identifies an object in the system.  

        :return: The dn of this BootDeviceBootMode.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this BootDeviceBootMode.
        The Distinguished Name unambiguously identifies an object in the system.  

        :param dn: The dn of this BootDeviceBootMode.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this BootDeviceBootMode.
        The Relative Name uniquely identifies an object within a given context.   

        :return: The rn of this BootDeviceBootMode.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this BootDeviceBootMode.
        The Relative Name uniquely identifies an object within a given context.   

        :param rn: The rn of this BootDeviceBootMode.
        :type: str
        """

        self._rn = rn

    @property
    def configured_boot_mode(self):
        """
        Gets the configured_boot_mode of this BootDeviceBootMode.

        :return: The configured_boot_mode of this BootDeviceBootMode.
        :rtype: str
        """
        return self._configured_boot_mode

    @configured_boot_mode.setter
    def configured_boot_mode(self, configured_boot_mode):
        """
        Sets the configured_boot_mode of this BootDeviceBootMode.

        :param configured_boot_mode: The configured_boot_mode of this BootDeviceBootMode.
        :type: str
        """

        self._configured_boot_mode = configured_boot_mode

    @property
    def compute_rack_unit(self):
        """
        Gets the compute_rack_unit of this BootDeviceBootMode.
        A collection of references to the [compute.RackUnit](mo://compute.RackUnit) Managed Object.  When this managed object is deleted, the referenced [compute.RackUnit](mo://compute.RackUnit) MO unsets its reference to this deleted MO. 

        :return: The compute_rack_unit of this BootDeviceBootMode.
        :rtype: ComputeRackUnitRef
        """
        return self._compute_rack_unit

    @compute_rack_unit.setter
    def compute_rack_unit(self, compute_rack_unit):
        """
        Sets the compute_rack_unit of this BootDeviceBootMode.
        A collection of references to the [compute.RackUnit](mo://compute.RackUnit) Managed Object.  When this managed object is deleted, the referenced [compute.RackUnit](mo://compute.RackUnit) MO unsets its reference to this deleted MO. 

        :param compute_rack_unit: The compute_rack_unit of this BootDeviceBootMode.
        :type: ComputeRackUnitRef
        """

        self._compute_rack_unit = compute_rack_unit

    @property
    def registered_device(self):
        """
        Gets the registered_device of this BootDeviceBootMode.
        The Device to which this Managed Object is associated. 

        :return: The registered_device of this BootDeviceBootMode.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this BootDeviceBootMode.
        The Device to which this Managed Object is associated. 

        :param registered_device: The registered_device of this BootDeviceBootMode.
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
        if not isinstance(other, BootDeviceBootMode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
