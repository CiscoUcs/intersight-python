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


class StorageStoragePolicy(object):
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
        'global_hot_spares': 'list[StorageLocalDisk]',
        'retain_policy_virtual_drives': 'bool',
        'unused_disks_state': 'str',
        'virtual_drives': 'list[StorageVirtualDriveConfig]',
        'disk_group_policies': 'list[StorageDiskGroupPolicy]',
        'organization': 'OrganizationOrganization',
        'profiles': 'list[PolicyAbstractConfigProfile]'
    }

    attribute_map = {
        'global_hot_spares': 'GlobalHotSpares',
        'retain_policy_virtual_drives': 'RetainPolicyVirtualDrives',
        'unused_disks_state': 'UnusedDisksState',
        'virtual_drives': 'VirtualDrives',
        'disk_group_policies': 'DiskGroupPolicies',
        'organization': 'Organization',
        'profiles': 'Profiles'
    }

    def __init__(self,
                 global_hot_spares=None,
                 retain_policy_virtual_drives=None,
                 unused_disks_state='UnconfiguredGood',
                 virtual_drives=None,
                 disk_group_policies=None,
                 organization=None,
                 profiles=None,
                 local_vars_configuration=None):  # noqa: E501
        """StorageStoragePolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._global_hot_spares = None
        self._retain_policy_virtual_drives = None
        self._unused_disks_state = None
        self._virtual_drives = None
        self._disk_group_policies = None
        self._organization = None
        self._profiles = None
        self.discriminator = None

        if global_hot_spares is not None:
            self.global_hot_spares = global_hot_spares
        if retain_policy_virtual_drives is not None:
            self.retain_policy_virtual_drives = retain_policy_virtual_drives
        if unused_disks_state is not None:
            self.unused_disks_state = unused_disks_state
        if virtual_drives is not None:
            self.virtual_drives = virtual_drives
        if disk_group_policies is not None:
            self.disk_group_policies = disk_group_policies
        if organization is not None:
            self.organization = organization
        if profiles is not None:
            self.profiles = profiles

    @property
    def global_hot_spares(self):
        """Gets the global_hot_spares of this StorageStoragePolicy.  # noqa: E501


        :return: The global_hot_spares of this StorageStoragePolicy.  # noqa: E501
        :rtype: list[StorageLocalDisk]
        """
        return self._global_hot_spares

    @global_hot_spares.setter
    def global_hot_spares(self, global_hot_spares):
        """Sets the global_hot_spares of this StorageStoragePolicy.


        :param global_hot_spares: The global_hot_spares of this StorageStoragePolicy.  # noqa: E501
        :type: list[StorageLocalDisk]
        """

        self._global_hot_spares = global_hot_spares

    @property
    def retain_policy_virtual_drives(self):
        """Gets the retain_policy_virtual_drives of this StorageStoragePolicy.  # noqa: E501

        Retains the virtual drives defined in policy if they exist already. If this flag is false, the existing virtual drives are removed and created again based on virtual drives in the policy.     # noqa: E501

        :return: The retain_policy_virtual_drives of this StorageStoragePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._retain_policy_virtual_drives

    @retain_policy_virtual_drives.setter
    def retain_policy_virtual_drives(self, retain_policy_virtual_drives):
        """Sets the retain_policy_virtual_drives of this StorageStoragePolicy.

        Retains the virtual drives defined in policy if they exist already. If this flag is false, the existing virtual drives are removed and created again based on virtual drives in the policy.     # noqa: E501

        :param retain_policy_virtual_drives: The retain_policy_virtual_drives of this StorageStoragePolicy.  # noqa: E501
        :type: bool
        """

        self._retain_policy_virtual_drives = retain_policy_virtual_drives

    @property
    def unused_disks_state(self):
        """Gets the unused_disks_state of this StorageStoragePolicy.  # noqa: E501

        This is used to specify the state, unconfigured good or jbod, in which the disks that are not used in this policy should be moved.    # noqa: E501

        :return: The unused_disks_state of this StorageStoragePolicy.  # noqa: E501
        :rtype: str
        """
        return self._unused_disks_state

    @unused_disks_state.setter
    def unused_disks_state(self, unused_disks_state):
        """Sets the unused_disks_state of this StorageStoragePolicy.

        This is used to specify the state, unconfigured good or jbod, in which the disks that are not used in this policy should be moved.    # noqa: E501

        :param unused_disks_state: The unused_disks_state of this StorageStoragePolicy.  # noqa: E501
        :type: str
        """
        allowed_values = ["UnconfiguredGood", "Jbod"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and unused_disks_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `unused_disks_state` ({0}), must be one of {1}"  # noqa: E501
                .format(unused_disks_state, allowed_values))

        self._unused_disks_state = unused_disks_state

    @property
    def virtual_drives(self):
        """Gets the virtual_drives of this StorageStoragePolicy.  # noqa: E501


        :return: The virtual_drives of this StorageStoragePolicy.  # noqa: E501
        :rtype: list[StorageVirtualDriveConfig]
        """
        return self._virtual_drives

    @virtual_drives.setter
    def virtual_drives(self, virtual_drives):
        """Sets the virtual_drives of this StorageStoragePolicy.


        :param virtual_drives: The virtual_drives of this StorageStoragePolicy.  # noqa: E501
        :type: list[StorageVirtualDriveConfig]
        """

        self._virtual_drives = virtual_drives

    @property
    def disk_group_policies(self):
        """Gets the disk_group_policies of this StorageStoragePolicy.  # noqa: E501

        A reference to a storageDiskGroupPolicy resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the used disk group policies.   # noqa: E501

        :return: The disk_group_policies of this StorageStoragePolicy.  # noqa: E501
        :rtype: list[StorageDiskGroupPolicy]
        """
        return self._disk_group_policies

    @disk_group_policies.setter
    def disk_group_policies(self, disk_group_policies):
        """Sets the disk_group_policies of this StorageStoragePolicy.

        A reference to a storageDiskGroupPolicy resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the used disk group policies.   # noqa: E501

        :param disk_group_policies: The disk_group_policies of this StorageStoragePolicy.  # noqa: E501
        :type: list[StorageDiskGroupPolicy]
        """

        self._disk_group_policies = disk_group_policies

    @property
    def organization(self):
        """Gets the organization of this StorageStoragePolicy.  # noqa: E501


        :return: The organization of this StorageStoragePolicy.  # noqa: E501
        :rtype: OrganizationOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this StorageStoragePolicy.


        :param organization: The organization of this StorageStoragePolicy.  # noqa: E501
        :type: OrganizationOrganization
        """

        self._organization = organization

    @property
    def profiles(self):
        """Gets the profiles of this StorageStoragePolicy.  # noqa: E501

        A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the profile objects.   # noqa: E501

        :return: The profiles of this StorageStoragePolicy.  # noqa: E501
        :rtype: list[PolicyAbstractConfigProfile]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """Sets the profiles of this StorageStoragePolicy.

        A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the profile objects.   # noqa: E501

        :param profiles: The profiles of this StorageStoragePolicy.  # noqa: E501
        :type: list[PolicyAbstractConfigProfile]
        """

        self._profiles = profiles

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
        if not isinstance(other, StorageStoragePolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageStoragePolicy):
            return True

        return self.to_dict() != other.to_dict()
