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


class IamSessionLimitsAllOf(object):
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
        'idle_time_out': 'int',
        'maximum_limit': 'int',
        'per_user_limit': 'int',
        'session_time_out': 'int',
        'account': 'IamAccount'
    }

    attribute_map = {
        'idle_time_out': 'IdleTimeOut',
        'maximum_limit': 'MaximumLimit',
        'per_user_limit': 'PerUserLimit',
        'session_time_out': 'SessionTimeOut',
        'account': 'Account'
    }

    def __init__(self,
                 idle_time_out=None,
                 maximum_limit=None,
                 per_user_limit=None,
                 session_time_out=None,
                 account=None,
                 local_vars_configuration=None):  # noqa: E501
        """IamSessionLimitsAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._idle_time_out = None
        self._maximum_limit = None
        self._per_user_limit = None
        self._session_time_out = None
        self._account = None
        self.discriminator = None

        if idle_time_out is not None:
            self.idle_time_out = idle_time_out
        if maximum_limit is not None:
            self.maximum_limit = maximum_limit
        if per_user_limit is not None:
            self.per_user_limit = per_user_limit
        if session_time_out is not None:
            self.session_time_out = session_time_out
        if account is not None:
            self.account = account

    @property
    def idle_time_out(self):
        """Gets the idle_time_out of this IamSessionLimitsAllOf.  # noqa: E501

        The idle timeout interval for the web session in seconds. The default value is 1800 seconds. When a session is not refreshed for this duration, backend will mark the session as idle and remove the session.    # noqa: E501

        :return: The idle_time_out of this IamSessionLimitsAllOf.  # noqa: E501
        :rtype: int
        """
        return self._idle_time_out

    @idle_time_out.setter
    def idle_time_out(self, idle_time_out):
        """Sets the idle_time_out of this IamSessionLimitsAllOf.

        The idle timeout interval for the web session in seconds. The default value is 1800 seconds. When a session is not refreshed for this duration, backend will mark the session as idle and remove the session.    # noqa: E501

        :param idle_time_out: The idle_time_out of this IamSessionLimitsAllOf.  # noqa: E501
        :type: int
        """

        self._idle_time_out = idle_time_out

    @property
    def maximum_limit(self):
        """Gets the maximum_limit of this IamSessionLimitsAllOf.  # noqa: E501

        The maximum number of sessions allowed in an account. The default value is 128.    # noqa: E501

        :return: The maximum_limit of this IamSessionLimitsAllOf.  # noqa: E501
        :rtype: int
        """
        return self._maximum_limit

    @maximum_limit.setter
    def maximum_limit(self, maximum_limit):
        """Sets the maximum_limit of this IamSessionLimitsAllOf.

        The maximum number of sessions allowed in an account. The default value is 128.    # noqa: E501

        :param maximum_limit: The maximum_limit of this IamSessionLimitsAllOf.  # noqa: E501
        :type: int
        """

        self._maximum_limit = maximum_limit

    @property
    def per_user_limit(self):
        """Gets the per_user_limit of this IamSessionLimitsAllOf.  # noqa: E501

        The maximum number of sessions allowed per user. Default value is 32.     # noqa: E501

        :return: The per_user_limit of this IamSessionLimitsAllOf.  # noqa: E501
        :rtype: int
        """
        return self._per_user_limit

    @per_user_limit.setter
    def per_user_limit(self, per_user_limit):
        """Sets the per_user_limit of this IamSessionLimitsAllOf.

        The maximum number of sessions allowed per user. Default value is 32.     # noqa: E501

        :param per_user_limit: The per_user_limit of this IamSessionLimitsAllOf.  # noqa: E501
        :type: int
        """

        self._per_user_limit = per_user_limit

    @property
    def session_time_out(self):
        """Gets the session_time_out of this IamSessionLimitsAllOf.  # noqa: E501

        The session expiry duration in seconds. The default value is 57600 seconds or 16 hours.     # noqa: E501

        :return: The session_time_out of this IamSessionLimitsAllOf.  # noqa: E501
        :rtype: int
        """
        return self._session_time_out

    @session_time_out.setter
    def session_time_out(self, session_time_out):
        """Sets the session_time_out of this IamSessionLimitsAllOf.

        The session expiry duration in seconds. The default value is 57600 seconds or 16 hours.     # noqa: E501

        :param session_time_out: The session_time_out of this IamSessionLimitsAllOf.  # noqa: E501
        :type: int
        """

        self._session_time_out = session_time_out

    @property
    def account(self):
        """Gets the account of this IamSessionLimitsAllOf.  # noqa: E501


        :return: The account of this IamSessionLimitsAllOf.  # noqa: E501
        :rtype: IamAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this IamSessionLimitsAllOf.


        :param account: The account of this IamSessionLimitsAllOf.  # noqa: E501
        :type: IamAccount
        """

        self._account = account

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
        if not isinstance(other, IamSessionLimitsAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IamSessionLimitsAllOf):
            return True

        return self.to_dict() != other.to_dict()
