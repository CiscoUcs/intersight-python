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


class ApplianceBackupBase(object):
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
        'filename': 'str',
        'protocol': 'str',
        'remote_host': 'str',
        'remote_path': 'str',
        'remote_port': 'int',
        'username': 'str'
    }

    attribute_map = {
        'filename': 'Filename',
        'protocol': 'Protocol',
        'remote_host': 'RemoteHost',
        'remote_path': 'RemotePath',
        'remote_port': 'RemotePort',
        'username': 'Username'
    }

    def __init__(self,
                 filename=None,
                 protocol='scp',
                 remote_host=None,
                 remote_path=None,
                 remote_port=None,
                 username=None,
                 local_vars_configuration=None):  # noqa: E501
        """ApplianceBackupBase - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._filename = None
        self._protocol = None
        self._remote_host = None
        self._remote_path = None
        self._remote_port = None
        self._username = None
        self.discriminator = None

        if filename is not None:
            self.filename = filename
        if protocol is not None:
            self.protocol = protocol
        if remote_host is not None:
            self.remote_host = remote_host
        if remote_path is not None:
            self.remote_path = remote_path
        if remote_port is not None:
            self.remote_port = remote_port
        if username is not None:
            self.username = username

    @property
    def filename(self):
        """Gets the filename of this ApplianceBackupBase.  # noqa: E501

        Backup filename to backup or restore.    # noqa: E501

        :return: The filename of this ApplianceBackupBase.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this ApplianceBackupBase.

        Backup filename to backup or restore.    # noqa: E501

        :param filename: The filename of this ApplianceBackupBase.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def protocol(self):
        """Gets the protocol of this ApplianceBackupBase.  # noqa: E501

        Communication protocol used by the file server (e.g. scp or sftp).    # noqa: E501

        :return: The protocol of this ApplianceBackupBase.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ApplianceBackupBase.

        Communication protocol used by the file server (e.g. scp or sftp).    # noqa: E501

        :param protocol: The protocol of this ApplianceBackupBase.  # noqa: E501
        :type: str
        """
        allowed_values = ["scp", "sftp"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and protocol not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values))

        self._protocol = protocol

    @property
    def remote_host(self):
        """Gets the remote_host of this ApplianceBackupBase.  # noqa: E501

        Hostname of the remote file server.    # noqa: E501

        :return: The remote_host of this ApplianceBackupBase.  # noqa: E501
        :rtype: str
        """
        return self._remote_host

    @remote_host.setter
    def remote_host(self, remote_host):
        """Sets the remote_host of this ApplianceBackupBase.

        Hostname of the remote file server.    # noqa: E501

        :param remote_host: The remote_host of this ApplianceBackupBase.  # noqa: E501
        :type: str
        """

        self._remote_host = remote_host

    @property
    def remote_path(self):
        """Gets the remote_path of this ApplianceBackupBase.  # noqa: E501

        File server directory to copy the file.    # noqa: E501

        :return: The remote_path of this ApplianceBackupBase.  # noqa: E501
        :rtype: str
        """
        return self._remote_path

    @remote_path.setter
    def remote_path(self, remote_path):
        """Sets the remote_path of this ApplianceBackupBase.

        File server directory to copy the file.    # noqa: E501

        :param remote_path: The remote_path of this ApplianceBackupBase.  # noqa: E501
        :type: str
        """

        self._remote_path = remote_path

    @property
    def remote_port(self):
        """Gets the remote_port of this ApplianceBackupBase.  # noqa: E501

        Remote TCP port on the file server (e.g. 22 for scp).    # noqa: E501

        :return: The remote_port of this ApplianceBackupBase.  # noqa: E501
        :rtype: int
        """
        return self._remote_port

    @remote_port.setter
    def remote_port(self, remote_port):
        """Sets the remote_port of this ApplianceBackupBase.

        Remote TCP port on the file server (e.g. 22 for scp).    # noqa: E501

        :param remote_port: The remote_port of this ApplianceBackupBase.  # noqa: E501
        :type: int
        """

        self._remote_port = remote_port

    @property
    def username(self):
        """Gets the username of this ApplianceBackupBase.  # noqa: E501

        Username to authenticate the fileserver.     # noqa: E501

        :return: The username of this ApplianceBackupBase.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ApplianceBackupBase.

        Username to authenticate the fileserver.     # noqa: E501

        :param username: The username of this ApplianceBackupBase.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if not isinstance(other, ApplianceBackupBase):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplianceBackupBase):
            return True

        return self.to_dict() != other.to_dict()
