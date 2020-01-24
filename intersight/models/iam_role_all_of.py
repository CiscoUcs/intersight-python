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


class IamRoleAllOf(object):
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
        'privilege_names': 'list[str]',
        'account': 'IamAccount',
        'privilege_sets': 'list[IamPrivilegeSet]',
        'system': 'IamSystem'
    }

    attribute_map = {
        'description': 'Description',
        'name': 'Name',
        'privilege_names': 'PrivilegeNames',
        'account': 'Account',
        'privilege_sets': 'PrivilegeSets',
        'system': 'System'
    }

    def __init__(self,
                 description=None,
                 name=None,
                 privilege_names=None,
                 account=None,
                 privilege_sets=None,
                 system=None,
                 local_vars_configuration=None):  # noqa: E501
        """IamRoleAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._name = None
        self._privilege_names = None
        self._account = None
        self._privilege_sets = None
        self._system = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if privilege_names is not None:
            self.privilege_names = privilege_names
        if account is not None:
            self.account = account
        if privilege_sets is not None:
            self.privilege_sets = privilege_sets
        if system is not None:
            self.system = system

    @property
    def description(self):
        """Gets the description of this IamRoleAllOf.  # noqa: E501

        Informative description about each role.    # noqa: E501

        :return: The description of this IamRoleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IamRoleAllOf.

        Informative description about each role.    # noqa: E501

        :param description: The description of this IamRoleAllOf.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this IamRoleAllOf.  # noqa: E501

        The name of the role which has to be granted to user.    # noqa: E501

        :return: The name of this IamRoleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IamRoleAllOf.

        The name of the role which has to be granted to user.    # noqa: E501

        :param name: The name of this IamRoleAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def privilege_names(self):
        """Gets the privilege_names of this IamRoleAllOf.  # noqa: E501


        :return: The privilege_names of this IamRoleAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._privilege_names

    @privilege_names.setter
    def privilege_names(self, privilege_names):
        """Sets the privilege_names of this IamRoleAllOf.


        :param privilege_names: The privilege_names of this IamRoleAllOf.  # noqa: E501
        :type: list[str]
        """

        self._privilege_names = privilege_names

    @property
    def account(self):
        """Gets the account of this IamRoleAllOf.  # noqa: E501


        :return: The account of this IamRoleAllOf.  # noqa: E501
        :rtype: IamAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this IamRoleAllOf.


        :param account: The account of this IamRoleAllOf.  # noqa: E501
        :type: IamAccount
        """

        self._account = account

    @property
    def privilege_sets(self):
        """Gets the privilege_sets of this IamRoleAllOf.  # noqa: E501

        A reference to a iamPrivilegeSet resource. When the $expand query parameter is specified, the referenced resource is returned inline. Reference to the privilege sets. Privilege set is a collection of privileges. Privilege sets are assigned to a user using roles.   # noqa: E501

        :return: The privilege_sets of this IamRoleAllOf.  # noqa: E501
        :rtype: list[IamPrivilegeSet]
        """
        return self._privilege_sets

    @privilege_sets.setter
    def privilege_sets(self, privilege_sets):
        """Sets the privilege_sets of this IamRoleAllOf.

        A reference to a iamPrivilegeSet resource. When the $expand query parameter is specified, the referenced resource is returned inline. Reference to the privilege sets. Privilege set is a collection of privileges. Privilege sets are assigned to a user using roles.   # noqa: E501

        :param privilege_sets: The privilege_sets of this IamRoleAllOf.  # noqa: E501
        :type: list[IamPrivilegeSet]
        """

        self._privilege_sets = privilege_sets

    @property
    def system(self):
        """Gets the system of this IamRoleAllOf.  # noqa: E501


        :return: The system of this IamRoleAllOf.  # noqa: E501
        :rtype: IamSystem
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this IamRoleAllOf.


        :param system: The system of this IamRoleAllOf.  # noqa: E501
        :type: IamSystem
        """

        self._system = system

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
        if not isinstance(other, IamRoleAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IamRoleAllOf):
            return True

        return self.to_dict() != other.to_dict()
