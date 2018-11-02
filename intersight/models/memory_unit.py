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


class MemoryUnit(object):
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
        'model': 'str',
        'revision': 'str',
        'serial': 'str',
        'vendor': 'str',
        'admin_state': 'str',
        'array_id': 'int',
        'bank': 'int',
        'capacity': 'str',
        'clock': 'str',
        'form_factor': 'str',
        'latency': 'str',
        'location': 'str',
        'memory_array': 'MemoryArrayRef',
        'memory_id': 'int',
        'oper_power_state': 'str',
        'oper_state': 'str',
        'operability': 'str',
        'presence': 'str',
        'registered_device': 'AssetDeviceRegistrationRef',
        'set': 'int',
        'speed': 'str',
        'thermal': 'str',
        'type': 'str',
        'visibility': 'str',
        'width': 'str'
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
        'model': 'Model',
        'revision': 'Revision',
        'serial': 'Serial',
        'vendor': 'Vendor',
        'admin_state': 'AdminState',
        'array_id': 'ArrayId',
        'bank': 'Bank',
        'capacity': 'Capacity',
        'clock': 'Clock',
        'form_factor': 'FormFactor',
        'latency': 'Latency',
        'location': 'Location',
        'memory_array': 'MemoryArray',
        'memory_id': 'MemoryId',
        'oper_power_state': 'OperPowerState',
        'oper_state': 'OperState',
        'operability': 'Operability',
        'presence': 'Presence',
        'registered_device': 'RegisteredDevice',
        'set': 'Set',
        'speed': 'Speed',
        'thermal': 'Thermal',
        'type': 'Type',
        'visibility': 'Visibility',
        'width': 'Width'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, admin_state=None, array_id=None, bank=None, capacity=None, clock=None, form_factor=None, latency=None, location=None, memory_array=None, memory_id=None, oper_power_state=None, oper_state=None, operability=None, presence=None, registered_device=None, set=None, speed=None, thermal=None, type=None, visibility=None, width=None):
        """
        MemoryUnit - a model defined in Swagger
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
        self._model = None
        self._revision = None
        self._serial = None
        self._vendor = None
        self._admin_state = None
        self._array_id = None
        self._bank = None
        self._capacity = None
        self._clock = None
        self._form_factor = None
        self._latency = None
        self._location = None
        self._memory_array = None
        self._memory_id = None
        self._oper_power_state = None
        self._oper_state = None
        self._operability = None
        self._presence = None
        self._registered_device = None
        self._set = None
        self._speed = None
        self._thermal = None
        self._type = None
        self._visibility = None
        self._width = None

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
        if model is not None:
          self.model = model
        if revision is not None:
          self.revision = revision
        if serial is not None:
          self.serial = serial
        if vendor is not None:
          self.vendor = vendor
        if admin_state is not None:
          self.admin_state = admin_state
        if array_id is not None:
          self.array_id = array_id
        if bank is not None:
          self.bank = bank
        if capacity is not None:
          self.capacity = capacity
        if clock is not None:
          self.clock = clock
        if form_factor is not None:
          self.form_factor = form_factor
        if latency is not None:
          self.latency = latency
        if location is not None:
          self.location = location
        if memory_array is not None:
          self.memory_array = memory_array
        if memory_id is not None:
          self.memory_id = memory_id
        if oper_power_state is not None:
          self.oper_power_state = oper_power_state
        if oper_state is not None:
          self.oper_state = oper_state
        if operability is not None:
          self.operability = operability
        if presence is not None:
          self.presence = presence
        if registered_device is not None:
          self.registered_device = registered_device
        if set is not None:
          self.set = set
        if speed is not None:
          self.speed = speed
        if thermal is not None:
          self.thermal = thermal
        if type is not None:
          self.type = type
        if visibility is not None:
          self.visibility = visibility
        if width is not None:
          self.width = width

    @property
    def account_moid(self):
        """
        Gets the account_moid of this MemoryUnit.
        The Account ID for this managed object.  

        :return: The account_moid of this MemoryUnit.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this MemoryUnit.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this MemoryUnit.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this MemoryUnit.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this MemoryUnit.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this MemoryUnit.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this MemoryUnit.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this MemoryUnit.
        The time when this managed object was created.  

        :return: The create_time of this MemoryUnit.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this MemoryUnit.
        The time when this managed object was created.  

        :param create_time: The create_time of this MemoryUnit.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this MemoryUnit.
        The time when this managed object was last modified.  

        :return: The mod_time of this MemoryUnit.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this MemoryUnit.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this MemoryUnit.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this MemoryUnit.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this MemoryUnit.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this MemoryUnit.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this MemoryUnit.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this MemoryUnit.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this MemoryUnit.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this MemoryUnit.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this MemoryUnit.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this MemoryUnit.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this MemoryUnit.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this MemoryUnit.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this MemoryUnit.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this MemoryUnit.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this MemoryUnit.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this MemoryUnit.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this MemoryUnit.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this MemoryUnit.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this MemoryUnit.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this MemoryUnit.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this MemoryUnit.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this MemoryUnit.
        The versioning info for this managed object   

        :return: The version_context of this MemoryUnit.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this MemoryUnit.
        The versioning info for this managed object   

        :param version_context: The version_context of this MemoryUnit.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this MemoryUnit.

        :return: The device_mo_id of this MemoryUnit.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this MemoryUnit.

        :param device_mo_id: The device_mo_id of this MemoryUnit.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this MemoryUnit.

        :return: The dn of this MemoryUnit.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this MemoryUnit.

        :param dn: The dn of this MemoryUnit.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this MemoryUnit.

        :return: The rn of this MemoryUnit.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this MemoryUnit.

        :param rn: The rn of this MemoryUnit.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this MemoryUnit.

        :return: The model of this MemoryUnit.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this MemoryUnit.

        :param model: The model of this MemoryUnit.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this MemoryUnit.

        :return: The revision of this MemoryUnit.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this MemoryUnit.

        :param revision: The revision of this MemoryUnit.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this MemoryUnit.

        :return: The serial of this MemoryUnit.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this MemoryUnit.

        :param serial: The serial of this MemoryUnit.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this MemoryUnit.

        :return: The vendor of this MemoryUnit.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this MemoryUnit.

        :param vendor: The vendor of this MemoryUnit.
        :type: str
        """

        self._vendor = vendor

    @property
    def admin_state(self):
        """
        Gets the admin_state of this MemoryUnit.

        :return: The admin_state of this MemoryUnit.
        :rtype: str
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """
        Sets the admin_state of this MemoryUnit.

        :param admin_state: The admin_state of this MemoryUnit.
        :type: str
        """

        self._admin_state = admin_state

    @property
    def array_id(self):
        """
        Gets the array_id of this MemoryUnit.

        :return: The array_id of this MemoryUnit.
        :rtype: int
        """
        return self._array_id

    @array_id.setter
    def array_id(self, array_id):
        """
        Sets the array_id of this MemoryUnit.

        :param array_id: The array_id of this MemoryUnit.
        :type: int
        """

        self._array_id = array_id

    @property
    def bank(self):
        """
        Gets the bank of this MemoryUnit.

        :return: The bank of this MemoryUnit.
        :rtype: int
        """
        return self._bank

    @bank.setter
    def bank(self, bank):
        """
        Sets the bank of this MemoryUnit.

        :param bank: The bank of this MemoryUnit.
        :type: int
        """

        self._bank = bank

    @property
    def capacity(self):
        """
        Gets the capacity of this MemoryUnit.

        :return: The capacity of this MemoryUnit.
        :rtype: str
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this MemoryUnit.

        :param capacity: The capacity of this MemoryUnit.
        :type: str
        """

        self._capacity = capacity

    @property
    def clock(self):
        """
        Gets the clock of this MemoryUnit.

        :return: The clock of this MemoryUnit.
        :rtype: str
        """
        return self._clock

    @clock.setter
    def clock(self, clock):
        """
        Sets the clock of this MemoryUnit.

        :param clock: The clock of this MemoryUnit.
        :type: str
        """

        self._clock = clock

    @property
    def form_factor(self):
        """
        Gets the form_factor of this MemoryUnit.

        :return: The form_factor of this MemoryUnit.
        :rtype: str
        """
        return self._form_factor

    @form_factor.setter
    def form_factor(self, form_factor):
        """
        Sets the form_factor of this MemoryUnit.

        :param form_factor: The form_factor of this MemoryUnit.
        :type: str
        """

        self._form_factor = form_factor

    @property
    def latency(self):
        """
        Gets the latency of this MemoryUnit.

        :return: The latency of this MemoryUnit.
        :rtype: str
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """
        Sets the latency of this MemoryUnit.

        :param latency: The latency of this MemoryUnit.
        :type: str
        """

        self._latency = latency

    @property
    def location(self):
        """
        Gets the location of this MemoryUnit.

        :return: The location of this MemoryUnit.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this MemoryUnit.

        :param location: The location of this MemoryUnit.
        :type: str
        """

        self._location = location

    @property
    def memory_array(self):
        """
        Gets the memory_array of this MemoryUnit.

        :return: The memory_array of this MemoryUnit.
        :rtype: MemoryArrayRef
        """
        return self._memory_array

    @memory_array.setter
    def memory_array(self, memory_array):
        """
        Sets the memory_array of this MemoryUnit.

        :param memory_array: The memory_array of this MemoryUnit.
        :type: MemoryArrayRef
        """

        self._memory_array = memory_array

    @property
    def memory_id(self):
        """
        Gets the memory_id of this MemoryUnit.

        :return: The memory_id of this MemoryUnit.
        :rtype: int
        """
        return self._memory_id

    @memory_id.setter
    def memory_id(self, memory_id):
        """
        Sets the memory_id of this MemoryUnit.

        :param memory_id: The memory_id of this MemoryUnit.
        :type: int
        """

        self._memory_id = memory_id

    @property
    def oper_power_state(self):
        """
        Gets the oper_power_state of this MemoryUnit.

        :return: The oper_power_state of this MemoryUnit.
        :rtype: str
        """
        return self._oper_power_state

    @oper_power_state.setter
    def oper_power_state(self, oper_power_state):
        """
        Sets the oper_power_state of this MemoryUnit.

        :param oper_power_state: The oper_power_state of this MemoryUnit.
        :type: str
        """

        self._oper_power_state = oper_power_state

    @property
    def oper_state(self):
        """
        Gets the oper_state of this MemoryUnit.

        :return: The oper_state of this MemoryUnit.
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """
        Sets the oper_state of this MemoryUnit.

        :param oper_state: The oper_state of this MemoryUnit.
        :type: str
        """

        self._oper_state = oper_state

    @property
    def operability(self):
        """
        Gets the operability of this MemoryUnit.

        :return: The operability of this MemoryUnit.
        :rtype: str
        """
        return self._operability

    @operability.setter
    def operability(self, operability):
        """
        Sets the operability of this MemoryUnit.

        :param operability: The operability of this MemoryUnit.
        :type: str
        """

        self._operability = operability

    @property
    def presence(self):
        """
        Gets the presence of this MemoryUnit.

        :return: The presence of this MemoryUnit.
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """
        Sets the presence of this MemoryUnit.

        :param presence: The presence of this MemoryUnit.
        :type: str
        """

        self._presence = presence

    @property
    def registered_device(self):
        """
        Gets the registered_device of this MemoryUnit.

        :return: The registered_device of this MemoryUnit.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this MemoryUnit.

        :param registered_device: The registered_device of this MemoryUnit.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def set(self):
        """
        Gets the set of this MemoryUnit.

        :return: The set of this MemoryUnit.
        :rtype: int
        """
        return self._set

    @set.setter
    def set(self, set):
        """
        Sets the set of this MemoryUnit.

        :param set: The set of this MemoryUnit.
        :type: int
        """

        self._set = set

    @property
    def speed(self):
        """
        Gets the speed of this MemoryUnit.

        :return: The speed of this MemoryUnit.
        :rtype: str
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """
        Sets the speed of this MemoryUnit.

        :param speed: The speed of this MemoryUnit.
        :type: str
        """

        self._speed = speed

    @property
    def thermal(self):
        """
        Gets the thermal of this MemoryUnit.

        :return: The thermal of this MemoryUnit.
        :rtype: str
        """
        return self._thermal

    @thermal.setter
    def thermal(self, thermal):
        """
        Sets the thermal of this MemoryUnit.

        :param thermal: The thermal of this MemoryUnit.
        :type: str
        """

        self._thermal = thermal

    @property
    def type(self):
        """
        Gets the type of this MemoryUnit.

        :return: The type of this MemoryUnit.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MemoryUnit.

        :param type: The type of this MemoryUnit.
        :type: str
        """

        self._type = type

    @property
    def visibility(self):
        """
        Gets the visibility of this MemoryUnit.

        :return: The visibility of this MemoryUnit.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """
        Sets the visibility of this MemoryUnit.

        :param visibility: The visibility of this MemoryUnit.
        :type: str
        """

        self._visibility = visibility

    @property
    def width(self):
        """
        Gets the width of this MemoryUnit.

        :return: The width of this MemoryUnit.
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this MemoryUnit.

        :param width: The width of this MemoryUnit.
        :type: str
        """

        self._width = width

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
        if not isinstance(other, MemoryUnit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
