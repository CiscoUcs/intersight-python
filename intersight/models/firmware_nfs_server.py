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


class FirmwareNfsServer(object):
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
        'mount_options': 'str',
        'remote_file': 'str',
        'remote_ip': 'str',
        'remote_share': 'str'
    }

    attribute_map = {
        'mount_options': 'MountOptions',
        'remote_file': 'RemoteFile',
        'remote_ip': 'RemoteIp',
        'remote_share': 'RemoteShare'
    }

    def __init__(self,
                 mount_options=None,
                 remote_file=None,
                 remote_ip=None,
                 remote_share=None,
                 local_vars_configuration=None):  # noqa: E501
        """FirmwareNfsServer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mount_options = None
        self._remote_file = None
        self._remote_ip = None
        self._remote_share = None
        self.discriminator = None

        if mount_options is not None:
            self.mount_options = mount_options
        if remote_file is not None:
            self.remote_file = remote_file
        if remote_ip is not None:
            self.remote_ip = remote_ip
        if remote_share is not None:
            self.remote_share = remote_share

    @property
    def mount_options(self):
        """Gets the mount_options of this FirmwareNfsServer.  # noqa: E501

        Mount option as configured on the NFS Server. Example:nolock.    # noqa: E501

        :return: The mount_options of this FirmwareNfsServer.  # noqa: E501
        :rtype: str
        """
        return self._mount_options

    @mount_options.setter
    def mount_options(self, mount_options):
        """Sets the mount_options of this FirmwareNfsServer.

        Mount option as configured on the NFS Server. Example:nolock.    # noqa: E501

        :param mount_options: The mount_options of this FirmwareNfsServer.  # noqa: E501
        :type: str
        """

        self._mount_options = mount_options

    @property
    def remote_file(self):
        """Gets the remote_file of this FirmwareNfsServer.  # noqa: E501

        Filename of the image in the remote share location. Example:ucs-c220m5-huu-3.1.2c.iso.    # noqa: E501

        :return: The remote_file of this FirmwareNfsServer.  # noqa: E501
        :rtype: str
        """
        return self._remote_file

    @remote_file.setter
    def remote_file(self, remote_file):
        """Sets the remote_file of this FirmwareNfsServer.

        Filename of the image in the remote share location. Example:ucs-c220m5-huu-3.1.2c.iso.    # noqa: E501

        :param remote_file: The remote_file of this FirmwareNfsServer.  # noqa: E501
        :type: str
        """

        self._remote_file = remote_file

    @property
    def remote_ip(self):
        """Gets the remote_ip of this FirmwareNfsServer.  # noqa: E501

        NFS Server Hostname or IP Address. Example:NFS-server-hostname or 10.10.8.7.    # noqa: E501

        :return: The remote_ip of this FirmwareNfsServer.  # noqa: E501
        :rtype: str
        """
        return self._remote_ip

    @remote_ip.setter
    def remote_ip(self, remote_ip):
        """Sets the remote_ip of this FirmwareNfsServer.

        NFS Server Hostname or IP Address. Example:NFS-server-hostname or 10.10.8.7.    # noqa: E501

        :param remote_ip: The remote_ip of this FirmwareNfsServer.  # noqa: E501
        :type: str
        """

        self._remote_ip = remote_ip

    @property
    def remote_share(self):
        """Gets the remote_share of this FirmwareNfsServer.  # noqa: E501

        Directory where the image is stored. Example:/share/subfolder.     # noqa: E501

        :return: The remote_share of this FirmwareNfsServer.  # noqa: E501
        :rtype: str
        """
        return self._remote_share

    @remote_share.setter
    def remote_share(self, remote_share):
        """Sets the remote_share of this FirmwareNfsServer.

        Directory where the image is stored. Example:/share/subfolder.     # noqa: E501

        :param remote_share: The remote_share of this FirmwareNfsServer.  # noqa: E501
        :type: str
        """

        self._remote_share = remote_share

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
        if not isinstance(other, FirmwareNfsServer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FirmwareNfsServer):
            return True

        return self.to_dict() != other.to_dict()
