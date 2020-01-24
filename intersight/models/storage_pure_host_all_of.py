# coding: utf-8
"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations.   # noqa: E501

    The version of the OpenAPI document: 1.0.9-1295
    Contact: intersight@cisco.com
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from intersight.configuration import Configuration


class StoragePureHostAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'host_group_name': 'str',
        'host_names': 'list[str]',
        'storage_utilization': 'StorageHostUtilization',
        'type': 'str',
        'host_group': 'StoragePureHost',
        'hosts': 'list[StoragePureHost]',
        'registered_device': 'AssetDeviceRegistration'
    }

    attribute_map = {
        'host_group_name': 'HostGroupName',
        'host_names': 'HostNames',
        'storage_utilization': 'StorageUtilization',
        'type': 'Type',
        'host_group': 'HostGroup',
        'hosts': 'Hosts',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self,
                 host_group_name=None,
                 host_names=None,
                 storage_utilization=None,
                 type='Host',
                 host_group=None,
                 hosts=None,
                 registered_device=None,
                 local_vars_configuration=None):  # noqa: E501
        """StoragePureHostAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._host_group_name = None
        self._host_names = None
        self._storage_utilization = None
        self._type = None
        self._host_group = None
        self._hosts = None
        self._registered_device = None
        self.discriminator = None

        if host_group_name is not None:
            self.host_group_name = host_group_name
        if host_names is not None:
            self.host_names = host_names
        if storage_utilization is not None:
            self.storage_utilization = storage_utilization
        if type is not None:
            self.type = type
        if host_group is not None:
            self.host_group = host_group
        if hosts is not None:
            self.hosts = hosts
        if registered_device is not None:
            self.registered_device = registered_device

    @property
    def host_group_name(self):
        """Gets the host_group_name of this StoragePureHostAllOf.  # noqa: E501

        Name of host group where the host belongs to. Empty if HostType is set as HostGroup.    # noqa: E501

        :return: The host_group_name of this StoragePureHostAllOf.  # noqa: E501
        :rtype: str
        """
        return self._host_group_name

    @host_group_name.setter
    def host_group_name(self, host_group_name):
        """Sets the host_group_name of this StoragePureHostAllOf.

        Name of host group where the host belongs to. Empty if HostType is set as HostGroup.    # noqa: E501

        :param host_group_name: The host_group_name of this StoragePureHostAllOf.  # noqa: E501
        :type: str
        """

        self._host_group_name = host_group_name

    @property
    def host_names(self):
        """Gets the host_names of this StoragePureHostAllOf.  # noqa: E501


        :return: The host_names of this StoragePureHostAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._host_names

    @host_names.setter
    def host_names(self, host_names):
        """Sets the host_names of this StoragePureHostAllOf.


        :param host_names: The host_names of this StoragePureHostAllOf.  # noqa: E501
        :type: list[str]
        """

        self._host_names = host_names

    @property
    def storage_utilization(self):
        """Gets the storage_utilization of this StoragePureHostAllOf.  # noqa: E501


        :return: The storage_utilization of this StoragePureHostAllOf.  # noqa: E501
        :rtype: StorageHostUtilization
        """
        return self._storage_utilization

    @storage_utilization.setter
    def storage_utilization(self, storage_utilization):
        """Sets the storage_utilization of this StoragePureHostAllOf.


        :param storage_utilization: The storage_utilization of this StoragePureHostAllOf.  # noqa: E501
        :type: StorageHostUtilization
        """

        self._storage_utilization = storage_utilization

    @property
    def type(self):
        """Gets the type of this StoragePureHostAllOf.  # noqa: E501

        Type of host entity whether it is a single host or host group (collection of host).     # noqa: E501

        :return: The type of this StoragePureHostAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StoragePureHostAllOf.

        Type of host entity whether it is a single host or host group (collection of host).     # noqa: E501

        :param type: The type of this StoragePureHostAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["Host", "HostGroup"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values))

        self._type = type

    @property
    def host_group(self):
        """Gets the host_group of this StoragePureHostAllOf.  # noqa: E501


        :return: The host_group of this StoragePureHostAllOf.  # noqa: E501
        :rtype: StoragePureHost
        """
        return self._host_group

    @host_group.setter
    def host_group(self, host_group):
        """Sets the host_group of this StoragePureHostAllOf.


        :param host_group: The host_group of this StoragePureHostAllOf.  # noqa: E501
        :type: StoragePureHost
        """

        self._host_group = host_group

    @property
    def hosts(self):
        """Gets the hosts of this StoragePureHostAllOf.  # noqa: E501

        A reference to a storagePureHost resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of host object associated to the host group.   # noqa: E501

        :return: The hosts of this StoragePureHostAllOf.  # noqa: E501
        :rtype: list[StoragePureHost]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this StoragePureHostAllOf.

        A reference to a storagePureHost resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of host object associated to the host group.   # noqa: E501

        :param hosts: The hosts of this StoragePureHostAllOf.  # noqa: E501
        :type: list[StoragePureHost]
        """

        self._hosts = hosts

    @property
    def registered_device(self):
        """Gets the registered_device of this StoragePureHostAllOf.  # noqa: E501


        :return: The registered_device of this StoragePureHostAllOf.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this StoragePureHostAllOf.


        :param registered_device: The registered_device of this StoragePureHostAllOf.  # noqa: E501
        :type: AssetDeviceRegistration
        """

        self._registered_device = registered_device

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StoragePureHostAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StoragePureHostAllOf):
            return True

        return self.to_dict() != other.to_dict()
