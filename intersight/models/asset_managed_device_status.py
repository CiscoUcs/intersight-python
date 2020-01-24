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


class AssetManagedDeviceStatus(object):
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
        'cloud_port': 'int',
        'connection_failure_reason': 'str',
        'connection_status': 'str',
        'error_code': 'int',
        'error_reason': 'str',
        'process_id': 'int',
        'server_port': 'int',
        'state': 'str'
    }

    attribute_map = {
        'cloud_port': 'CloudPort',
        'connection_failure_reason': 'ConnectionFailureReason',
        'connection_status': 'ConnectionStatus',
        'error_code': 'ErrorCode',
        'error_reason': 'ErrorReason',
        'process_id': 'ProcessId',
        'server_port': 'ServerPort',
        'state': 'State'
    }

    def __init__(self,
                 cloud_port=None,
                 connection_failure_reason=None,
                 connection_status='Unknown',
                 error_code=None,
                 error_reason=None,
                 process_id=None,
                 server_port=None,
                 state='New',
                 local_vars_configuration=None):  # noqa: E501
        """AssetManagedDeviceStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cloud_port = None
        self._connection_failure_reason = None
        self._connection_status = None
        self._error_code = None
        self._error_reason = None
        self._process_id = None
        self._server_port = None
        self._state = None
        self.discriminator = None

        if cloud_port is not None:
            self.cloud_port = cloud_port
        if connection_failure_reason is not None:
            self.connection_failure_reason = connection_failure_reason
        if connection_status is not None:
            self.connection_status = connection_status
        if error_code is not None:
            self.error_code = error_code
        if error_reason is not None:
            self.error_reason = error_reason
        if process_id is not None:
            self.process_id = process_id
        if server_port is not None:
            self.server_port = server_port
        if state is not None:
            self.state = state

    @property
    def cloud_port(self):
        """Gets the cloud_port of this AssetManagedDeviceStatus.  # noqa: E501

        Port used for the connection to the Cloud by the Device Connector for the Managed Device.    # noqa: E501

        :return: The cloud_port of this AssetManagedDeviceStatus.  # noqa: E501
        :rtype: int
        """
        return self._cloud_port

    @cloud_port.setter
    def cloud_port(self, cloud_port):
        """Sets the cloud_port of this AssetManagedDeviceStatus.

        Port used for the connection to the Cloud by the Device Connector for the Managed Device.    # noqa: E501

        :param cloud_port: The cloud_port of this AssetManagedDeviceStatus.  # noqa: E501
        :type: int
        """

        self._cloud_port = cloud_port

    @property
    def connection_failure_reason(self):
        """Gets the connection_failure_reason of this AssetManagedDeviceStatus.  # noqa: E501

        Maintains the reason for the failure of connection to the Device in case of connection failure.    # noqa: E501

        :return: The connection_failure_reason of this AssetManagedDeviceStatus.  # noqa: E501
        :rtype: str
        """
        return self._connection_failure_reason

    @connection_failure_reason.setter
    def connection_failure_reason(self, connection_failure_reason):
        """Sets the connection_failure_reason of this AssetManagedDeviceStatus.

        Maintains the reason for the failure of connection to the Device in case of connection failure.    # noqa: E501

        :param connection_failure_reason: The connection_failure_reason of this AssetManagedDeviceStatus.  # noqa: E501
        :type: str
        """

        self._connection_failure_reason = connection_failure_reason

    @property
    def connection_status(self):
        """Gets the connection_status of this AssetManagedDeviceStatus.  # noqa: E501

        Maintains the status of the connection to the Device.    # noqa: E501

        :return: The connection_status of this AssetManagedDeviceStatus.  # noqa: E501
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """Sets the connection_status of this AssetManagedDeviceStatus.

        Maintains the status of the connection to the Device.    # noqa: E501

        :param connection_status: The connection_status of this AssetManagedDeviceStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unknown", "Success", "Failure"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and connection_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `connection_status` ({0}), must be one of {1}"  # noqa: E501
                .format(connection_status, allowed_values))

        self._connection_status = connection_status

    @property
    def error_code(self):
        """Gets the error_code of this AssetManagedDeviceStatus.  # noqa: E501

        Maintains code related to error from Device Connector, if any.    # noqa: E501

        :return: The error_code of this AssetManagedDeviceStatus.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this AssetManagedDeviceStatus.

        Maintains code related to error from Device Connector, if any.    # noqa: E501

        :param error_code: The error_code of this AssetManagedDeviceStatus.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

    @property
    def error_reason(self):
        """Gets the error_reason of this AssetManagedDeviceStatus.  # noqa: E501

        Maintains the reason for the error from Device Connector, if any.    # noqa: E501

        :return: The error_reason of this AssetManagedDeviceStatus.  # noqa: E501
        :rtype: str
        """
        return self._error_reason

    @error_reason.setter
    def error_reason(self, error_reason):
        """Sets the error_reason of this AssetManagedDeviceStatus.

        Maintains the reason for the error from Device Connector, if any.    # noqa: E501

        :param error_reason: The error_reason of this AssetManagedDeviceStatus.  # noqa: E501
        :type: str
        """

        self._error_reason = error_reason

    @property
    def process_id(self):
        """Gets the process_id of this AssetManagedDeviceStatus.  # noqa: E501

        Maintains the process pid of the Device Connector for the Managed Device.    # noqa: E501

        :return: The process_id of this AssetManagedDeviceStatus.  # noqa: E501
        :rtype: int
        """
        return self._process_id

    @process_id.setter
    def process_id(self, process_id):
        """Sets the process_id of this AssetManagedDeviceStatus.

        Maintains the process pid of the Device Connector for the Managed Device.    # noqa: E501

        :param process_id: The process_id of this AssetManagedDeviceStatus.  # noqa: E501
        :type: int
        """

        self._process_id = process_id

    @property
    def server_port(self):
        """Gets the server_port of this AssetManagedDeviceStatus.  # noqa: E501

        Port used for receiving requests from Intersight Assist by the Device Connector for the Managed Device.    # noqa: E501

        :return: The server_port of this AssetManagedDeviceStatus.  # noqa: E501
        :rtype: int
        """
        return self._server_port

    @server_port.setter
    def server_port(self, server_port):
        """Sets the server_port of this AssetManagedDeviceStatus.

        Port used for receiving requests from Intersight Assist by the Device Connector for the Managed Device.    # noqa: E501

        :param server_port: The server_port of this AssetManagedDeviceStatus.  # noqa: E501
        :type: int
        """

        self._server_port = server_port

    @property
    def state(self):
        """Gets the state of this AssetManagedDeviceStatus.  # noqa: E501

        Maintains the state of the Managed Device, such as Start Success, Start Failure, etc. See ManagedDeviceState for device connection states.     # noqa: E501

        :return: The state of this AssetManagedDeviceStatus.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AssetManagedDeviceStatus.

        Maintains the state of the Managed Device, such as Start Success, Start Failure, etc. See ManagedDeviceState for device connection states.     # noqa: E501

        :param state: The state of this AssetManagedDeviceStatus.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "New", "StartSent", "StartSentFailure", "StartSuccess",
            "StartFailure", "UpdateSentFailure", "UpdateSent",
            "DeleteSentFailure", "DeleteInProgress", "DeleteFailure",
            "DeleteSuccess"
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values))

        self._state = state

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
        if not isinstance(other, AssetManagedDeviceStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetManagedDeviceStatus):
            return True

        return self.to_dict() != other.to_dict()
