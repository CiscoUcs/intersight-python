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


class StoragePhysicalPort(object):
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
        'iqn': 'str',
        'name': 'str',
        'speed': 'int',
        'status': 'str',
        'type': 'str',
        'wwn': 'str',
        'wwnn': 'str',
        'wwpn': 'str',
        'controller': 'StorageArrayController',
        'storage_array': 'StorageGenericArray'
    }

    attribute_map = {
        'iqn': 'Iqn',
        'name': 'Name',
        'speed': 'Speed',
        'status': 'Status',
        'type': 'Type',
        'wwn': 'Wwn',
        'wwnn': 'Wwnn',
        'wwpn': 'Wwpn',
        'controller': 'Controller',
        'storage_array': 'StorageArray'
    }

    def __init__(self,
                 iqn=None,
                 name=None,
                 speed=None,
                 status='Unknown',
                 type='FC',
                 wwn=None,
                 wwnn=None,
                 wwpn=None,
                 controller=None,
                 storage_array=None,
                 local_vars_configuration=None):  # noqa: E501
        """StoragePhysicalPort - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._iqn = None
        self._name = None
        self._speed = None
        self._status = None
        self._type = None
        self._wwn = None
        self._wwnn = None
        self._wwpn = None
        self._controller = None
        self._storage_array = None
        self.discriminator = None

        if iqn is not None:
            self.iqn = iqn
        if name is not None:
            self.name = name
        if speed is not None:
            self.speed = speed
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if wwn is not None:
            self.wwn = wwn
        if wwnn is not None:
            self.wwnn = wwnn
        if wwpn is not None:
            self.wwpn = wwpn
        if controller is not None:
            self.controller = controller
        if storage_array is not None:
            self.storage_array = storage_array

    @property
    def iqn(self):
        """Gets the iqn of this StoragePhysicalPort.  # noqa: E501

        ISCSI qualified name applicable for ethernet port. eg 'iqn.2008-05.com.storage:fnm00151300643-514f0c50141faf05'.    # noqa: E501

        :return: The iqn of this StoragePhysicalPort.  # noqa: E501
        :rtype: str
        """
        return self._iqn

    @iqn.setter
    def iqn(self, iqn):
        """Sets the iqn of this StoragePhysicalPort.

        ISCSI qualified name applicable for ethernet port. eg 'iqn.2008-05.com.storage:fnm00151300643-514f0c50141faf05'.    # noqa: E501

        :param iqn: The iqn of this StoragePhysicalPort.  # noqa: E501
        :type: str
        """

        self._iqn = iqn

    @property
    def name(self):
        """Gets the name of this StoragePhysicalPort.  # noqa: E501

        Name of the physical port available in storage array.    # noqa: E501

        :return: The name of this StoragePhysicalPort.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StoragePhysicalPort.

        Name of the physical port available in storage array.    # noqa: E501

        :param name: The name of this StoragePhysicalPort.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def speed(self):
        """Gets the speed of this StoragePhysicalPort.  # noqa: E501

        Operational speed of physical port measured in Gbps.    # noqa: E501

        :return: The speed of this StoragePhysicalPort.  # noqa: E501
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this StoragePhysicalPort.

        Operational speed of physical port measured in Gbps.    # noqa: E501

        :param speed: The speed of this StoragePhysicalPort.  # noqa: E501
        :type: int
        """

        self._speed = speed

    @property
    def status(self):
        """Gets the status of this StoragePhysicalPort.  # noqa: E501

        Status of storage array port.    # noqa: E501

        :return: The status of this StoragePhysicalPort.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StoragePhysicalPort.

        Status of storage array port.    # noqa: E501

        :param status: The status of this StoragePhysicalPort.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "Unknown", "Ok", "Degraded", "Critical", "Offline", "Identifying",
            "NotAvailable", "Updating", "Unrecognized"
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values))

        self._status = status

    @property
    def type(self):
        """Gets the type of this StoragePhysicalPort.  # noqa: E501

        Port type, it can be a any of the following category FC, FCoE and iSCSI.    # noqa: E501

        :return: The type of this StoragePhysicalPort.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StoragePhysicalPort.

        Port type, it can be a any of the following category FC, FCoE and iSCSI.    # noqa: E501

        :param type: The type of this StoragePhysicalPort.  # noqa: E501
        :type: str
        """
        allowed_values = ["FC", "iSCSI", "FCoE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values))

        self._type = type

    @property
    def wwn(self):
        """Gets the wwn of this StoragePhysicalPort.  # noqa: E501

        World wide name of FC port. It is a combination of WWNN and WWPN represented in 128 bit hexa decimal formatted with colon. e.g '51:4f:0c:50:14:1f:af:01:51:4f:0c:51:14:1f:af:01'.    # noqa: E501

        :return: The wwn of this StoragePhysicalPort.  # noqa: E501
        :rtype: str
        """
        return self._wwn

    @wwn.setter
    def wwn(self, wwn):
        """Sets the wwn of this StoragePhysicalPort.

        World wide name of FC port. It is a combination of WWNN and WWPN represented in 128 bit hexa decimal formatted with colon. e.g '51:4f:0c:50:14:1f:af:01:51:4f:0c:51:14:1f:af:01'.    # noqa: E501

        :param wwn: The wwn of this StoragePhysicalPort.  # noqa: E501
        :type: str
        """

        self._wwn = wwn

    @property
    def wwnn(self):
        """Gets the wwnn of this StoragePhysicalPort.  # noqa: E501

        World wide node name of FC port. Represented in 64 bit digit hexa formatted with colon eg '51:4f:0c:50:14:1f:af:01'.    # noqa: E501

        :return: The wwnn of this StoragePhysicalPort.  # noqa: E501
        :rtype: str
        """
        return self._wwnn

    @wwnn.setter
    def wwnn(self, wwnn):
        """Sets the wwnn of this StoragePhysicalPort.

        World wide node name of FC port. Represented in 64 bit digit hexa formatted with colon eg '51:4f:0c:50:14:1f:af:01'.    # noqa: E501

        :param wwnn: The wwnn of this StoragePhysicalPort.  # noqa: E501
        :type: str
        """

        self._wwnn = wwnn

    @property
    def wwpn(self):
        """Gets the wwpn of this StoragePhysicalPort.  # noqa: E501

        World wide port name of FC port. Represented in 64 bit digit hexa formatted with colon eg '51:4f:0c:51:14:1f:af:01'.     # noqa: E501

        :return: The wwpn of this StoragePhysicalPort.  # noqa: E501
        :rtype: str
        """
        return self._wwpn

    @wwpn.setter
    def wwpn(self, wwpn):
        """Sets the wwpn of this StoragePhysicalPort.

        World wide port name of FC port. Represented in 64 bit digit hexa formatted with colon eg '51:4f:0c:51:14:1f:af:01'.     # noqa: E501

        :param wwpn: The wwpn of this StoragePhysicalPort.  # noqa: E501
        :type: str
        """

        self._wwpn = wwpn

    @property
    def controller(self):
        """Gets the controller of this StoragePhysicalPort.  # noqa: E501


        :return: The controller of this StoragePhysicalPort.  # noqa: E501
        :rtype: StorageArrayController
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """Sets the controller of this StoragePhysicalPort.


        :param controller: The controller of this StoragePhysicalPort.  # noqa: E501
        :type: StorageArrayController
        """

        self._controller = controller

    @property
    def storage_array(self):
        """Gets the storage_array of this StoragePhysicalPort.  # noqa: E501


        :return: The storage_array of this StoragePhysicalPort.  # noqa: E501
        :rtype: StorageGenericArray
        """
        return self._storage_array

    @storage_array.setter
    def storage_array(self, storage_array):
        """Sets the storage_array of this StoragePhysicalPort.


        :param storage_array: The storage_array of this StoragePhysicalPort.  # noqa: E501
        :type: StorageGenericArray
        """

        self._storage_array = storage_array

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
        if not isinstance(other, StoragePhysicalPort):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StoragePhysicalPort):
            return True

        return self.to_dict() != other.to_dict()
