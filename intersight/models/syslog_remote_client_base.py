# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1461
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SyslogRemoteClientBase(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'object_type': 'str',
        'enabled': 'bool',
        'hostname': 'str',
        'min_severity': 'str',
        'port': 'int',
        'protocol': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'enabled': 'Enabled',
        'hostname': 'Hostname',
        'min_severity': 'MinSeverity',
        'port': 'Port',
        'protocol': 'Protocol'
    }

    def __init__(self, object_type=None, enabled=None, hostname=None, min_severity='warning', port=None, protocol='udp'):
        """
        SyslogRemoteClientBase - a model defined in Swagger
        """

        self._object_type = None
        self._enabled = None
        self._hostname = None
        self._min_severity = None
        self._port = None
        self._protocol = None

        if object_type is not None:
          self.object_type = object_type
        if enabled is not None:
          self.enabled = enabled
        if hostname is not None:
          self.hostname = hostname
        if min_severity is not None:
          self.min_severity = min_severity
        if port is not None:
          self.port = port
        if protocol is not None:
          self.protocol = protocol

    @property
    def object_type(self):
        """
        Gets the object_type of this SyslogRemoteClientBase.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :return: The object_type of this SyslogRemoteClientBase.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this SyslogRemoteClientBase.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :param object_type: The object_type of this SyslogRemoteClientBase.
        :type: str
        """

        self._object_type = object_type

    @property
    def enabled(self):
        """
        Gets the enabled of this SyslogRemoteClientBase.
        Enables/disables remote logging for the endpoint If enabled, log messages will be sent to the syslog server mentioned in the Hostname/IP Address field.

        :return: The enabled of this SyslogRemoteClientBase.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this SyslogRemoteClientBase.
        Enables/disables remote logging for the endpoint If enabled, log messages will be sent to the syslog server mentioned in the Hostname/IP Address field.

        :param enabled: The enabled of this SyslogRemoteClientBase.
        :type: bool
        """

        self._enabled = enabled

    @property
    def hostname(self):
        """
        Gets the hostname of this SyslogRemoteClientBase.
        Hostname or IP Address of the syslog server where log should be stored.

        :return: The hostname of this SyslogRemoteClientBase.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this SyslogRemoteClientBase.
        Hostname or IP Address of the syslog server where log should be stored.

        :param hostname: The hostname of this SyslogRemoteClientBase.
        :type: str
        """

        self._hostname = hostname

    @property
    def min_severity(self):
        """
        Gets the min_severity of this SyslogRemoteClientBase.
        Lowest level of messages to be included in the remote log.

        :return: The min_severity of this SyslogRemoteClientBase.
        :rtype: str
        """
        return self._min_severity

    @min_severity.setter
    def min_severity(self, min_severity):
        """
        Sets the min_severity of this SyslogRemoteClientBase.
        Lowest level of messages to be included in the remote log.

        :param min_severity: The min_severity of this SyslogRemoteClientBase.
        :type: str
        """
        allowed_values = ["warning", "emergency", "alert", "critical", "error", "notice", "informational", "debug"]
        if min_severity not in allowed_values:
            raise ValueError(
                "Invalid value for `min_severity` ({0}), must be one of {1}"
                .format(min_severity, allowed_values)
            )

        self._min_severity = min_severity

    @property
    def port(self):
        """
        Gets the port of this SyslogRemoteClientBase.
        Port number used for logging on syslog server.

        :return: The port of this SyslogRemoteClientBase.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this SyslogRemoteClientBase.
        Port number used for logging on syslog server.

        :param port: The port of this SyslogRemoteClientBase.
        :type: int
        """

        self._port = port

    @property
    def protocol(self):
        """
        Gets the protocol of this SyslogRemoteClientBase.
        Transport layer protocol for transmission of log messages to syslog server.

        :return: The protocol of this SyslogRemoteClientBase.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this SyslogRemoteClientBase.
        Transport layer protocol for transmission of log messages to syslog server.

        :param protocol: The protocol of this SyslogRemoteClientBase.
        :type: str
        """
        allowed_values = ["udp", "tcp"]
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SyslogRemoteClientBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
