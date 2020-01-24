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


class OrganizationOrganization(object):
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
        'description': 'str',
        'name': 'str',
        'account': 'IamAccount',
        'resource_groups': 'list[ResourceGroup]'
    }

    attribute_map = {
        'description': 'Description',
        'name': 'Name',
        'account': 'Account',
        'resource_groups': 'ResourceGroups'
    }

    def __init__(self,
                 description=None,
                 name=None,
                 account=None,
                 resource_groups=None,
                 local_vars_configuration=None):  # noqa: E501
        """OrganizationOrganization - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._name = None
        self._account = None
        self._resource_groups = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if account is not None:
            self.account = account
        if resource_groups is not None:
            self.resource_groups = resource_groups

    @property
    def description(self):
        """Gets the description of this OrganizationOrganization.  # noqa: E501

        The informative description about the usage of this organization.    # noqa: E501

        :return: The description of this OrganizationOrganization.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OrganizationOrganization.

        The informative description about the usage of this organization.    # noqa: E501

        :param description: The description of this OrganizationOrganization.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this OrganizationOrganization.  # noqa: E501

        The name of the organization. There can be multiple organizations under an account.     # noqa: E501

        :return: The name of this OrganizationOrganization.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationOrganization.

        The name of the organization. There can be multiple organizations under an account.     # noqa: E501

        :param name: The name of this OrganizationOrganization.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def account(self):
        """Gets the account of this OrganizationOrganization.  # noqa: E501


        :return: The account of this OrganizationOrganization.  # noqa: E501
        :rtype: IamAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this OrganizationOrganization.


        :param account: The account of this OrganizationOrganization.  # noqa: E501
        :type: IamAccount
        """

        self._account = account

    @property
    def resource_groups(self):
        """Gets the resource_groups of this OrganizationOrganization.  # noqa: E501

        A reference to a resourceGroup resource. When the $expand query parameter is specified, the referenced resource is returned inline. The resource groups associated with these organization.   # noqa: E501

        :return: The resource_groups of this OrganizationOrganization.  # noqa: E501
        :rtype: list[ResourceGroup]
        """
        return self._resource_groups

    @resource_groups.setter
    def resource_groups(self, resource_groups):
        """Sets the resource_groups of this OrganizationOrganization.

        A reference to a resourceGroup resource. When the $expand query parameter is specified, the referenced resource is returned inline. The resource groups associated with these organization.   # noqa: E501

        :param resource_groups: The resource_groups of this OrganizationOrganization.  # noqa: E501
        :type: list[ResourceGroup]
        """

        self._resource_groups = resource_groups

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
        if not isinstance(other, OrganizationOrganization):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationOrganization):
            return True

        return self.to_dict() != other.to_dict()
