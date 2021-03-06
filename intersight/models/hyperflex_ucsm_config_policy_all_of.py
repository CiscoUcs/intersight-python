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


class HyperflexUcsmConfigPolicyAllOf(object):
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
        'kvm_ip_range': 'HyperflexIpAddrRange',
        'mac_prefix_range': 'HyperflexMacAddrPrefixRange',
        'server_firmware_version': 'str',
        'cluster_profiles': 'list[HyperflexClusterProfile]',
        'organization': 'OrganizationOrganization'
    }

    attribute_map = {
        'kvm_ip_range': 'KvmIpRange',
        'mac_prefix_range': 'MacPrefixRange',
        'server_firmware_version': 'ServerFirmwareVersion',
        'cluster_profiles': 'ClusterProfiles',
        'organization': 'Organization'
    }

    def __init__(self,
                 kvm_ip_range=None,
                 mac_prefix_range=None,
                 server_firmware_version=None,
                 cluster_profiles=None,
                 organization=None,
                 local_vars_configuration=None):  # noqa: E501
        """HyperflexUcsmConfigPolicyAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kvm_ip_range = None
        self._mac_prefix_range = None
        self._server_firmware_version = None
        self._cluster_profiles = None
        self._organization = None
        self.discriminator = None

        if kvm_ip_range is not None:
            self.kvm_ip_range = kvm_ip_range
        if mac_prefix_range is not None:
            self.mac_prefix_range = mac_prefix_range
        if server_firmware_version is not None:
            self.server_firmware_version = server_firmware_version
        if cluster_profiles is not None:
            self.cluster_profiles = cluster_profiles
        if organization is not None:
            self.organization = organization

    @property
    def kvm_ip_range(self):
        """Gets the kvm_ip_range of this HyperflexUcsmConfigPolicyAllOf.  # noqa: E501


        :return: The kvm_ip_range of this HyperflexUcsmConfigPolicyAllOf.  # noqa: E501
        :rtype: HyperflexIpAddrRange
        """
        return self._kvm_ip_range

    @kvm_ip_range.setter
    def kvm_ip_range(self, kvm_ip_range):
        """Sets the kvm_ip_range of this HyperflexUcsmConfigPolicyAllOf.


        :param kvm_ip_range: The kvm_ip_range of this HyperflexUcsmConfigPolicyAllOf.  # noqa: E501
        :type: HyperflexIpAddrRange
        """

        self._kvm_ip_range = kvm_ip_range

    @property
    def mac_prefix_range(self):
        """Gets the mac_prefix_range of this HyperflexUcsmConfigPolicyAllOf.  # noqa: E501


        :return: The mac_prefix_range of this HyperflexUcsmConfigPolicyAllOf.  # noqa: E501
        :rtype: HyperflexMacAddrPrefixRange
        """
        return self._mac_prefix_range

    @mac_prefix_range.setter
    def mac_prefix_range(self, mac_prefix_range):
        """Sets the mac_prefix_range of this HyperflexUcsmConfigPolicyAllOf.


        :param mac_prefix_range: The mac_prefix_range of this HyperflexUcsmConfigPolicyAllOf.  # noqa: E501
        :type: HyperflexMacAddrPrefixRange
        """

        self._mac_prefix_range = mac_prefix_range

    @property
    def server_firmware_version(self):
        """Gets the server_firmware_version of this HyperflexUcsmConfigPolicyAllOf.  # noqa: E501

        The server firmware bundle version used for server components such as CIMC, adapters, BIOS, etc.     # noqa: E501

        :return: The server_firmware_version of this HyperflexUcsmConfigPolicyAllOf.  # noqa: E501
        :rtype: str
        """
        return self._server_firmware_version

    @server_firmware_version.setter
    def server_firmware_version(self, server_firmware_version):
        """Sets the server_firmware_version of this HyperflexUcsmConfigPolicyAllOf.

        The server firmware bundle version used for server components such as CIMC, adapters, BIOS, etc.     # noqa: E501

        :param server_firmware_version: The server_firmware_version of this HyperflexUcsmConfigPolicyAllOf.  # noqa: E501
        :type: str
        """

        self._server_firmware_version = server_firmware_version

    @property
    def cluster_profiles(self):
        """Gets the cluster_profiles of this HyperflexUcsmConfigPolicyAllOf.  # noqa: E501

        A reference to a hyperflexClusterProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of cluster profiles using this policy.   # noqa: E501

        :return: The cluster_profiles of this HyperflexUcsmConfigPolicyAllOf.  # noqa: E501
        :rtype: list[HyperflexClusterProfile]
        """
        return self._cluster_profiles

    @cluster_profiles.setter
    def cluster_profiles(self, cluster_profiles):
        """Sets the cluster_profiles of this HyperflexUcsmConfigPolicyAllOf.

        A reference to a hyperflexClusterProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of cluster profiles using this policy.   # noqa: E501

        :param cluster_profiles: The cluster_profiles of this HyperflexUcsmConfigPolicyAllOf.  # noqa: E501
        :type: list[HyperflexClusterProfile]
        """

        self._cluster_profiles = cluster_profiles

    @property
    def organization(self):
        """Gets the organization of this HyperflexUcsmConfigPolicyAllOf.  # noqa: E501


        :return: The organization of this HyperflexUcsmConfigPolicyAllOf.  # noqa: E501
        :rtype: OrganizationOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this HyperflexUcsmConfigPolicyAllOf.


        :param organization: The organization of this HyperflexUcsmConfigPolicyAllOf.  # noqa: E501
        :type: OrganizationOrganization
        """

        self._organization = organization

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
        if not isinstance(other, HyperflexUcsmConfigPolicyAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HyperflexUcsmConfigPolicyAllOf):
            return True

        return self.to_dict() != other.to_dict()
