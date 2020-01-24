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


class EquipmentSwitchCard(object):
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
        'description': 'str',
        'num_ports': 'int',
        'presence': 'str',
        'slot_id': 'int',
        'state': 'str',
        'network_element': 'NetworkElement',
        'port_groups': 'list[PortGroup]',
        'registered_device': 'AssetDeviceRegistration'
    }

    attribute_map = {
        'description': 'Description',
        'num_ports': 'NumPorts',
        'presence': 'Presence',
        'slot_id': 'SlotId',
        'state': 'State',
        'network_element': 'NetworkElement',
        'port_groups': 'PortGroups',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self,
                 description=None,
                 num_ports=None,
                 presence=None,
                 slot_id=None,
                 state=None,
                 network_element=None,
                 port_groups=None,
                 registered_device=None,
                 local_vars_configuration=None):  # noqa: E501
        """EquipmentSwitchCard - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._num_ports = None
        self._presence = None
        self._slot_id = None
        self._state = None
        self._network_element = None
        self._port_groups = None
        self._registered_device = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if num_ports is not None:
            self.num_ports = num_ports
        if presence is not None:
            self.presence = presence
        if slot_id is not None:
            self.slot_id = slot_id
        if state is not None:
            self.state = state
        if network_element is not None:
            self.network_element = network_element
        if port_groups is not None:
            self.port_groups = port_groups
        if registered_device is not None:
            self.registered_device = registered_device

    @property
    def description(self):
        """Gets the description of this EquipmentSwitchCard.  # noqa: E501


        :return: The description of this EquipmentSwitchCard.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EquipmentSwitchCard.


        :param description: The description of this EquipmentSwitchCard.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def num_ports(self):
        """Gets the num_ports of this EquipmentSwitchCard.  # noqa: E501


        :return: The num_ports of this EquipmentSwitchCard.  # noqa: E501
        :rtype: int
        """
        return self._num_ports

    @num_ports.setter
    def num_ports(self, num_ports):
        """Sets the num_ports of this EquipmentSwitchCard.


        :param num_ports: The num_ports of this EquipmentSwitchCard.  # noqa: E501
        :type: int
        """

        self._num_ports = num_ports

    @property
    def presence(self):
        """Gets the presence of this EquipmentSwitchCard.  # noqa: E501


        :return: The presence of this EquipmentSwitchCard.  # noqa: E501
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """Sets the presence of this EquipmentSwitchCard.


        :param presence: The presence of this EquipmentSwitchCard.  # noqa: E501
        :type: str
        """

        self._presence = presence

    @property
    def slot_id(self):
        """Gets the slot_id of this EquipmentSwitchCard.  # noqa: E501


        :return: The slot_id of this EquipmentSwitchCard.  # noqa: E501
        :rtype: int
        """
        return self._slot_id

    @slot_id.setter
    def slot_id(self, slot_id):
        """Sets the slot_id of this EquipmentSwitchCard.


        :param slot_id: The slot_id of this EquipmentSwitchCard.  # noqa: E501
        :type: int
        """

        self._slot_id = slot_id

    @property
    def state(self):
        """Gets the state of this EquipmentSwitchCard.  # noqa: E501


        :return: The state of this EquipmentSwitchCard.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this EquipmentSwitchCard.


        :param state: The state of this EquipmentSwitchCard.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def network_element(self):
        """Gets the network_element of this EquipmentSwitchCard.  # noqa: E501


        :return: The network_element of this EquipmentSwitchCard.  # noqa: E501
        :rtype: NetworkElement
        """
        return self._network_element

    @network_element.setter
    def network_element(self, network_element):
        """Sets the network_element of this EquipmentSwitchCard.


        :param network_element: The network_element of this EquipmentSwitchCard.  # noqa: E501
        :type: NetworkElement
        """

        self._network_element = network_element

    @property
    def port_groups(self):
        """Gets the port_groups of this EquipmentSwitchCard.  # noqa: E501

        A reference to a portGroup resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The port_groups of this EquipmentSwitchCard.  # noqa: E501
        :rtype: list[PortGroup]
        """
        return self._port_groups

    @port_groups.setter
    def port_groups(self, port_groups):
        """Sets the port_groups of this EquipmentSwitchCard.

        A reference to a portGroup resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param port_groups: The port_groups of this EquipmentSwitchCard.  # noqa: E501
        :type: list[PortGroup]
        """

        self._port_groups = port_groups

    @property
    def registered_device(self):
        """Gets the registered_device of this EquipmentSwitchCard.  # noqa: E501


        :return: The registered_device of this EquipmentSwitchCard.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this EquipmentSwitchCard.


        :param registered_device: The registered_device of this EquipmentSwitchCard.  # noqa: E501
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
        if not isinstance(other, EquipmentSwitchCard):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EquipmentSwitchCard):
            return True

        return self.to_dict() != other.to_dict()
