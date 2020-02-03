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


class NiatelemetryNiaInventory(object):
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
        'cpu': 'float',
        'crash_reset_logs': 'str',
        'device_name': 'str',
        'device_type': 'str',
        'disk': 'NiatelemetryDiskinfo',
        'log_in_time': 'str',
        'log_out_time': 'str',
        'memory': 'int',
        'record_type': 'str',
        'record_version': 'str',
        'serial': 'str',
        'software_download': 'str',
        'version': 'str',
        'license_state': 'NiatelemetryNiaLicenseStateRef',
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
        'cpu': 'Cpu',
        'crash_reset_logs': 'CrashResetLogs',
        'device_name': 'DeviceName',
        'device_type': 'DeviceType',
        'disk': 'Disk',
        'log_in_time': 'LogInTime',
        'log_out_time': 'LogOutTime',
        'memory': 'Memory',
        'record_type': 'RecordType',
        'record_version': 'RecordVersion',
        'serial': 'Serial',
        'software_download': 'SoftwareDownload',
        'version': 'Version',
        'license_state': 'LicenseState',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, cpu=None, crash_reset_logs=None, device_name=None, device_type=None, disk=None, log_in_time=None, log_out_time=None, memory=None, record_type=None, record_version=None, serial=None, software_download=None, version=None, license_state=None, registered_device=None):
        """
        NiatelemetryNiaInventory - a model defined in Swagger
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
        self._cpu = None
        self._crash_reset_logs = None
        self._device_name = None
        self._device_type = None
        self._disk = None
        self._log_in_time = None
        self._log_out_time = None
        self._memory = None
        self._record_type = None
        self._record_version = None
        self._serial = None
        self._software_download = None
        self._version = None
        self._license_state = None
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
        if cpu is not None:
          self.cpu = cpu
        if crash_reset_logs is not None:
          self.crash_reset_logs = crash_reset_logs
        if device_name is not None:
          self.device_name = device_name
        if device_type is not None:
          self.device_type = device_type
        if disk is not None:
          self.disk = disk
        if log_in_time is not None:
          self.log_in_time = log_in_time
        if log_out_time is not None:
          self.log_out_time = log_out_time
        if memory is not None:
          self.memory = memory
        if record_type is not None:
          self.record_type = record_type
        if record_version is not None:
          self.record_version = record_version
        if serial is not None:
          self.serial = serial
        if software_download is not None:
          self.software_download = software_download
        if version is not None:
          self.version = version
        if license_state is not None:
          self.license_state = license_state
        if registered_device is not None:
          self.registered_device = registered_device

    @property
    def account_moid(self):
        """
        Gets the account_moid of this NiatelemetryNiaInventory.
        The Account ID for this managed object.  

        :return: The account_moid of this NiatelemetryNiaInventory.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this NiatelemetryNiaInventory.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this NiatelemetryNiaInventory.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this NiatelemetryNiaInventory.
        The time when this managed object was created.  

        :return: The create_time of this NiatelemetryNiaInventory.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this NiatelemetryNiaInventory.
        The time when this managed object was created.  

        :param create_time: The create_time of this NiatelemetryNiaInventory.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this NiatelemetryNiaInventory.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this NiatelemetryNiaInventory.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this NiatelemetryNiaInventory.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this NiatelemetryNiaInventory.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this NiatelemetryNiaInventory.
        The time when this managed object was last modified.  

        :return: The mod_time of this NiatelemetryNiaInventory.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this NiatelemetryNiaInventory.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this NiatelemetryNiaInventory.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this NiatelemetryNiaInventory.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this NiatelemetryNiaInventory.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this NiatelemetryNiaInventory.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this NiatelemetryNiaInventory.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this NiatelemetryNiaInventory.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this NiatelemetryNiaInventory.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this NiatelemetryNiaInventory.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this NiatelemetryNiaInventory.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this NiatelemetryNiaInventory.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this NiatelemetryNiaInventory.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this NiatelemetryNiaInventory.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this NiatelemetryNiaInventory.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this NiatelemetryNiaInventory.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this NiatelemetryNiaInventory.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this NiatelemetryNiaInventory.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this NiatelemetryNiaInventory.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this NiatelemetryNiaInventory.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this NiatelemetryNiaInventory.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this NiatelemetryNiaInventory.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this NiatelemetryNiaInventory.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this NiatelemetryNiaInventory.
        The versioning info for this managed object.   

        :return: The version_context of this NiatelemetryNiaInventory.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this NiatelemetryNiaInventory.
        The versioning info for this managed object.   

        :param version_context: The version_context of this NiatelemetryNiaInventory.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this NiatelemetryNiaInventory.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this NiatelemetryNiaInventory.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this NiatelemetryNiaInventory.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this NiatelemetryNiaInventory.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this NiatelemetryNiaInventory.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this NiatelemetryNiaInventory.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this NiatelemetryNiaInventory.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this NiatelemetryNiaInventory.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this NiatelemetryNiaInventory.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this NiatelemetryNiaInventory.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this NiatelemetryNiaInventory.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this NiatelemetryNiaInventory.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def cpu(self):
        """
        Gets the cpu of this NiatelemetryNiaInventory.
        CPU usage of device being inventoried.  

        :return: The cpu of this NiatelemetryNiaInventory.
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """
        Sets the cpu of this NiatelemetryNiaInventory.
        CPU usage of device being inventoried.  

        :param cpu: The cpu of this NiatelemetryNiaInventory.
        :type: float
        """

        self._cpu = cpu

    @property
    def crash_reset_logs(self):
        """
        Gets the crash_reset_logs of this NiatelemetryNiaInventory.
        Last crash reset reason of device being inventoried.  

        :return: The crash_reset_logs of this NiatelemetryNiaInventory.
        :rtype: str
        """
        return self._crash_reset_logs

    @crash_reset_logs.setter
    def crash_reset_logs(self, crash_reset_logs):
        """
        Sets the crash_reset_logs of this NiatelemetryNiaInventory.
        Last crash reset reason of device being inventoried.  

        :param crash_reset_logs: The crash_reset_logs of this NiatelemetryNiaInventory.
        :type: str
        """

        self._crash_reset_logs = crash_reset_logs

    @property
    def device_name(self):
        """
        Gets the device_name of this NiatelemetryNiaInventory.
        Name of device being inventoried.  

        :return: The device_name of this NiatelemetryNiaInventory.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """
        Sets the device_name of this NiatelemetryNiaInventory.
        Name of device being inventoried.  

        :param device_name: The device_name of this NiatelemetryNiaInventory.
        :type: str
        """

        self._device_name = device_name

    @property
    def device_type(self):
        """
        Gets the device_type of this NiatelemetryNiaInventory.
        Type of device being inventoried.  

        :return: The device_type of this NiatelemetryNiaInventory.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """
        Sets the device_type of this NiatelemetryNiaInventory.
        Type of device being inventoried.  

        :param device_type: The device_type of this NiatelemetryNiaInventory.
        :type: str
        """

        self._device_type = device_type

    @property
    def disk(self):
        """
        Gets the disk of this NiatelemetryNiaInventory.
        Disk Usage of device being inventoried.  

        :return: The disk of this NiatelemetryNiaInventory.
        :rtype: NiatelemetryDiskinfo
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """
        Sets the disk of this NiatelemetryNiaInventory.
        Disk Usage of device being inventoried.  

        :param disk: The disk of this NiatelemetryNiaInventory.
        :type: NiatelemetryDiskinfo
        """

        self._disk = disk

    @property
    def log_in_time(self):
        """
        Gets the log_in_time of this NiatelemetryNiaInventory.
        Last log in time device being inventoried.  

        :return: The log_in_time of this NiatelemetryNiaInventory.
        :rtype: str
        """
        return self._log_in_time

    @log_in_time.setter
    def log_in_time(self, log_in_time):
        """
        Sets the log_in_time of this NiatelemetryNiaInventory.
        Last log in time device being inventoried.  

        :param log_in_time: The log_in_time of this NiatelemetryNiaInventory.
        :type: str
        """

        self._log_in_time = log_in_time

    @property
    def log_out_time(self):
        """
        Gets the log_out_time of this NiatelemetryNiaInventory.
        Last log out time of device being inventoried.  

        :return: The log_out_time of this NiatelemetryNiaInventory.
        :rtype: str
        """
        return self._log_out_time

    @log_out_time.setter
    def log_out_time(self, log_out_time):
        """
        Sets the log_out_time of this NiatelemetryNiaInventory.
        Last log out time of device being inventoried.  

        :param log_out_time: The log_out_time of this NiatelemetryNiaInventory.
        :type: str
        """

        self._log_out_time = log_out_time

    @property
    def memory(self):
        """
        Gets the memory of this NiatelemetryNiaInventory.
        Memory usage of device being inventoried.  

        :return: The memory of this NiatelemetryNiaInventory.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """
        Sets the memory of this NiatelemetryNiaInventory.
        Memory usage of device being inventoried.  

        :param memory: The memory of this NiatelemetryNiaInventory.
        :type: int
        """

        self._memory = memory

    @property
    def record_type(self):
        """
        Gets the record_type of this NiatelemetryNiaInventory.
        Type of record DCNM / APIC / SE.  

        :return: The record_type of this NiatelemetryNiaInventory.
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """
        Sets the record_type of this NiatelemetryNiaInventory.
        Type of record DCNM / APIC / SE.  

        :param record_type: The record_type of this NiatelemetryNiaInventory.
        :type: str
        """

        self._record_type = record_type

    @property
    def record_version(self):
        """
        Gets the record_version of this NiatelemetryNiaInventory.
        Version of record being pushed.  

        :return: The record_version of this NiatelemetryNiaInventory.
        :rtype: str
        """
        return self._record_version

    @record_version.setter
    def record_version(self, record_version):
        """
        Sets the record_version of this NiatelemetryNiaInventory.
        Version of record being pushed.  

        :param record_version: The record_version of this NiatelemetryNiaInventory.
        :type: str
        """

        self._record_version = record_version

    @property
    def serial(self):
        """
        Gets the serial of this NiatelemetryNiaInventory.
        Serial number of device being invetoried.  

        :return: The serial of this NiatelemetryNiaInventory.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this NiatelemetryNiaInventory.
        Serial number of device being invetoried.  

        :param serial: The serial of this NiatelemetryNiaInventory.
        :type: str
        """

        self._serial = serial

    @property
    def software_download(self):
        """
        Gets the software_download of this NiatelemetryNiaInventory.
        Last software downloaded of device being inventoried.  

        :return: The software_download of this NiatelemetryNiaInventory.
        :rtype: str
        """
        return self._software_download

    @software_download.setter
    def software_download(self, software_download):
        """
        Sets the software_download of this NiatelemetryNiaInventory.
        Last software downloaded of device being inventoried.  

        :param software_download: The software_download of this NiatelemetryNiaInventory.
        :type: str
        """

        self._software_download = software_download

    @property
    def version(self):
        """
        Gets the version of this NiatelemetryNiaInventory.
        Software version of device being inventoried.   

        :return: The version of this NiatelemetryNiaInventory.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this NiatelemetryNiaInventory.
        Software version of device being inventoried.   

        :param version: The version of this NiatelemetryNiaInventory.
        :type: str
        """

        self._version = version

    @property
    def license_state(self):
        """
        Gets the license_state of this NiatelemetryNiaInventory.
        The license of this device. 

        :return: The license_state of this NiatelemetryNiaInventory.
        :rtype: NiatelemetryNiaLicenseStateRef
        """
        return self._license_state

    @license_state.setter
    def license_state(self, license_state):
        """
        Sets the license_state of this NiatelemetryNiaInventory.
        The license of this device. 

        :param license_state: The license_state of this NiatelemetryNiaInventory.
        :type: NiatelemetryNiaLicenseStateRef
        """

        self._license_state = license_state

    @property
    def registered_device(self):
        """
        Gets the registered_device of this NiatelemetryNiaInventory.
        Relationship to the Device Registration object for this setup. 

        :return: The registered_device of this NiatelemetryNiaInventory.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this NiatelemetryNiaInventory.
        Relationship to the Device Registration object for this setup. 

        :param registered_device: The registered_device of this NiatelemetryNiaInventory.
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
        if not isinstance(other, NiatelemetryNiaInventory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
