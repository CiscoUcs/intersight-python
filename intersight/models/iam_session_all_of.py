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


class IamSessionAllOf(object):
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
        'account_permissions': 'list[IamAccountPermissions]',
        'client_ip_address': 'str',
        'expiration': 'datetime',
        'idle_time_expiration': 'datetime',
        'last_login_client': 'str',
        'last_login_time': 'datetime',
        'permission': 'IamPermission',
        'user': 'IamUser'
    }

    attribute_map = {
        'account_permissions': 'AccountPermissions',
        'client_ip_address': 'ClientIpAddress',
        'expiration': 'Expiration',
        'idle_time_expiration': 'IdleTimeExpiration',
        'last_login_client': 'LastLoginClient',
        'last_login_time': 'LastLoginTime',
        'permission': 'Permission',
        'user': 'User'
    }

    def __init__(self,
                 account_permissions=None,
                 client_ip_address=None,
                 expiration=None,
                 idle_time_expiration=None,
                 last_login_client=None,
                 last_login_time=None,
                 permission=None,
                 user=None,
                 local_vars_configuration=None):  # noqa: E501
        """IamSessionAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_permissions = None
        self._client_ip_address = None
        self._expiration = None
        self._idle_time_expiration = None
        self._last_login_client = None
        self._last_login_time = None
        self._permission = None
        self._user = None
        self.discriminator = None

        if account_permissions is not None:
            self.account_permissions = account_permissions
        if client_ip_address is not None:
            self.client_ip_address = client_ip_address
        if expiration is not None:
            self.expiration = expiration
        if idle_time_expiration is not None:
            self.idle_time_expiration = idle_time_expiration
        if last_login_client is not None:
            self.last_login_client = last_login_client
        if last_login_time is not None:
            self.last_login_time = last_login_time
        if permission is not None:
            self.permission = permission
        if user is not None:
            self.user = user

    @property
    def account_permissions(self):
        """Gets the account_permissions of this IamSessionAllOf.  # noqa: E501


        :return: The account_permissions of this IamSessionAllOf.  # noqa: E501
        :rtype: list[IamAccountPermissions]
        """
        return self._account_permissions

    @account_permissions.setter
    def account_permissions(self, account_permissions):
        """Sets the account_permissions of this IamSessionAllOf.


        :param account_permissions: The account_permissions of this IamSessionAllOf.  # noqa: E501
        :type: list[IamAccountPermissions]
        """

        self._account_permissions = account_permissions

    @property
    def client_ip_address(self):
        """Gets the client_ip_address of this IamSessionAllOf.  # noqa: E501

        The user agent IP address from which the session is launched.    # noqa: E501

        :return: The client_ip_address of this IamSessionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._client_ip_address

    @client_ip_address.setter
    def client_ip_address(self, client_ip_address):
        """Sets the client_ip_address of this IamSessionAllOf.

        The user agent IP address from which the session is launched.    # noqa: E501

        :param client_ip_address: The client_ip_address of this IamSessionAllOf.  # noqa: E501
        :type: str
        """

        self._client_ip_address = client_ip_address

    @property
    def expiration(self):
        """Gets the expiration of this IamSessionAllOf.  # noqa: E501

        Expiration time for the session.    # noqa: E501

        :return: The expiration of this IamSessionAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this IamSessionAllOf.

        Expiration time for the session.    # noqa: E501

        :param expiration: The expiration of this IamSessionAllOf.  # noqa: E501
        :type: datetime
        """

        self._expiration = expiration

    @property
    def idle_time_expiration(self):
        """Gets the idle_time_expiration of this IamSessionAllOf.  # noqa: E501

        Idle time expiration for the session.    # noqa: E501

        :return: The idle_time_expiration of this IamSessionAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._idle_time_expiration

    @idle_time_expiration.setter
    def idle_time_expiration(self, idle_time_expiration):
        """Sets the idle_time_expiration of this IamSessionAllOf.

        Idle time expiration for the session.    # noqa: E501

        :param idle_time_expiration: The idle_time_expiration of this IamSessionAllOf.  # noqa: E501
        :type: datetime
        """

        self._idle_time_expiration = idle_time_expiration

    @property
    def last_login_client(self):
        """Gets the last_login_client of this IamSessionAllOf.  # noqa: E501

        The client address from which last login is initiated.    # noqa: E501

        :return: The last_login_client of this IamSessionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._last_login_client

    @last_login_client.setter
    def last_login_client(self, last_login_client):
        """Sets the last_login_client of this IamSessionAllOf.

        The client address from which last login is initiated.    # noqa: E501

        :param last_login_client: The last_login_client of this IamSessionAllOf.  # noqa: E501
        :type: str
        """

        self._last_login_client = last_login_client

    @property
    def last_login_time(self):
        """Gets the last_login_time of this IamSessionAllOf.  # noqa: E501

        The last login time for user.        # noqa: E501

        :return: The last_login_time of this IamSessionAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login_time

    @last_login_time.setter
    def last_login_time(self, last_login_time):
        """Sets the last_login_time of this IamSessionAllOf.

        The last login time for user.        # noqa: E501

        :param last_login_time: The last_login_time of this IamSessionAllOf.  # noqa: E501
        :type: datetime
        """

        self._last_login_time = last_login_time

    @property
    def permission(self):
        """Gets the permission of this IamSessionAllOf.  # noqa: E501


        :return: The permission of this IamSessionAllOf.  # noqa: E501
        :rtype: IamPermission
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this IamSessionAllOf.


        :param permission: The permission of this IamSessionAllOf.  # noqa: E501
        :type: IamPermission
        """

        self._permission = permission

    @property
    def user(self):
        """Gets the user of this IamSessionAllOf.  # noqa: E501


        :return: The user of this IamSessionAllOf.  # noqa: E501
        :rtype: IamUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this IamSessionAllOf.


        :param user: The user of this IamSessionAllOf.  # noqa: E501
        :type: IamUser
        """

        self._user = user

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
        if not isinstance(other, IamSessionAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IamSessionAllOf):
            return True

        return self.to_dict() != other.to_dict()
