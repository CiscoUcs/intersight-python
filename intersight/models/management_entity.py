# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-255
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ManagementEntity(object):
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
        'ancestors': 'list[MoBaseMoRef]',
        'create_time': 'datetime',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'parent': 'MoBaseMoRef',
        'tags': 'list[MoTag]',
        'version_context': 'MoVersionContext',
        'device_mo_id': 'str',
        'dn': 'str',
        'rn': 'str',
        'entity_id': 'str',
        'leadership': 'str',
        'network_element': 'NetworkElementRef',
        'registered_device': 'AssetDeviceRegistrationRef'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'ancestors': 'Ancestors',
        'create_time': 'CreateTime',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'parent': 'Parent',
        'tags': 'Tags',
        'version_context': 'VersionContext',
        'device_mo_id': 'DeviceMoId',
        'dn': 'Dn',
        'rn': 'Rn',
        'entity_id': 'EntityId',
        'leadership': 'Leadership',
        'network_element': 'NetworkElement',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, device_mo_id=None, dn=None, rn=None, entity_id=None, leadership=None, network_element=None, registered_device=None):
        """
        ManagementEntity - a model defined in Swagger
        """

        self._account_moid = None
        self._ancestors = None
        self._create_time = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._parent = None
        self._tags = None
        self._version_context = None
        self._device_mo_id = None
        self._dn = None
        self._rn = None
        self._entity_id = None
        self._leadership = None
        self._network_element = None
        self._registered_device = None

        if account_moid is not None:
          self.account_moid = account_moid
        if ancestors is not None:
          self.ancestors = ancestors
        if create_time is not None:
          self.create_time = create_time
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if parent is not None:
          self.parent = parent
        if tags is not None:
          self.tags = tags
        if version_context is not None:
          self.version_context = version_context
        if device_mo_id is not None:
          self.device_mo_id = device_mo_id
        if dn is not None:
          self.dn = dn
        if rn is not None:
          self.rn = rn
        if entity_id is not None:
          self.entity_id = entity_id
        if leadership is not None:
          self.leadership = leadership
        if network_element is not None:
          self.network_element = network_element
        if registered_device is not None:
          self.registered_device = registered_device

    @property
    def account_moid(self):
        """
        Gets the account_moid of this ManagementEntity.
        The Account ID for this managed object.  

        :return: The account_moid of this ManagementEntity.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this ManagementEntity.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this ManagementEntity.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this ManagementEntity.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this ManagementEntity.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this ManagementEntity.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this ManagementEntity.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this ManagementEntity.
        The time when this managed object was created.  

        :return: The create_time of this ManagementEntity.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this ManagementEntity.
        The time when this managed object was created.  

        :param create_time: The create_time of this ManagementEntity.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this ManagementEntity.
        The time when this managed object was last modified.  

        :return: The mod_time of this ManagementEntity.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this ManagementEntity.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this ManagementEntity.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this ManagementEntity.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this ManagementEntity.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this ManagementEntity.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this ManagementEntity.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this ManagementEntity.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this ManagementEntity.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this ManagementEntity.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this ManagementEntity.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this ManagementEntity.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this ManagementEntity.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this ManagementEntity.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this ManagementEntity.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this ManagementEntity.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this ManagementEntity.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this ManagementEntity.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this ManagementEntity.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this ManagementEntity.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this ManagementEntity.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ManagementEntity.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this ManagementEntity.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this ManagementEntity.
        The versioning info for this managed object   

        :return: The version_context of this ManagementEntity.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this ManagementEntity.
        The versioning info for this managed object   

        :param version_context: The version_context of this ManagementEntity.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this ManagementEntity.

        :return: The device_mo_id of this ManagementEntity.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this ManagementEntity.

        :param device_mo_id: The device_mo_id of this ManagementEntity.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this ManagementEntity.

        :return: The dn of this ManagementEntity.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this ManagementEntity.

        :param dn: The dn of this ManagementEntity.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this ManagementEntity.

        :return: The rn of this ManagementEntity.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this ManagementEntity.

        :param rn: The rn of this ManagementEntity.
        :type: str
        """

        self._rn = rn

    @property
    def entity_id(self):
        """
        Gets the entity_id of this ManagementEntity.

        :return: The entity_id of this ManagementEntity.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this ManagementEntity.

        :param entity_id: The entity_id of this ManagementEntity.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def leadership(self):
        """
        Gets the leadership of this ManagementEntity.

        :return: The leadership of this ManagementEntity.
        :rtype: str
        """
        return self._leadership

    @leadership.setter
    def leadership(self, leadership):
        """
        Sets the leadership of this ManagementEntity.

        :param leadership: The leadership of this ManagementEntity.
        :type: str
        """

        self._leadership = leadership

    @property
    def network_element(self):
        """
        Gets the network_element of this ManagementEntity.

        :return: The network_element of this ManagementEntity.
        :rtype: NetworkElementRef
        """
        return self._network_element

    @network_element.setter
    def network_element(self, network_element):
        """
        Sets the network_element of this ManagementEntity.

        :param network_element: The network_element of this ManagementEntity.
        :type: NetworkElementRef
        """

        self._network_element = network_element

    @property
    def registered_device(self):
        """
        Gets the registered_device of this ManagementEntity.

        :return: The registered_device of this ManagementEntity.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this ManagementEntity.

        :param registered_device: The registered_device of this ManagementEntity.
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
        if not isinstance(other, ManagementEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
