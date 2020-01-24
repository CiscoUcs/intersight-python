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


class CondHclStatus(object):
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
        'component_status': 'str',
        'hardware_status': 'str',
        'hcl_firmware_version': 'str',
        'hcl_model': 'str',
        'hcl_os_vendor': 'str',
        'hcl_os_version': 'str',
        'hcl_processor': 'str',
        'inv_firmware_version': 'str',
        'inv_model': 'str',
        'inv_os_vendor': 'str',
        'inv_os_version': 'str',
        'inv_processor': 'str',
        'reason': 'str',
        'server_reason': 'str',
        'software_status': 'str',
        'status': 'str',
        'details': 'list[CondHclStatusDetail]',
        'managed_object': 'InventoryBase',
        'registered_device': 'AssetDeviceRegistration'
    }

    attribute_map = {
        'component_status': 'ComponentStatus',
        'hardware_status': 'HardwareStatus',
        'hcl_firmware_version': 'HclFirmwareVersion',
        'hcl_model': 'HclModel',
        'hcl_os_vendor': 'HclOsVendor',
        'hcl_os_version': 'HclOsVersion',
        'hcl_processor': 'HclProcessor',
        'inv_firmware_version': 'InvFirmwareVersion',
        'inv_model': 'InvModel',
        'inv_os_vendor': 'InvOsVendor',
        'inv_os_version': 'InvOsVersion',
        'inv_processor': 'InvProcessor',
        'reason': 'Reason',
        'server_reason': 'ServerReason',
        'software_status': 'SoftwareStatus',
        'status': 'Status',
        'details': 'Details',
        'managed_object': 'ManagedObject',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self,
                 component_status='Incomplete',
                 hardware_status='Incomplete',
                 hcl_firmware_version=None,
                 hcl_model=None,
                 hcl_os_vendor=None,
                 hcl_os_version=None,
                 hcl_processor=None,
                 inv_firmware_version=None,
                 inv_model=None,
                 inv_os_vendor=None,
                 inv_os_version=None,
                 inv_processor=None,
                 reason='Missing-Os-Info',
                 server_reason='Missing-Os-Driver-Info',
                 software_status='Incomplete',
                 status='Incomplete',
                 details=None,
                 managed_object=None,
                 registered_device=None,
                 local_vars_configuration=None):  # noqa: E501
        """CondHclStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._component_status = None
        self._hardware_status = None
        self._hcl_firmware_version = None
        self._hcl_model = None
        self._hcl_os_vendor = None
        self._hcl_os_version = None
        self._hcl_processor = None
        self._inv_firmware_version = None
        self._inv_model = None
        self._inv_os_vendor = None
        self._inv_os_version = None
        self._inv_processor = None
        self._reason = None
        self._server_reason = None
        self._software_status = None
        self._status = None
        self._details = None
        self._managed_object = None
        self._registered_device = None
        self.discriminator = None

        if component_status is not None:
            self.component_status = component_status
        if hardware_status is not None:
            self.hardware_status = hardware_status
        if hcl_firmware_version is not None:
            self.hcl_firmware_version = hcl_firmware_version
        if hcl_model is not None:
            self.hcl_model = hcl_model
        if hcl_os_vendor is not None:
            self.hcl_os_vendor = hcl_os_vendor
        if hcl_os_version is not None:
            self.hcl_os_version = hcl_os_version
        if hcl_processor is not None:
            self.hcl_processor = hcl_processor
        if inv_firmware_version is not None:
            self.inv_firmware_version = inv_firmware_version
        if inv_model is not None:
            self.inv_model = inv_model
        if inv_os_vendor is not None:
            self.inv_os_vendor = inv_os_vendor
        if inv_os_version is not None:
            self.inv_os_version = inv_os_version
        if inv_processor is not None:
            self.inv_processor = inv_processor
        if reason is not None:
            self.reason = reason
        if server_reason is not None:
            self.server_reason = server_reason
        if software_status is not None:
            self.software_status = software_status
        if status is not None:
            self.status = status
        if details is not None:
            self.details = details
        if managed_object is not None:
            self.managed_object = managed_object
        if registered_device is not None:
            self.registered_device = registered_device

    @property
    def component_status(self):
        """Gets the component_status of this CondHclStatus.  # noqa: E501

        The overall status for the components found in the HCL. This will provide the HCL validation status for all the components. It can be one of the following. \"Validated\" - all the components hardware/software profiles are listed in the HCL. \"Not-Listed\" - one or more components hardware/software profiles are not listed in the HCL \"Incomplete\" - the components are not evaluated as the server's software/hardware profiles are not listed in the HCL. \"Not-Evaluated\" - The components are not evaluated against the HCL because it is exempted.    # noqa: E501

        :return: The component_status of this CondHclStatus.  # noqa: E501
        :rtype: str
        """
        return self._component_status

    @component_status.setter
    def component_status(self, component_status):
        """Sets the component_status of this CondHclStatus.

        The overall status for the components found in the HCL. This will provide the HCL validation status for all the components. It can be one of the following. \"Validated\" - all the components hardware/software profiles are listed in the HCL. \"Not-Listed\" - one or more components hardware/software profiles are not listed in the HCL \"Incomplete\" - the components are not evaluated as the server's software/hardware profiles are not listed in the HCL. \"Not-Evaluated\" - The components are not evaluated against the HCL because it is exempted.    # noqa: E501

        :param component_status: The component_status of this CondHclStatus.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "Incomplete", "Not-Found", "Not-Listed", "Validated",
            "Not-Evaluated"
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and component_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `component_status` ({0}), must be one of {1}"  # noqa: E501
                .format(component_status, allowed_values))

        self._component_status = component_status

    @property
    def hardware_status(self):
        """Gets the hardware_status of this CondHclStatus.  # noqa: E501

        The server model, processor and firmware are considered as part of the hardware profile for the server. This will provide the HCL validation status for the hardware profile. For the failure reason see the serverReason property. The status can be one of the following \"Validated\" - The server model, processor and firmware combination is listed in the HCL \"Not-Listed\" - The server model, processor and firmware combination is not listed in the HCL. \"Not-Evaluated\" - The server is not evaluated against the HCL because it is exempted.    # noqa: E501

        :return: The hardware_status of this CondHclStatus.  # noqa: E501
        :rtype: str
        """
        return self._hardware_status

    @hardware_status.setter
    def hardware_status(self, hardware_status):
        """Sets the hardware_status of this CondHclStatus.

        The server model, processor and firmware are considered as part of the hardware profile for the server. This will provide the HCL validation status for the hardware profile. For the failure reason see the serverReason property. The status can be one of the following \"Validated\" - The server model, processor and firmware combination is listed in the HCL \"Not-Listed\" - The server model, processor and firmware combination is not listed in the HCL. \"Not-Evaluated\" - The server is not evaluated against the HCL because it is exempted.    # noqa: E501

        :param hardware_status: The hardware_status of this CondHclStatus.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "Incomplete", "Not-Found", "Not-Listed", "Validated",
            "Not-Evaluated"
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and hardware_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `hardware_status` ({0}), must be one of {1}"  # noqa: E501
                .format(hardware_status, allowed_values))

        self._hardware_status = hardware_status

    @property
    def hcl_firmware_version(self):
        """Gets the hcl_firmware_version of this CondHclStatus.  # noqa: E501

        The current CIMC version for the server normalized for querying HCL data. It is empty if we are missing this information.    # noqa: E501

        :return: The hcl_firmware_version of this CondHclStatus.  # noqa: E501
        :rtype: str
        """
        return self._hcl_firmware_version

    @hcl_firmware_version.setter
    def hcl_firmware_version(self, hcl_firmware_version):
        """Sets the hcl_firmware_version of this CondHclStatus.

        The current CIMC version for the server normalized for querying HCL data. It is empty if we are missing this information.    # noqa: E501

        :param hcl_firmware_version: The hcl_firmware_version of this CondHclStatus.  # noqa: E501
        :type: str
        """

        self._hcl_firmware_version = hcl_firmware_version

    @property
    def hcl_model(self):
        """Gets the hcl_model of this CondHclStatus.  # noqa: E501

        The managed object's model to validate normalized for querying HCL data. It is empty if we are missing this information.    # noqa: E501

        :return: The hcl_model of this CondHclStatus.  # noqa: E501
        :rtype: str
        """
        return self._hcl_model

    @hcl_model.setter
    def hcl_model(self, hcl_model):
        """Sets the hcl_model of this CondHclStatus.

        The managed object's model to validate normalized for querying HCL data. It is empty if we are missing this information.    # noqa: E501

        :param hcl_model: The hcl_model of this CondHclStatus.  # noqa: E501
        :type: str
        """

        self._hcl_model = hcl_model

    @property
    def hcl_os_vendor(self):
        """Gets the hcl_os_vendor of this CondHclStatus.  # noqa: E501

        The OS Vendor for the managed object to validate normalized for querying HCL data. It is empty if we are missing this information.    # noqa: E501

        :return: The hcl_os_vendor of this CondHclStatus.  # noqa: E501
        :rtype: str
        """
        return self._hcl_os_vendor

    @hcl_os_vendor.setter
    def hcl_os_vendor(self, hcl_os_vendor):
        """Sets the hcl_os_vendor of this CondHclStatus.

        The OS Vendor for the managed object to validate normalized for querying HCL data. It is empty if we are missing this information.    # noqa: E501

        :param hcl_os_vendor: The hcl_os_vendor of this CondHclStatus.  # noqa: E501
        :type: str
        """

        self._hcl_os_vendor = hcl_os_vendor

    @property
    def hcl_os_version(self):
        """Gets the hcl_os_version of this CondHclStatus.  # noqa: E501

        The OS Version for the managed object to validate normalized for querying HCL data. It is empty if we are missing this information.    # noqa: E501

        :return: The hcl_os_version of this CondHclStatus.  # noqa: E501
        :rtype: str
        """
        return self._hcl_os_version

    @hcl_os_version.setter
    def hcl_os_version(self, hcl_os_version):
        """Sets the hcl_os_version of this CondHclStatus.

        The OS Version for the managed object to validate normalized for querying HCL data. It is empty if we are missing this information.    # noqa: E501

        :param hcl_os_version: The hcl_os_version of this CondHclStatus.  # noqa: E501
        :type: str
        """

        self._hcl_os_version = hcl_os_version

    @property
    def hcl_processor(self):
        """Gets the hcl_processor of this CondHclStatus.  # noqa: E501

        The managed object's processor to validate if applicable normalized for querying HCL data. It is empty if we are missing this information.    # noqa: E501

        :return: The hcl_processor of this CondHclStatus.  # noqa: E501
        :rtype: str
        """
        return self._hcl_processor

    @hcl_processor.setter
    def hcl_processor(self, hcl_processor):
        """Sets the hcl_processor of this CondHclStatus.

        The managed object's processor to validate if applicable normalized for querying HCL data. It is empty if we are missing this information.    # noqa: E501

        :param hcl_processor: The hcl_processor of this CondHclStatus.  # noqa: E501
        :type: str
        """

        self._hcl_processor = hcl_processor

    @property
    def inv_firmware_version(self):
        """Gets the inv_firmware_version of this CondHclStatus.  # noqa: E501

        The current CIMC version for the server as received from inventory. It is empty if we are missing this information.    # noqa: E501

        :return: The inv_firmware_version of this CondHclStatus.  # noqa: E501
        :rtype: str
        """
        return self._inv_firmware_version

    @inv_firmware_version.setter
    def inv_firmware_version(self, inv_firmware_version):
        """Sets the inv_firmware_version of this CondHclStatus.

        The current CIMC version for the server as received from inventory. It is empty if we are missing this information.    # noqa: E501

        :param inv_firmware_version: The inv_firmware_version of this CondHclStatus.  # noqa: E501
        :type: str
        """

        self._inv_firmware_version = inv_firmware_version

    @property
    def inv_model(self):
        """Gets the inv_model of this CondHclStatus.  # noqa: E501

        The managed object's model to validate as received from the inventory. It is empty if we are missing this information.    # noqa: E501

        :return: The inv_model of this CondHclStatus.  # noqa: E501
        :rtype: str
        """
        return self._inv_model

    @inv_model.setter
    def inv_model(self, inv_model):
        """Sets the inv_model of this CondHclStatus.

        The managed object's model to validate as received from the inventory. It is empty if we are missing this information.    # noqa: E501

        :param inv_model: The inv_model of this CondHclStatus.  # noqa: E501
        :type: str
        """

        self._inv_model = inv_model

    @property
    def inv_os_vendor(self):
        """Gets the inv_os_vendor of this CondHclStatus.  # noqa: E501

        The OS Vendor for the managed object to validate as received from inventory. It is empty if we are missing this information.    # noqa: E501

        :return: The inv_os_vendor of this CondHclStatus.  # noqa: E501
        :rtype: str
        """
        return self._inv_os_vendor

    @inv_os_vendor.setter
    def inv_os_vendor(self, inv_os_vendor):
        """Sets the inv_os_vendor of this CondHclStatus.

        The OS Vendor for the managed object to validate as received from inventory. It is empty if we are missing this information.    # noqa: E501

        :param inv_os_vendor: The inv_os_vendor of this CondHclStatus.  # noqa: E501
        :type: str
        """

        self._inv_os_vendor = inv_os_vendor

    @property
    def inv_os_version(self):
        """Gets the inv_os_version of this CondHclStatus.  # noqa: E501

        The OS Version for the managed object to validate as received from inventory. It is empty if we are missing this information.    # noqa: E501

        :return: The inv_os_version of this CondHclStatus.  # noqa: E501
        :rtype: str
        """
        return self._inv_os_version

    @inv_os_version.setter
    def inv_os_version(self, inv_os_version):
        """Sets the inv_os_version of this CondHclStatus.

        The OS Version for the managed object to validate as received from inventory. It is empty if we are missing this information.    # noqa: E501

        :param inv_os_version: The inv_os_version of this CondHclStatus.  # noqa: E501
        :type: str
        """

        self._inv_os_version = inv_os_version

    @property
    def inv_processor(self):
        """Gets the inv_processor of this CondHclStatus.  # noqa: E501

        The managed object's processor to validate if applicable as received from inventory. It is empty if we are missing this information.    # noqa: E501

        :return: The inv_processor of this CondHclStatus.  # noqa: E501
        :rtype: str
        """
        return self._inv_processor

    @inv_processor.setter
    def inv_processor(self, inv_processor):
        """Sets the inv_processor of this CondHclStatus.

        The managed object's processor to validate if applicable as received from inventory. It is empty if we are missing this information.    # noqa: E501

        :param inv_processor: The inv_processor of this CondHclStatus.  # noqa: E501
        :type: str
        """

        self._inv_processor = inv_processor

    @property
    def reason(self):
        """Gets the reason of this CondHclStatus.  # noqa: E501

        The reason for the HCL status. It will be one of the following \"Missing-Os-Info\" - we are missing os information in the inventory from the device connector \"Incompatible-Components\" - we have 1 or more components with \"Not-Validated\" status \"Compatible\" - all the components have \"Validated\" status. \"Not-Evaluated\" - The server is not evaluated against the HCL because it is exempted.    # noqa: E501

        :return: The reason of this CondHclStatus.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this CondHclStatus.

        The reason for the HCL status. It will be one of the following \"Missing-Os-Info\" - we are missing os information in the inventory from the device connector \"Incompatible-Components\" - we have 1 or more components with \"Not-Validated\" status \"Compatible\" - all the components have \"Validated\" status. \"Not-Evaluated\" - The server is not evaluated against the HCL because it is exempted.    # noqa: E501

        :param reason: The reason of this CondHclStatus.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "Missing-Os-Info", "Incompatible-Components", "Compatible",
            "Not-Evaluated"
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and reason not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"  # noqa: E501
                .format(reason, allowed_values))

        self._reason = reason

    @property
    def server_reason(self):
        """Gets the server_reason of this CondHclStatus.  # noqa: E501

        The reason generated by the server's HCL validation. For HCL the evaluation can be seen in three logical stages 1. Evaluate the server's hardware status 2. Evaluate the server's software status 3. Evaluate the server's components (each component has its own hardware/software evaluation) The evaluation does not proceed to the next stage until the previous stage is evaluated. Therefore there can be only one validation reason. \"Incompatible-Server\" - the server model is not listed in the HCL. \"Incompatible-Processor\" - the server model and processor combination is not listed in HCL. \"Incompatible-Firmware\" - the server model, processor and server firmware is not listed in HCL. \"Missing-Os-Info\" - the os vendor and version is not listed in HCL with the HW profile. \"Incompatible-Os-Info\" - the os vendor and version is not listed in HCL with the HW profile. \"Incompatible-Components\" - there is one or more components with \"Not-Validated\" status \"Service-Unavailable\" - HCL data service is unavailable at the moment (try again later). \"Compatible\" - the server and all its components are validated. \"Not-Evaluated\" - The server is not evaluated against the HCL because it is exempted.    # noqa: E501

        :return: The server_reason of this CondHclStatus.  # noqa: E501
        :rtype: str
        """
        return self._server_reason

    @server_reason.setter
    def server_reason(self, server_reason):
        """Sets the server_reason of this CondHclStatus.

        The reason generated by the server's HCL validation. For HCL the evaluation can be seen in three logical stages 1. Evaluate the server's hardware status 2. Evaluate the server's software status 3. Evaluate the server's components (each component has its own hardware/software evaluation) The evaluation does not proceed to the next stage until the previous stage is evaluated. Therefore there can be only one validation reason. \"Incompatible-Server\" - the server model is not listed in the HCL. \"Incompatible-Processor\" - the server model and processor combination is not listed in HCL. \"Incompatible-Firmware\" - the server model, processor and server firmware is not listed in HCL. \"Missing-Os-Info\" - the os vendor and version is not listed in HCL with the HW profile. \"Incompatible-Os-Info\" - the os vendor and version is not listed in HCL with the HW profile. \"Incompatible-Components\" - there is one or more components with \"Not-Validated\" status \"Service-Unavailable\" - HCL data service is unavailable at the moment (try again later). \"Compatible\" - the server and all its components are validated. \"Not-Evaluated\" - The server is not evaluated against the HCL because it is exempted.    # noqa: E501

        :param server_reason: The server_reason of this CondHclStatus.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "Missing-Os-Driver-Info", "Incompatible-Server",
            "Incompatible-Processor", "Incompatible-Os-Info",
            "Incompatible-Firmware", "Service-Unavailable", "Service-Error",
            "Not-Evaluated", "Incompatible-Components", "Compatible"
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and server_reason not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `server_reason` ({0}), must be one of {1}"  # noqa: E501
                .format(server_reason, allowed_values))

        self._server_reason = server_reason

    @property
    def software_status(self):
        """Gets the software_status of this CondHclStatus.  # noqa: E501

        The OS vendor and version are considered part of the software profile for the server. This will provide the HCL validation status for the software profile. For the failure reason see the serverReason property. The status can be be one of the following \"Validated\" - The os vendor/version is listed in the HCL for the server model, processor and firmware \"Not-Listed\" - The os vendor/version is not listed in the HCL for the server model, processor and firmware \"Incomplete\" - The inventory is missing os vendor/version and HCL validation was not performed. \"Not-Evaluated\" - The server is not evaluated against the HCL because it is exempted.    # noqa: E501

        :return: The software_status of this CondHclStatus.  # noqa: E501
        :rtype: str
        """
        return self._software_status

    @software_status.setter
    def software_status(self, software_status):
        """Sets the software_status of this CondHclStatus.

        The OS vendor and version are considered part of the software profile for the server. This will provide the HCL validation status for the software profile. For the failure reason see the serverReason property. The status can be be one of the following \"Validated\" - The os vendor/version is listed in the HCL for the server model, processor and firmware \"Not-Listed\" - The os vendor/version is not listed in the HCL for the server model, processor and firmware \"Incomplete\" - The inventory is missing os vendor/version and HCL validation was not performed. \"Not-Evaluated\" - The server is not evaluated against the HCL because it is exempted.    # noqa: E501

        :param software_status: The software_status of this CondHclStatus.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "Incomplete", "Not-Found", "Not-Listed", "Validated",
            "Not-Evaluated"
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and software_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `software_status` ({0}), must be one of {1}"  # noqa: E501
                .format(software_status, allowed_values))

        self._software_status = software_status

    @property
    def status(self):
        """Gets the status of this CondHclStatus.  # noqa: E501

        The HCL compatibility status of the managed object. The status can be one of the following \"Incomplete\" - there is no enough information to evaluate against the HCL data \"Validated\" - all components have been evaluated against the HCL and they all have \"Validated\" status \"Not-Listed\" - all components have been evaluated against the HCL and one or more have \"Not-Listed\" status. \"Not-Evaluated\" - server is not evaluated against the HCL because it is exempted.     # noqa: E501

        :return: The status of this CondHclStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CondHclStatus.

        The HCL compatibility status of the managed object. The status can be one of the following \"Incomplete\" - there is no enough information to evaluate against the HCL data \"Validated\" - all components have been evaluated against the HCL and they all have \"Validated\" status \"Not-Listed\" - all components have been evaluated against the HCL and one or more have \"Not-Listed\" status. \"Not-Evaluated\" - server is not evaluated against the HCL because it is exempted.     # noqa: E501

        :param status: The status of this CondHclStatus.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "Incomplete", "Not-Found", "Not-Listed", "Validated",
            "Not-Evaluated"
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values))

        self._status = status

    @property
    def details(self):
        """Gets the details of this CondHclStatus.  # noqa: E501

        A reference to a condHclStatusDetail resource. When the $expand query parameter is specified, the referenced resource is returned inline. The collection of all the detailed related components for which we performed HCL validation.   # noqa: E501

        :return: The details of this CondHclStatus.  # noqa: E501
        :rtype: list[CondHclStatusDetail]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this CondHclStatus.

        A reference to a condHclStatusDetail resource. When the $expand query parameter is specified, the referenced resource is returned inline. The collection of all the detailed related components for which we performed HCL validation.   # noqa: E501

        :param details: The details of this CondHclStatus.  # noqa: E501
        :type: list[CondHclStatusDetail]
        """

        self._details = details

    @property
    def managed_object(self):
        """Gets the managed_object of this CondHclStatus.  # noqa: E501


        :return: The managed_object of this CondHclStatus.  # noqa: E501
        :rtype: InventoryBase
        """
        return self._managed_object

    @managed_object.setter
    def managed_object(self, managed_object):
        """Sets the managed_object of this CondHclStatus.


        :param managed_object: The managed_object of this CondHclStatus.  # noqa: E501
        :type: InventoryBase
        """

        self._managed_object = managed_object

    @property
    def registered_device(self):
        """Gets the registered_device of this CondHclStatus.  # noqa: E501


        :return: The registered_device of this CondHclStatus.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this CondHclStatus.


        :param registered_device: The registered_device of this CondHclStatus.  # noqa: E501
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
        if not isinstance(other, CondHclStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CondHclStatus):
            return True

        return self.to_dict() != other.to_dict()
