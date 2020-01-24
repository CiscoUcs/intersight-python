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


class AdapterUnitAllOf(object):
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
        'adapter_id': 'str',
        'base_mac_address': 'str',
        'integrated': 'str',
        'oper_state': 'str',
        'operability': 'str',
        'part_number': 'str',
        'pci_slot': 'str',
        'power': 'str',
        'presence': 'str',
        'thermal': 'str',
        'vid': 'str',
        'compute_blade': 'ComputeBlade',
        'compute_rack_unit': 'ComputeRackUnit',
        'controller': 'ManagementController',
        'ext_eth_ifs': 'list[AdapterExtEthInterface]',
        'host_eth_ifs': 'list[AdapterHostEthInterface]',
        'host_fc_ifs': 'list[AdapterHostFcInterface]',
        'host_iscsi_ifs': 'list[AdapterHostIscsiInterface]',
        'registered_device': 'AssetDeviceRegistration'
    }

    attribute_map = {
        'adapter_id': 'AdapterId',
        'base_mac_address': 'BaseMacAddress',
        'integrated': 'Integrated',
        'oper_state': 'OperState',
        'operability': 'Operability',
        'part_number': 'PartNumber',
        'pci_slot': 'PciSlot',
        'power': 'Power',
        'presence': 'Presence',
        'thermal': 'Thermal',
        'vid': 'Vid',
        'compute_blade': 'ComputeBlade',
        'compute_rack_unit': 'ComputeRackUnit',
        'controller': 'Controller',
        'ext_eth_ifs': 'ExtEthIfs',
        'host_eth_ifs': 'HostEthIfs',
        'host_fc_ifs': 'HostFcIfs',
        'host_iscsi_ifs': 'HostIscsiIfs',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self,
                 adapter_id=None,
                 base_mac_address=None,
                 integrated=None,
                 oper_state=None,
                 operability=None,
                 part_number=None,
                 pci_slot=None,
                 power=None,
                 presence=None,
                 thermal=None,
                 vid=None,
                 compute_blade=None,
                 compute_rack_unit=None,
                 controller=None,
                 ext_eth_ifs=None,
                 host_eth_ifs=None,
                 host_fc_ifs=None,
                 host_iscsi_ifs=None,
                 registered_device=None,
                 local_vars_configuration=None):  # noqa: E501
        """AdapterUnitAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._adapter_id = None
        self._base_mac_address = None
        self._integrated = None
        self._oper_state = None
        self._operability = None
        self._part_number = None
        self._pci_slot = None
        self._power = None
        self._presence = None
        self._thermal = None
        self._vid = None
        self._compute_blade = None
        self._compute_rack_unit = None
        self._controller = None
        self._ext_eth_ifs = None
        self._host_eth_ifs = None
        self._host_fc_ifs = None
        self._host_iscsi_ifs = None
        self._registered_device = None
        self.discriminator = None

        if adapter_id is not None:
            self.adapter_id = adapter_id
        if base_mac_address is not None:
            self.base_mac_address = base_mac_address
        if integrated is not None:
            self.integrated = integrated
        if oper_state is not None:
            self.oper_state = oper_state
        if operability is not None:
            self.operability = operability
        if part_number is not None:
            self.part_number = part_number
        if pci_slot is not None:
            self.pci_slot = pci_slot
        if power is not None:
            self.power = power
        if presence is not None:
            self.presence = presence
        if thermal is not None:
            self.thermal = thermal
        if vid is not None:
            self.vid = vid
        if compute_blade is not None:
            self.compute_blade = compute_blade
        if compute_rack_unit is not None:
            self.compute_rack_unit = compute_rack_unit
        if controller is not None:
            self.controller = controller
        if ext_eth_ifs is not None:
            self.ext_eth_ifs = ext_eth_ifs
        if host_eth_ifs is not None:
            self.host_eth_ifs = host_eth_ifs
        if host_fc_ifs is not None:
            self.host_fc_ifs = host_fc_ifs
        if host_iscsi_ifs is not None:
            self.host_iscsi_ifs = host_iscsi_ifs
        if registered_device is not None:
            self.registered_device = registered_device

    @property
    def adapter_id(self):
        """Gets the adapter_id of this AdapterUnitAllOf.  # noqa: E501

        Unique Identifier of an adapter Unit within a Rack Interface.    # noqa: E501

        :return: The adapter_id of this AdapterUnitAllOf.  # noqa: E501
        :rtype: str
        """
        return self._adapter_id

    @adapter_id.setter
    def adapter_id(self, adapter_id):
        """Sets the adapter_id of this AdapterUnitAllOf.

        Unique Identifier of an adapter Unit within a Rack Interface.    # noqa: E501

        :param adapter_id: The adapter_id of this AdapterUnitAllOf.  # noqa: E501
        :type: str
        """

        self._adapter_id = adapter_id

    @property
    def base_mac_address(self):
        """Gets the base_mac_address of this AdapterUnitAllOf.  # noqa: E501


        :return: The base_mac_address of this AdapterUnitAllOf.  # noqa: E501
        :rtype: str
        """
        return self._base_mac_address

    @base_mac_address.setter
    def base_mac_address(self, base_mac_address):
        """Sets the base_mac_address of this AdapterUnitAllOf.


        :param base_mac_address: The base_mac_address of this AdapterUnitAllOf.  # noqa: E501
        :type: str
        """

        self._base_mac_address = base_mac_address

    @property
    def integrated(self):
        """Gets the integrated of this AdapterUnitAllOf.  # noqa: E501


        :return: The integrated of this AdapterUnitAllOf.  # noqa: E501
        :rtype: str
        """
        return self._integrated

    @integrated.setter
    def integrated(self, integrated):
        """Sets the integrated of this AdapterUnitAllOf.


        :param integrated: The integrated of this AdapterUnitAllOf.  # noqa: E501
        :type: str
        """

        self._integrated = integrated

    @property
    def oper_state(self):
        """Gets the oper_state of this AdapterUnitAllOf.  # noqa: E501


        :return: The oper_state of this AdapterUnitAllOf.  # noqa: E501
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """Sets the oper_state of this AdapterUnitAllOf.


        :param oper_state: The oper_state of this AdapterUnitAllOf.  # noqa: E501
        :type: str
        """

        self._oper_state = oper_state

    @property
    def operability(self):
        """Gets the operability of this AdapterUnitAllOf.  # noqa: E501


        :return: The operability of this AdapterUnitAllOf.  # noqa: E501
        :rtype: str
        """
        return self._operability

    @operability.setter
    def operability(self, operability):
        """Sets the operability of this AdapterUnitAllOf.


        :param operability: The operability of this AdapterUnitAllOf.  # noqa: E501
        :type: str
        """

        self._operability = operability

    @property
    def part_number(self):
        """Gets the part_number of this AdapterUnitAllOf.  # noqa: E501


        :return: The part_number of this AdapterUnitAllOf.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this AdapterUnitAllOf.


        :param part_number: The part_number of this AdapterUnitAllOf.  # noqa: E501
        :type: str
        """

        self._part_number = part_number

    @property
    def pci_slot(self):
        """Gets the pci_slot of this AdapterUnitAllOf.  # noqa: E501


        :return: The pci_slot of this AdapterUnitAllOf.  # noqa: E501
        :rtype: str
        """
        return self._pci_slot

    @pci_slot.setter
    def pci_slot(self, pci_slot):
        """Sets the pci_slot of this AdapterUnitAllOf.


        :param pci_slot: The pci_slot of this AdapterUnitAllOf.  # noqa: E501
        :type: str
        """

        self._pci_slot = pci_slot

    @property
    def power(self):
        """Gets the power of this AdapterUnitAllOf.  # noqa: E501


        :return: The power of this AdapterUnitAllOf.  # noqa: E501
        :rtype: str
        """
        return self._power

    @power.setter
    def power(self, power):
        """Sets the power of this AdapterUnitAllOf.


        :param power: The power of this AdapterUnitAllOf.  # noqa: E501
        :type: str
        """

        self._power = power

    @property
    def presence(self):
        """Gets the presence of this AdapterUnitAllOf.  # noqa: E501


        :return: The presence of this AdapterUnitAllOf.  # noqa: E501
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """Sets the presence of this AdapterUnitAllOf.


        :param presence: The presence of this AdapterUnitAllOf.  # noqa: E501
        :type: str
        """

        self._presence = presence

    @property
    def thermal(self):
        """Gets the thermal of this AdapterUnitAllOf.  # noqa: E501


        :return: The thermal of this AdapterUnitAllOf.  # noqa: E501
        :rtype: str
        """
        return self._thermal

    @thermal.setter
    def thermal(self, thermal):
        """Sets the thermal of this AdapterUnitAllOf.


        :param thermal: The thermal of this AdapterUnitAllOf.  # noqa: E501
        :type: str
        """

        self._thermal = thermal

    @property
    def vid(self):
        """Gets the vid of this AdapterUnitAllOf.  # noqa: E501


        :return: The vid of this AdapterUnitAllOf.  # noqa: E501
        :rtype: str
        """
        return self._vid

    @vid.setter
    def vid(self, vid):
        """Sets the vid of this AdapterUnitAllOf.


        :param vid: The vid of this AdapterUnitAllOf.  # noqa: E501
        :type: str
        """

        self._vid = vid

    @property
    def compute_blade(self):
        """Gets the compute_blade of this AdapterUnitAllOf.  # noqa: E501


        :return: The compute_blade of this AdapterUnitAllOf.  # noqa: E501
        :rtype: ComputeBlade
        """
        return self._compute_blade

    @compute_blade.setter
    def compute_blade(self, compute_blade):
        """Sets the compute_blade of this AdapterUnitAllOf.


        :param compute_blade: The compute_blade of this AdapterUnitAllOf.  # noqa: E501
        :type: ComputeBlade
        """

        self._compute_blade = compute_blade

    @property
    def compute_rack_unit(self):
        """Gets the compute_rack_unit of this AdapterUnitAllOf.  # noqa: E501


        :return: The compute_rack_unit of this AdapterUnitAllOf.  # noqa: E501
        :rtype: ComputeRackUnit
        """
        return self._compute_rack_unit

    @compute_rack_unit.setter
    def compute_rack_unit(self, compute_rack_unit):
        """Sets the compute_rack_unit of this AdapterUnitAllOf.


        :param compute_rack_unit: The compute_rack_unit of this AdapterUnitAllOf.  # noqa: E501
        :type: ComputeRackUnit
        """

        self._compute_rack_unit = compute_rack_unit

    @property
    def controller(self):
        """Gets the controller of this AdapterUnitAllOf.  # noqa: E501


        :return: The controller of this AdapterUnitAllOf.  # noqa: E501
        :rtype: ManagementController
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """Sets the controller of this AdapterUnitAllOf.


        :param controller: The controller of this AdapterUnitAllOf.  # noqa: E501
        :type: ManagementController
        """

        self._controller = controller

    @property
    def ext_eth_ifs(self):
        """Gets the ext_eth_ifs of this AdapterUnitAllOf.  # noqa: E501

        A reference to a adapterExtEthInterface resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The ext_eth_ifs of this AdapterUnitAllOf.  # noqa: E501
        :rtype: list[AdapterExtEthInterface]
        """
        return self._ext_eth_ifs

    @ext_eth_ifs.setter
    def ext_eth_ifs(self, ext_eth_ifs):
        """Sets the ext_eth_ifs of this AdapterUnitAllOf.

        A reference to a adapterExtEthInterface resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param ext_eth_ifs: The ext_eth_ifs of this AdapterUnitAllOf.  # noqa: E501
        :type: list[AdapterExtEthInterface]
        """

        self._ext_eth_ifs = ext_eth_ifs

    @property
    def host_eth_ifs(self):
        """Gets the host_eth_ifs of this AdapterUnitAllOf.  # noqa: E501

        A reference to a adapterHostEthInterface resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The host_eth_ifs of this AdapterUnitAllOf.  # noqa: E501
        :rtype: list[AdapterHostEthInterface]
        """
        return self._host_eth_ifs

    @host_eth_ifs.setter
    def host_eth_ifs(self, host_eth_ifs):
        """Sets the host_eth_ifs of this AdapterUnitAllOf.

        A reference to a adapterHostEthInterface resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param host_eth_ifs: The host_eth_ifs of this AdapterUnitAllOf.  # noqa: E501
        :type: list[AdapterHostEthInterface]
        """

        self._host_eth_ifs = host_eth_ifs

    @property
    def host_fc_ifs(self):
        """Gets the host_fc_ifs of this AdapterUnitAllOf.  # noqa: E501

        A reference to a adapterHostFcInterface resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The host_fc_ifs of this AdapterUnitAllOf.  # noqa: E501
        :rtype: list[AdapterHostFcInterface]
        """
        return self._host_fc_ifs

    @host_fc_ifs.setter
    def host_fc_ifs(self, host_fc_ifs):
        """Sets the host_fc_ifs of this AdapterUnitAllOf.

        A reference to a adapterHostFcInterface resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param host_fc_ifs: The host_fc_ifs of this AdapterUnitAllOf.  # noqa: E501
        :type: list[AdapterHostFcInterface]
        """

        self._host_fc_ifs = host_fc_ifs

    @property
    def host_iscsi_ifs(self):
        """Gets the host_iscsi_ifs of this AdapterUnitAllOf.  # noqa: E501

        A reference to a adapterHostIscsiInterface resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The host_iscsi_ifs of this AdapterUnitAllOf.  # noqa: E501
        :rtype: list[AdapterHostIscsiInterface]
        """
        return self._host_iscsi_ifs

    @host_iscsi_ifs.setter
    def host_iscsi_ifs(self, host_iscsi_ifs):
        """Sets the host_iscsi_ifs of this AdapterUnitAllOf.

        A reference to a adapterHostIscsiInterface resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param host_iscsi_ifs: The host_iscsi_ifs of this AdapterUnitAllOf.  # noqa: E501
        :type: list[AdapterHostIscsiInterface]
        """

        self._host_iscsi_ifs = host_iscsi_ifs

    @property
    def registered_device(self):
        """Gets the registered_device of this AdapterUnitAllOf.  # noqa: E501


        :return: The registered_device of this AdapterUnitAllOf.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this AdapterUnitAllOf.


        :param registered_device: The registered_device of this AdapterUnitAllOf.  # noqa: E501
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
        if not isinstance(other, AdapterUnitAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdapterUnitAllOf):
            return True

        return self.to_dict() != other.to_dict()
