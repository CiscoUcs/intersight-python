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


class IamAccountPermissionsAllOf(object):
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
        'account_identifier': 'str',
        'account_name': 'str',
        'account_status': 'str',
        'permissions': 'list[IamPermissionReference]'
    }

    attribute_map = {
        'account_identifier': 'AccountIdentifier',
        'account_name': 'AccountName',
        'account_status': 'AccountStatus',
        'permissions': 'Permissions'
    }

    def __init__(self,
                 account_identifier=None,
                 account_name=None,
                 account_status=None,
                 permissions=None,
                 local_vars_configuration=None):  # noqa: E501
        """IamAccountPermissionsAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_identifier = None
        self._account_name = None
        self._account_status = None
        self._permissions = None
        self.discriminator = None

        if account_identifier is not None:
            self.account_identifier = account_identifier
        if account_name is not None:
            self.account_name = account_name
        if account_status is not None:
            self.account_status = account_status
        if permissions is not None:
            self.permissions = permissions

    @property
    def account_identifier(self):
        """Gets the account_identifier of this IamAccountPermissionsAllOf.  # noqa: E501

        MOID of the account which a user can select after authentication.    # noqa: E501

        :return: The account_identifier of this IamAccountPermissionsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this IamAccountPermissionsAllOf.

        MOID of the account which a user can select after authentication.    # noqa: E501

        :param account_identifier: The account_identifier of this IamAccountPermissionsAllOf.  # noqa: E501
        :type: str
        """

        self._account_identifier = account_identifier

    @property
    def account_name(self):
        """Gets the account_name of this IamAccountPermissionsAllOf.  # noqa: E501

        Name of the account which a user can select after authentication.    # noqa: E501

        :return: The account_name of this IamAccountPermissionsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this IamAccountPermissionsAllOf.

        Name of the account which a user can select after authentication.    # noqa: E501

        :param account_name: The account_name of this IamAccountPermissionsAllOf.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def account_status(self):
        """Gets the account_status of this IamAccountPermissionsAllOf.  # noqa: E501

        Status of the account. Account remains inactive until a device is claimed to the account.    # noqa: E501

        :return: The account_status of this IamAccountPermissionsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._account_status

    @account_status.setter
    def account_status(self, account_status):
        """Sets the account_status of this IamAccountPermissionsAllOf.

        Status of the account. Account remains inactive until a device is claimed to the account.    # noqa: E501

        :param account_status: The account_status of this IamAccountPermissionsAllOf.  # noqa: E501
        :type: str
        """

        self._account_status = account_status

    @property
    def permissions(self):
        """Gets the permissions of this IamAccountPermissionsAllOf.  # noqa: E501


        :return: The permissions of this IamAccountPermissionsAllOf.  # noqa: E501
        :rtype: list[IamPermissionReference]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this IamAccountPermissionsAllOf.


        :param permissions: The permissions of this IamAccountPermissionsAllOf.  # noqa: E501
        :type: list[IamPermissionReference]
        """

        self._permissions = permissions

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
        if not isinstance(other, IamAccountPermissionsAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IamAccountPermissionsAllOf):
            return True

        return self.to_dict() != other.to_dict()
