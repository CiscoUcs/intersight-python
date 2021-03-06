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


class StorageSasPortAllOf(object):
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
        'address': 'str',
        'disk_id': 'int',
        'end_point_id': 'int',
        'link_description': 'str',
        'link_speed': 'str',
        'registered_device': 'AssetDeviceRegistration',
        'storage_physical_disk': 'StoragePhysicalDisk'
    }

    attribute_map = {
        'address': 'Address',
        'disk_id': 'DiskId',
        'end_point_id': 'EndPointId',
        'link_description': 'LinkDescription',
        'link_speed': 'LinkSpeed',
        'registered_device': 'RegisteredDevice',
        'storage_physical_disk': 'StoragePhysicalDisk'
    }

    def __init__(self,
                 address=None,
                 disk_id=None,
                 end_point_id=None,
                 link_description=None,
                 link_speed=None,
                 registered_device=None,
                 storage_physical_disk=None,
                 local_vars_configuration=None):  # noqa: E501
        """StorageSasPortAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._disk_id = None
        self._end_point_id = None
        self._link_description = None
        self._link_speed = None
        self._registered_device = None
        self._storage_physical_disk = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if disk_id is not None:
            self.disk_id = disk_id
        if end_point_id is not None:
            self.end_point_id = end_point_id
        if link_description is not None:
            self.link_description = link_description
        if link_speed is not None:
            self.link_speed = link_speed
        if registered_device is not None:
            self.registered_device = registered_device
        if storage_physical_disk is not None:
            self.storage_physical_disk = storage_physical_disk

    @property
    def address(self):
        """Gets the address of this StorageSasPortAllOf.  # noqa: E501

        The SAS Address assigned to storage port.    # noqa: E501

        :return: The address of this StorageSasPortAllOf.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this StorageSasPortAllOf.

        The SAS Address assigned to storage port.    # noqa: E501

        :param address: The address of this StorageSasPortAllOf.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def disk_id(self):
        """Gets the disk_id of this StorageSasPortAllOf.  # noqa: E501

        The disk identifier.    # noqa: E501

        :return: The disk_id of this StorageSasPortAllOf.  # noqa: E501
        :rtype: int
        """
        return self._disk_id

    @disk_id.setter
    def disk_id(self, disk_id):
        """Sets the disk_id of this StorageSasPortAllOf.

        The disk identifier.    # noqa: E501

        :param disk_id: The disk_id of this StorageSasPortAllOf.  # noqa: E501
        :type: int
        """

        self._disk_id = disk_id

    @property
    def end_point_id(self):
        """Gets the end_point_id of this StorageSasPortAllOf.  # noqa: E501

        The end-point Id assigned to storage port.    # noqa: E501

        :return: The end_point_id of this StorageSasPortAllOf.  # noqa: E501
        :rtype: int
        """
        return self._end_point_id

    @end_point_id.setter
    def end_point_id(self, end_point_id):
        """Sets the end_point_id of this StorageSasPortAllOf.

        The end-point Id assigned to storage port.    # noqa: E501

        :param end_point_id: The end_point_id of this StorageSasPortAllOf.  # noqa: E501
        :type: int
        """

        self._end_point_id = end_point_id

    @property
    def link_description(self):
        """Gets the link_description of this StorageSasPortAllOf.  # noqa: E501

        The link description.    # noqa: E501

        :return: The link_description of this StorageSasPortAllOf.  # noqa: E501
        :rtype: str
        """
        return self._link_description

    @link_description.setter
    def link_description(self, link_description):
        """Sets the link_description of this StorageSasPortAllOf.

        The link description.    # noqa: E501

        :param link_description: The link_description of this StorageSasPortAllOf.  # noqa: E501
        :type: str
        """

        self._link_description = link_description

    @property
    def link_speed(self):
        """Gets the link_speed of this StorageSasPortAllOf.  # noqa: E501

        The link speed negotiated for communication.     # noqa: E501

        :return: The link_speed of this StorageSasPortAllOf.  # noqa: E501
        :rtype: str
        """
        return self._link_speed

    @link_speed.setter
    def link_speed(self, link_speed):
        """Sets the link_speed of this StorageSasPortAllOf.

        The link speed negotiated for communication.     # noqa: E501

        :param link_speed: The link_speed of this StorageSasPortAllOf.  # noqa: E501
        :type: str
        """

        self._link_speed = link_speed

    @property
    def registered_device(self):
        """Gets the registered_device of this StorageSasPortAllOf.  # noqa: E501


        :return: The registered_device of this StorageSasPortAllOf.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this StorageSasPortAllOf.


        :param registered_device: The registered_device of this StorageSasPortAllOf.  # noqa: E501
        :type: AssetDeviceRegistration
        """

        self._registered_device = registered_device

    @property
    def storage_physical_disk(self):
        """Gets the storage_physical_disk of this StorageSasPortAllOf.  # noqa: E501


        :return: The storage_physical_disk of this StorageSasPortAllOf.  # noqa: E501
        :rtype: StoragePhysicalDisk
        """
        return self._storage_physical_disk

    @storage_physical_disk.setter
    def storage_physical_disk(self, storage_physical_disk):
        """Sets the storage_physical_disk of this StorageSasPortAllOf.


        :param storage_physical_disk: The storage_physical_disk of this StorageSasPortAllOf.  # noqa: E501
        :type: StoragePhysicalDisk
        """

        self._storage_physical_disk = storage_physical_disk

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
        if not isinstance(other, StorageSasPortAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageSasPortAllOf):
            return True

        return self.to_dict() != other.to_dict()
