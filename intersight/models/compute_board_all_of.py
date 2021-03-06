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


class ComputeBoardAllOf(object):
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
        'board_id': 'int',
        'cpu_type_controller': 'str',
        'oper_power_state': 'str',
        'presence': 'str',
        'compute_blade': 'ComputeBlade',
        'compute_rack_unit': 'ComputeRackUnit',
        'equipment_tpms': 'list[EquipmentTpm]',
        'graphics_cards': 'list[GraphicsCard]',
        'memory_arrays': 'list[MemoryArray]',
        'pci_coprocessor_cards': 'list[PciCoprocessorCard]',
        'pci_switch': 'list[PciSwitch]',
        'persistent_memory_configuration':
        'MemoryPersistentMemoryConfiguration',
        'processors': 'list[ProcessorUnit]',
        'registered_device': 'AssetDeviceRegistration',
        'security_units': 'list[SecurityUnit]',
        'storage_controllers': 'list[StorageController]',
        'storage_flex_flash_controllers': 'list[StorageFlexFlashController]',
        'storage_flex_util_controllers': 'list[StorageFlexUtilController]'
    }

    attribute_map = {
        'board_id': 'BoardId',
        'cpu_type_controller': 'CpuTypeController',
        'oper_power_state': 'OperPowerState',
        'presence': 'Presence',
        'compute_blade': 'ComputeBlade',
        'compute_rack_unit': 'ComputeRackUnit',
        'equipment_tpms': 'EquipmentTpms',
        'graphics_cards': 'GraphicsCards',
        'memory_arrays': 'MemoryArrays',
        'pci_coprocessor_cards': 'PciCoprocessorCards',
        'pci_switch': 'PciSwitch',
        'persistent_memory_configuration': 'PersistentMemoryConfiguration',
        'processors': 'Processors',
        'registered_device': 'RegisteredDevice',
        'security_units': 'SecurityUnits',
        'storage_controllers': 'StorageControllers',
        'storage_flex_flash_controllers': 'StorageFlexFlashControllers',
        'storage_flex_util_controllers': 'StorageFlexUtilControllers'
    }

    def __init__(self,
                 board_id=None,
                 cpu_type_controller=None,
                 oper_power_state=None,
                 presence=None,
                 compute_blade=None,
                 compute_rack_unit=None,
                 equipment_tpms=None,
                 graphics_cards=None,
                 memory_arrays=None,
                 pci_coprocessor_cards=None,
                 pci_switch=None,
                 persistent_memory_configuration=None,
                 processors=None,
                 registered_device=None,
                 security_units=None,
                 storage_controllers=None,
                 storage_flex_flash_controllers=None,
                 storage_flex_util_controllers=None,
                 local_vars_configuration=None):  # noqa: E501
        """ComputeBoardAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._board_id = None
        self._cpu_type_controller = None
        self._oper_power_state = None
        self._presence = None
        self._compute_blade = None
        self._compute_rack_unit = None
        self._equipment_tpms = None
        self._graphics_cards = None
        self._memory_arrays = None
        self._pci_coprocessor_cards = None
        self._pci_switch = None
        self._persistent_memory_configuration = None
        self._processors = None
        self._registered_device = None
        self._security_units = None
        self._storage_controllers = None
        self._storage_flex_flash_controllers = None
        self._storage_flex_util_controllers = None
        self.discriminator = None

        if board_id is not None:
            self.board_id = board_id
        if cpu_type_controller is not None:
            self.cpu_type_controller = cpu_type_controller
        if oper_power_state is not None:
            self.oper_power_state = oper_power_state
        if presence is not None:
            self.presence = presence
        if compute_blade is not None:
            self.compute_blade = compute_blade
        if compute_rack_unit is not None:
            self.compute_rack_unit = compute_rack_unit
        if equipment_tpms is not None:
            self.equipment_tpms = equipment_tpms
        if graphics_cards is not None:
            self.graphics_cards = graphics_cards
        if memory_arrays is not None:
            self.memory_arrays = memory_arrays
        if pci_coprocessor_cards is not None:
            self.pci_coprocessor_cards = pci_coprocessor_cards
        if pci_switch is not None:
            self.pci_switch = pci_switch
        if persistent_memory_configuration is not None:
            self.persistent_memory_configuration = persistent_memory_configuration
        if processors is not None:
            self.processors = processors
        if registered_device is not None:
            self.registered_device = registered_device
        if security_units is not None:
            self.security_units = security_units
        if storage_controllers is not None:
            self.storage_controllers = storage_controllers
        if storage_flex_flash_controllers is not None:
            self.storage_flex_flash_controllers = storage_flex_flash_controllers
        if storage_flex_util_controllers is not None:
            self.storage_flex_util_controllers = storage_flex_util_controllers

    @property
    def board_id(self):
        """Gets the board_id of this ComputeBoardAllOf.  # noqa: E501


        :return: The board_id of this ComputeBoardAllOf.  # noqa: E501
        :rtype: int
        """
        return self._board_id

    @board_id.setter
    def board_id(self, board_id):
        """Sets the board_id of this ComputeBoardAllOf.


        :param board_id: The board_id of this ComputeBoardAllOf.  # noqa: E501
        :type: int
        """

        self._board_id = board_id

    @property
    def cpu_type_controller(self):
        """Gets the cpu_type_controller of this ComputeBoardAllOf.  # noqa: E501


        :return: The cpu_type_controller of this ComputeBoardAllOf.  # noqa: E501
        :rtype: str
        """
        return self._cpu_type_controller

    @cpu_type_controller.setter
    def cpu_type_controller(self, cpu_type_controller):
        """Sets the cpu_type_controller of this ComputeBoardAllOf.


        :param cpu_type_controller: The cpu_type_controller of this ComputeBoardAllOf.  # noqa: E501
        :type: str
        """

        self._cpu_type_controller = cpu_type_controller

    @property
    def oper_power_state(self):
        """Gets the oper_power_state of this ComputeBoardAllOf.  # noqa: E501


        :return: The oper_power_state of this ComputeBoardAllOf.  # noqa: E501
        :rtype: str
        """
        return self._oper_power_state

    @oper_power_state.setter
    def oper_power_state(self, oper_power_state):
        """Sets the oper_power_state of this ComputeBoardAllOf.


        :param oper_power_state: The oper_power_state of this ComputeBoardAllOf.  # noqa: E501
        :type: str
        """

        self._oper_power_state = oper_power_state

    @property
    def presence(self):
        """Gets the presence of this ComputeBoardAllOf.  # noqa: E501


        :return: The presence of this ComputeBoardAllOf.  # noqa: E501
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """Sets the presence of this ComputeBoardAllOf.


        :param presence: The presence of this ComputeBoardAllOf.  # noqa: E501
        :type: str
        """

        self._presence = presence

    @property
    def compute_blade(self):
        """Gets the compute_blade of this ComputeBoardAllOf.  # noqa: E501


        :return: The compute_blade of this ComputeBoardAllOf.  # noqa: E501
        :rtype: ComputeBlade
        """
        return self._compute_blade

    @compute_blade.setter
    def compute_blade(self, compute_blade):
        """Sets the compute_blade of this ComputeBoardAllOf.


        :param compute_blade: The compute_blade of this ComputeBoardAllOf.  # noqa: E501
        :type: ComputeBlade
        """

        self._compute_blade = compute_blade

    @property
    def compute_rack_unit(self):
        """Gets the compute_rack_unit of this ComputeBoardAllOf.  # noqa: E501


        :return: The compute_rack_unit of this ComputeBoardAllOf.  # noqa: E501
        :rtype: ComputeRackUnit
        """
        return self._compute_rack_unit

    @compute_rack_unit.setter
    def compute_rack_unit(self, compute_rack_unit):
        """Sets the compute_rack_unit of this ComputeBoardAllOf.


        :param compute_rack_unit: The compute_rack_unit of this ComputeBoardAllOf.  # noqa: E501
        :type: ComputeRackUnit
        """

        self._compute_rack_unit = compute_rack_unit

    @property
    def equipment_tpms(self):
        """Gets the equipment_tpms of this ComputeBoardAllOf.  # noqa: E501

        A reference to a equipmentTpm resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The equipment_tpms of this ComputeBoardAllOf.  # noqa: E501
        :rtype: list[EquipmentTpm]
        """
        return self._equipment_tpms

    @equipment_tpms.setter
    def equipment_tpms(self, equipment_tpms):
        """Sets the equipment_tpms of this ComputeBoardAllOf.

        A reference to a equipmentTpm resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param equipment_tpms: The equipment_tpms of this ComputeBoardAllOf.  # noqa: E501
        :type: list[EquipmentTpm]
        """

        self._equipment_tpms = equipment_tpms

    @property
    def graphics_cards(self):
        """Gets the graphics_cards of this ComputeBoardAllOf.  # noqa: E501

        A reference to a graphicsCard resource. When the $expand query parameter is specified, the referenced resource is returned inline. It shows Graphics cards present in a server.   # noqa: E501

        :return: The graphics_cards of this ComputeBoardAllOf.  # noqa: E501
        :rtype: list[GraphicsCard]
        """
        return self._graphics_cards

    @graphics_cards.setter
    def graphics_cards(self, graphics_cards):
        """Sets the graphics_cards of this ComputeBoardAllOf.

        A reference to a graphicsCard resource. When the $expand query parameter is specified, the referenced resource is returned inline. It shows Graphics cards present in a server.   # noqa: E501

        :param graphics_cards: The graphics_cards of this ComputeBoardAllOf.  # noqa: E501
        :type: list[GraphicsCard]
        """

        self._graphics_cards = graphics_cards

    @property
    def memory_arrays(self):
        """Gets the memory_arrays of this ComputeBoardAllOf.  # noqa: E501

        A reference to a memoryArray resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The memory_arrays of this ComputeBoardAllOf.  # noqa: E501
        :rtype: list[MemoryArray]
        """
        return self._memory_arrays

    @memory_arrays.setter
    def memory_arrays(self, memory_arrays):
        """Sets the memory_arrays of this ComputeBoardAllOf.

        A reference to a memoryArray resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param memory_arrays: The memory_arrays of this ComputeBoardAllOf.  # noqa: E501
        :type: list[MemoryArray]
        """

        self._memory_arrays = memory_arrays

    @property
    def pci_coprocessor_cards(self):
        """Gets the pci_coprocessor_cards of this ComputeBoardAllOf.  # noqa: E501

        A reference to a pciCoprocessorCard resource. When the $expand query parameter is specified, the referenced resource is returned inline. It shows PCI CoprocessorCard present in a server.   # noqa: E501

        :return: The pci_coprocessor_cards of this ComputeBoardAllOf.  # noqa: E501
        :rtype: list[PciCoprocessorCard]
        """
        return self._pci_coprocessor_cards

    @pci_coprocessor_cards.setter
    def pci_coprocessor_cards(self, pci_coprocessor_cards):
        """Sets the pci_coprocessor_cards of this ComputeBoardAllOf.

        A reference to a pciCoprocessorCard resource. When the $expand query parameter is specified, the referenced resource is returned inline. It shows PCI CoprocessorCard present in a server.   # noqa: E501

        :param pci_coprocessor_cards: The pci_coprocessor_cards of this ComputeBoardAllOf.  # noqa: E501
        :type: list[PciCoprocessorCard]
        """

        self._pci_coprocessor_cards = pci_coprocessor_cards

    @property
    def pci_switch(self):
        """Gets the pci_switch of this ComputeBoardAllOf.  # noqa: E501

        A reference to a pciSwitch resource. When the $expand query parameter is specified, the referenced resource is returned inline. It shows PCI Switches presen in a server.   # noqa: E501

        :return: The pci_switch of this ComputeBoardAllOf.  # noqa: E501
        :rtype: list[PciSwitch]
        """
        return self._pci_switch

    @pci_switch.setter
    def pci_switch(self, pci_switch):
        """Sets the pci_switch of this ComputeBoardAllOf.

        A reference to a pciSwitch resource. When the $expand query parameter is specified, the referenced resource is returned inline. It shows PCI Switches presen in a server.   # noqa: E501

        :param pci_switch: The pci_switch of this ComputeBoardAllOf.  # noqa: E501
        :type: list[PciSwitch]
        """

        self._pci_switch = pci_switch

    @property
    def persistent_memory_configuration(self):
        """Gets the persistent_memory_configuration of this ComputeBoardAllOf.  # noqa: E501


        :return: The persistent_memory_configuration of this ComputeBoardAllOf.  # noqa: E501
        :rtype: MemoryPersistentMemoryConfiguration
        """
        return self._persistent_memory_configuration

    @persistent_memory_configuration.setter
    def persistent_memory_configuration(self, persistent_memory_configuration):
        """Sets the persistent_memory_configuration of this ComputeBoardAllOf.


        :param persistent_memory_configuration: The persistent_memory_configuration of this ComputeBoardAllOf.  # noqa: E501
        :type: MemoryPersistentMemoryConfiguration
        """

        self._persistent_memory_configuration = persistent_memory_configuration

    @property
    def processors(self):
        """Gets the processors of this ComputeBoardAllOf.  # noqa: E501

        A reference to a processorUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The processors of this ComputeBoardAllOf.  # noqa: E501
        :rtype: list[ProcessorUnit]
        """
        return self._processors

    @processors.setter
    def processors(self, processors):
        """Sets the processors of this ComputeBoardAllOf.

        A reference to a processorUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param processors: The processors of this ComputeBoardAllOf.  # noqa: E501
        :type: list[ProcessorUnit]
        """

        self._processors = processors

    @property
    def registered_device(self):
        """Gets the registered_device of this ComputeBoardAllOf.  # noqa: E501


        :return: The registered_device of this ComputeBoardAllOf.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this ComputeBoardAllOf.


        :param registered_device: The registered_device of this ComputeBoardAllOf.  # noqa: E501
        :type: AssetDeviceRegistration
        """

        self._registered_device = registered_device

    @property
    def security_units(self):
        """Gets the security_units of this ComputeBoardAllOf.  # noqa: E501

        A reference to a securityUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The security_units of this ComputeBoardAllOf.  # noqa: E501
        :rtype: list[SecurityUnit]
        """
        return self._security_units

    @security_units.setter
    def security_units(self, security_units):
        """Sets the security_units of this ComputeBoardAllOf.

        A reference to a securityUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param security_units: The security_units of this ComputeBoardAllOf.  # noqa: E501
        :type: list[SecurityUnit]
        """

        self._security_units = security_units

    @property
    def storage_controllers(self):
        """Gets the storage_controllers of this ComputeBoardAllOf.  # noqa: E501

        A reference to a storageController resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The storage_controllers of this ComputeBoardAllOf.  # noqa: E501
        :rtype: list[StorageController]
        """
        return self._storage_controllers

    @storage_controllers.setter
    def storage_controllers(self, storage_controllers):
        """Sets the storage_controllers of this ComputeBoardAllOf.

        A reference to a storageController resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param storage_controllers: The storage_controllers of this ComputeBoardAllOf.  # noqa: E501
        :type: list[StorageController]
        """

        self._storage_controllers = storage_controllers

    @property
    def storage_flex_flash_controllers(self):
        """Gets the storage_flex_flash_controllers of this ComputeBoardAllOf.  # noqa: E501

        A reference to a storageFlexFlashController resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The storage_flex_flash_controllers of this ComputeBoardAllOf.  # noqa: E501
        :rtype: list[StorageFlexFlashController]
        """
        return self._storage_flex_flash_controllers

    @storage_flex_flash_controllers.setter
    def storage_flex_flash_controllers(self, storage_flex_flash_controllers):
        """Sets the storage_flex_flash_controllers of this ComputeBoardAllOf.

        A reference to a storageFlexFlashController resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param storage_flex_flash_controllers: The storage_flex_flash_controllers of this ComputeBoardAllOf.  # noqa: E501
        :type: list[StorageFlexFlashController]
        """

        self._storage_flex_flash_controllers = storage_flex_flash_controllers

    @property
    def storage_flex_util_controllers(self):
        """Gets the storage_flex_util_controllers of this ComputeBoardAllOf.  # noqa: E501

        A reference to a storageFlexUtilController resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The storage_flex_util_controllers of this ComputeBoardAllOf.  # noqa: E501
        :rtype: list[StorageFlexUtilController]
        """
        return self._storage_flex_util_controllers

    @storage_flex_util_controllers.setter
    def storage_flex_util_controllers(self, storage_flex_util_controllers):
        """Sets the storage_flex_util_controllers of this ComputeBoardAllOf.

        A reference to a storageFlexUtilController resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param storage_flex_util_controllers: The storage_flex_util_controllers of this ComputeBoardAllOf.  # noqa: E501
        :type: list[StorageFlexUtilController]
        """

        self._storage_flex_util_controllers = storage_flex_util_controllers

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
        if not isinstance(other, ComputeBoardAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComputeBoardAllOf):
            return True

        return self.to_dict() != other.to_dict()
