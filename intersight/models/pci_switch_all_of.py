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


class PciSwitchAllOf(object):
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
        'device_id': 'str',
        'health': 'str',
        'num_of_adaptors': 'str',
        'pci_address': 'str',
        'pci_slot': 'str',
        'product_name': 'str',
        'product_revision': 'str',
        'sub_device_id': 'str',
        'sub_vendor_id': 'str',
        'temperature': 'str',
        'type': 'str',
        'vendor_id': 'str',
        'compute_board': 'ComputeBoard',
        'links': 'list[PciLink]',
        'registered_device': 'AssetDeviceRegistration'
    }

    attribute_map = {
        'device_id': 'DeviceId',
        'health': 'Health',
        'num_of_adaptors': 'NumOfAdaptors',
        'pci_address': 'PciAddress',
        'pci_slot': 'PciSlot',
        'product_name': 'ProductName',
        'product_revision': 'ProductRevision',
        'sub_device_id': 'SubDeviceId',
        'sub_vendor_id': 'SubVendorId',
        'temperature': 'Temperature',
        'type': 'Type',
        'vendor_id': 'VendorId',
        'compute_board': 'ComputeBoard',
        'links': 'Links',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self,
                 device_id=None,
                 health=None,
                 num_of_adaptors=None,
                 pci_address=None,
                 pci_slot=None,
                 product_name=None,
                 product_revision=None,
                 sub_device_id=None,
                 sub_vendor_id=None,
                 temperature=None,
                 type=None,
                 vendor_id=None,
                 compute_board=None,
                 links=None,
                 registered_device=None,
                 local_vars_configuration=None):  # noqa: E501
        """PciSwitchAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_id = None
        self._health = None
        self._num_of_adaptors = None
        self._pci_address = None
        self._pci_slot = None
        self._product_name = None
        self._product_revision = None
        self._sub_device_id = None
        self._sub_vendor_id = None
        self._temperature = None
        self._type = None
        self._vendor_id = None
        self._compute_board = None
        self._links = None
        self._registered_device = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if health is not None:
            self.health = health
        if num_of_adaptors is not None:
            self.num_of_adaptors = num_of_adaptors
        if pci_address is not None:
            self.pci_address = pci_address
        if pci_slot is not None:
            self.pci_slot = pci_slot
        if product_name is not None:
            self.product_name = product_name
        if product_revision is not None:
            self.product_revision = product_revision
        if sub_device_id is not None:
            self.sub_device_id = sub_device_id
        if sub_vendor_id is not None:
            self.sub_vendor_id = sub_vendor_id
        if temperature is not None:
            self.temperature = temperature
        if type is not None:
            self.type = type
        if vendor_id is not None:
            self.vendor_id = vendor_id
        if compute_board is not None:
            self.compute_board = compute_board
        if links is not None:
            self.links = links
        if registered_device is not None:
            self.registered_device = registered_device

    @property
    def device_id(self):
        """Gets the device_id of this PciSwitchAllOf.  # noqa: E501

        It shows the device id of the switch.    # noqa: E501

        :return: The device_id of this PciSwitchAllOf.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this PciSwitchAllOf.

        It shows the device id of the switch.    # noqa: E501

        :param device_id: The device_id of this PciSwitchAllOf.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def health(self):
        """Gets the health of this PciSwitchAllOf.  # noqa: E501

        It shows the composite health of the switch.    # noqa: E501

        :return: The health of this PciSwitchAllOf.  # noqa: E501
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this PciSwitchAllOf.

        It shows the composite health of the switch.    # noqa: E501

        :param health: The health of this PciSwitchAllOf.  # noqa: E501
        :type: str
        """

        self._health = health

    @property
    def num_of_adaptors(self):
        """Gets the num_of_adaptors of this PciSwitchAllOf.  # noqa: E501

        It shows the number of gpus and pci adapters connected the switch.    # noqa: E501

        :return: The num_of_adaptors of this PciSwitchAllOf.  # noqa: E501
        :rtype: str
        """
        return self._num_of_adaptors

    @num_of_adaptors.setter
    def num_of_adaptors(self, num_of_adaptors):
        """Sets the num_of_adaptors of this PciSwitchAllOf.

        It shows the number of gpus and pci adapters connected the switch.    # noqa: E501

        :param num_of_adaptors: The num_of_adaptors of this PciSwitchAllOf.  # noqa: E501
        :type: str
        """

        self._num_of_adaptors = num_of_adaptors

    @property
    def pci_address(self):
        """Gets the pci_address of this PciSwitchAllOf.  # noqa: E501

        It shows shows the PCI address of switch.    # noqa: E501

        :return: The pci_address of this PciSwitchAllOf.  # noqa: E501
        :rtype: str
        """
        return self._pci_address

    @pci_address.setter
    def pci_address(self, pci_address):
        """Sets the pci_address of this PciSwitchAllOf.

        It shows shows the PCI address of switch.    # noqa: E501

        :param pci_address: The pci_address of this PciSwitchAllOf.  # noqa: E501
        :type: str
        """

        self._pci_address = pci_address

    @property
    def pci_slot(self):
        """Gets the pci_slot of this PciSwitchAllOf.  # noqa: E501

        It shows the PCI slot name for switch.    # noqa: E501

        :return: The pci_slot of this PciSwitchAllOf.  # noqa: E501
        :rtype: str
        """
        return self._pci_slot

    @pci_slot.setter
    def pci_slot(self, pci_slot):
        """Sets the pci_slot of this PciSwitchAllOf.

        It shows the PCI slot name for switch.    # noqa: E501

        :param pci_slot: The pci_slot of this PciSwitchAllOf.  # noqa: E501
        :type: str
        """

        self._pci_slot = pci_slot

    @property
    def product_name(self):
        """Gets the product_name of this PciSwitchAllOf.  # noqa: E501

        It shows the model information for the switch.    # noqa: E501

        :return: The product_name of this PciSwitchAllOf.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this PciSwitchAllOf.

        It shows the model information for the switch.    # noqa: E501

        :param product_name: The product_name of this PciSwitchAllOf.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def product_revision(self):
        """Gets the product_revision of this PciSwitchAllOf.  # noqa: E501

        It shows the revision for the product.    # noqa: E501

        :return: The product_revision of this PciSwitchAllOf.  # noqa: E501
        :rtype: str
        """
        return self._product_revision

    @product_revision.setter
    def product_revision(self, product_revision):
        """Sets the product_revision of this PciSwitchAllOf.

        It shows the revision for the product.    # noqa: E501

        :param product_revision: The product_revision of this PciSwitchAllOf.  # noqa: E501
        :type: str
        """

        self._product_revision = product_revision

    @property
    def sub_device_id(self):
        """Gets the sub_device_id of this PciSwitchAllOf.  # noqa: E501

        It shows the sub device id of the switch.    # noqa: E501

        :return: The sub_device_id of this PciSwitchAllOf.  # noqa: E501
        :rtype: str
        """
        return self._sub_device_id

    @sub_device_id.setter
    def sub_device_id(self, sub_device_id):
        """Sets the sub_device_id of this PciSwitchAllOf.

        It shows the sub device id of the switch.    # noqa: E501

        :param sub_device_id: The sub_device_id of this PciSwitchAllOf.  # noqa: E501
        :type: str
        """

        self._sub_device_id = sub_device_id

    @property
    def sub_vendor_id(self):
        """Gets the sub_vendor_id of this PciSwitchAllOf.  # noqa: E501

        It shows the sub vendor id of the switch.    # noqa: E501

        :return: The sub_vendor_id of this PciSwitchAllOf.  # noqa: E501
        :rtype: str
        """
        return self._sub_vendor_id

    @sub_vendor_id.setter
    def sub_vendor_id(self, sub_vendor_id):
        """Sets the sub_vendor_id of this PciSwitchAllOf.

        It shows the sub vendor id of the switch.    # noqa: E501

        :param sub_vendor_id: The sub_vendor_id of this PciSwitchAllOf.  # noqa: E501
        :type: str
        """

        self._sub_vendor_id = sub_vendor_id

    @property
    def temperature(self):
        """Gets the temperature of this PciSwitchAllOf.  # noqa: E501

        It shows the current temperature of the switch.    # noqa: E501

        :return: The temperature of this PciSwitchAllOf.  # noqa: E501
        :rtype: str
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this PciSwitchAllOf.

        It shows the current temperature of the switch.    # noqa: E501

        :param temperature: The temperature of this PciSwitchAllOf.  # noqa: E501
        :type: str
        """

        self._temperature = temperature

    @property
    def type(self):
        """Gets the type of this PciSwitchAllOf.  # noqa: E501

        It shows the type inforamtion of switch.    # noqa: E501

        :return: The type of this PciSwitchAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PciSwitchAllOf.

        It shows the type inforamtion of switch.    # noqa: E501

        :param type: The type of this PciSwitchAllOf.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def vendor_id(self):
        """Gets the vendor_id of this PciSwitchAllOf.  # noqa: E501

        It shows the vendor id of the switch.     # noqa: E501

        :return: The vendor_id of this PciSwitchAllOf.  # noqa: E501
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """Sets the vendor_id of this PciSwitchAllOf.

        It shows the vendor id of the switch.     # noqa: E501

        :param vendor_id: The vendor_id of this PciSwitchAllOf.  # noqa: E501
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def compute_board(self):
        """Gets the compute_board of this PciSwitchAllOf.  # noqa: E501


        :return: The compute_board of this PciSwitchAllOf.  # noqa: E501
        :rtype: ComputeBoard
        """
        return self._compute_board

    @compute_board.setter
    def compute_board(self, compute_board):
        """Sets the compute_board of this PciSwitchAllOf.


        :param compute_board: The compute_board of this PciSwitchAllOf.  # noqa: E501
        :type: ComputeBoard
        """

        self._compute_board = compute_board

    @property
    def links(self):
        """Gets the links of this PciSwitchAllOf.  # noqa: E501

        A reference to a pciLink resource. When the $expand query parameter is specified, the referenced resource is returned inline. It shows the number of gpus and pci adapters under each switch.   # noqa: E501

        :return: The links of this PciSwitchAllOf.  # noqa: E501
        :rtype: list[PciLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PciSwitchAllOf.

        A reference to a pciLink resource. When the $expand query parameter is specified, the referenced resource is returned inline. It shows the number of gpus and pci adapters under each switch.   # noqa: E501

        :param links: The links of this PciSwitchAllOf.  # noqa: E501
        :type: list[PciLink]
        """

        self._links = links

    @property
    def registered_device(self):
        """Gets the registered_device of this PciSwitchAllOf.  # noqa: E501


        :return: The registered_device of this PciSwitchAllOf.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this PciSwitchAllOf.


        :param registered_device: The registered_device of this PciSwitchAllOf.  # noqa: E501
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
        if not isinstance(other, PciSwitchAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PciSwitchAllOf):
            return True

        return self.to_dict() != other.to_dict()
