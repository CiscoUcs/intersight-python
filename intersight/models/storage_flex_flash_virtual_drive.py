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


class StorageFlexFlashVirtualDrive(object):
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
        'drive_scope': 'str',
        'drive_status': 'str',
        'partition_id': 'str',
        'resident_image': 'str',
        'size': 'str',
        'virtual_drive': 'str',
        'registered_device': 'AssetDeviceRegistration',
        'storage_flex_flash_controller': 'StorageFlexFlashController'
    }

    attribute_map = {
        'drive_scope': 'DriveScope',
        'drive_status': 'DriveStatus',
        'partition_id': 'PartitionId',
        'resident_image': 'ResidentImage',
        'size': 'Size',
        'virtual_drive': 'VirtualDrive',
        'registered_device': 'RegisteredDevice',
        'storage_flex_flash_controller': 'StorageFlexFlashController'
    }

    def __init__(self,
                 drive_scope=None,
                 drive_status=None,
                 partition_id=None,
                 resident_image=None,
                 size=None,
                 virtual_drive=None,
                 registered_device=None,
                 storage_flex_flash_controller=None,
                 local_vars_configuration=None):  # noqa: E501
        """StorageFlexFlashVirtualDrive - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._drive_scope = None
        self._drive_status = None
        self._partition_id = None
        self._resident_image = None
        self._size = None
        self._virtual_drive = None
        self._registered_device = None
        self._storage_flex_flash_controller = None
        self.discriminator = None

        if drive_scope is not None:
            self.drive_scope = drive_scope
        if drive_status is not None:
            self.drive_status = drive_status
        if partition_id is not None:
            self.partition_id = partition_id
        if resident_image is not None:
            self.resident_image = resident_image
        if size is not None:
            self.size = size
        if virtual_drive is not None:
            self.virtual_drive = virtual_drive
        if registered_device is not None:
            self.registered_device = registered_device
        if storage_flex_flash_controller is not None:
            self.storage_flex_flash_controller = storage_flex_flash_controller

    @property
    def drive_scope(self):
        """Gets the drive_scope of this StorageFlexFlashVirtualDrive.  # noqa: E501


        :return: The drive_scope of this StorageFlexFlashVirtualDrive.  # noqa: E501
        :rtype: str
        """
        return self._drive_scope

    @drive_scope.setter
    def drive_scope(self, drive_scope):
        """Sets the drive_scope of this StorageFlexFlashVirtualDrive.


        :param drive_scope: The drive_scope of this StorageFlexFlashVirtualDrive.  # noqa: E501
        :type: str
        """

        self._drive_scope = drive_scope

    @property
    def drive_status(self):
        """Gets the drive_status of this StorageFlexFlashVirtualDrive.  # noqa: E501


        :return: The drive_status of this StorageFlexFlashVirtualDrive.  # noqa: E501
        :rtype: str
        """
        return self._drive_status

    @drive_status.setter
    def drive_status(self, drive_status):
        """Sets the drive_status of this StorageFlexFlashVirtualDrive.


        :param drive_status: The drive_status of this StorageFlexFlashVirtualDrive.  # noqa: E501
        :type: str
        """

        self._drive_status = drive_status

    @property
    def partition_id(self):
        """Gets the partition_id of this StorageFlexFlashVirtualDrive.  # noqa: E501


        :return: The partition_id of this StorageFlexFlashVirtualDrive.  # noqa: E501
        :rtype: str
        """
        return self._partition_id

    @partition_id.setter
    def partition_id(self, partition_id):
        """Sets the partition_id of this StorageFlexFlashVirtualDrive.


        :param partition_id: The partition_id of this StorageFlexFlashVirtualDrive.  # noqa: E501
        :type: str
        """

        self._partition_id = partition_id

    @property
    def resident_image(self):
        """Gets the resident_image of this StorageFlexFlashVirtualDrive.  # noqa: E501


        :return: The resident_image of this StorageFlexFlashVirtualDrive.  # noqa: E501
        :rtype: str
        """
        return self._resident_image

    @resident_image.setter
    def resident_image(self, resident_image):
        """Sets the resident_image of this StorageFlexFlashVirtualDrive.


        :param resident_image: The resident_image of this StorageFlexFlashVirtualDrive.  # noqa: E501
        :type: str
        """

        self._resident_image = resident_image

    @property
    def size(self):
        """Gets the size of this StorageFlexFlashVirtualDrive.  # noqa: E501


        :return: The size of this StorageFlexFlashVirtualDrive.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this StorageFlexFlashVirtualDrive.


        :param size: The size of this StorageFlexFlashVirtualDrive.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def virtual_drive(self):
        """Gets the virtual_drive of this StorageFlexFlashVirtualDrive.  # noqa: E501


        :return: The virtual_drive of this StorageFlexFlashVirtualDrive.  # noqa: E501
        :rtype: str
        """
        return self._virtual_drive

    @virtual_drive.setter
    def virtual_drive(self, virtual_drive):
        """Sets the virtual_drive of this StorageFlexFlashVirtualDrive.


        :param virtual_drive: The virtual_drive of this StorageFlexFlashVirtualDrive.  # noqa: E501
        :type: str
        """

        self._virtual_drive = virtual_drive

    @property
    def registered_device(self):
        """Gets the registered_device of this StorageFlexFlashVirtualDrive.  # noqa: E501


        :return: The registered_device of this StorageFlexFlashVirtualDrive.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this StorageFlexFlashVirtualDrive.


        :param registered_device: The registered_device of this StorageFlexFlashVirtualDrive.  # noqa: E501
        :type: AssetDeviceRegistration
        """

        self._registered_device = registered_device

    @property
    def storage_flex_flash_controller(self):
        """Gets the storage_flex_flash_controller of this StorageFlexFlashVirtualDrive.  # noqa: E501


        :return: The storage_flex_flash_controller of this StorageFlexFlashVirtualDrive.  # noqa: E501
        :rtype: StorageFlexFlashController
        """
        return self._storage_flex_flash_controller

    @storage_flex_flash_controller.setter
    def storage_flex_flash_controller(self, storage_flex_flash_controller):
        """Sets the storage_flex_flash_controller of this StorageFlexFlashVirtualDrive.


        :param storage_flex_flash_controller: The storage_flex_flash_controller of this StorageFlexFlashVirtualDrive.  # noqa: E501
        :type: StorageFlexFlashController
        """

        self._storage_flex_flash_controller = storage_flex_flash_controller

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
        if not isinstance(other, StorageFlexFlashVirtualDrive):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageFlexFlashVirtualDrive):
            return True

        return self.to_dict() != other.to_dict()
