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


class ApplianceRestore(object):
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
        'elapsed_time': 'int',
        'end_time': 'datetime',
        'is_password_set': 'bool',
        'messages': 'list[str]',
        'password': 'str',
        'start_time': 'datetime',
        'status': 'str',
        'account': 'IamAccount'
    }

    attribute_map = {
        'elapsed_time': 'ElapsedTime',
        'end_time': 'EndTime',
        'is_password_set': 'IsPasswordSet',
        'messages': 'Messages',
        'password': 'Password',
        'start_time': 'StartTime',
        'status': 'Status',
        'account': 'Account'
    }

    def __init__(self,
                 elapsed_time=None,
                 end_time=None,
                 is_password_set=None,
                 messages=None,
                 password=None,
                 start_time=None,
                 status='Started',
                 account=None,
                 local_vars_configuration=None):  # noqa: E501
        """ApplianceRestore - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._elapsed_time = None
        self._end_time = None
        self._is_password_set = None
        self._messages = None
        self._password = None
        self._start_time = None
        self._status = None
        self._account = None
        self.discriminator = None

        if elapsed_time is not None:
            self.elapsed_time = elapsed_time
        if end_time is not None:
            self.end_time = end_time
        if is_password_set is not None:
            self.is_password_set = is_password_set
        if messages is not None:
            self.messages = messages
        if password is not None:
            self.password = password
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if account is not None:
            self.account = account

    @property
    def elapsed_time(self):
        """Gets the elapsed_time of this ApplianceRestore.  # noqa: E501

        Elapsed time in seconds since the restore process has started.    # noqa: E501

        :return: The elapsed_time of this ApplianceRestore.  # noqa: E501
        :rtype: int
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """Sets the elapsed_time of this ApplianceRestore.

        Elapsed time in seconds since the restore process has started.    # noqa: E501

        :param elapsed_time: The elapsed_time of this ApplianceRestore.  # noqa: E501
        :type: int
        """

        self._elapsed_time = elapsed_time

    @property
    def end_time(self):
        """Gets the end_time of this ApplianceRestore.  # noqa: E501

        End date and time of the restore process.    # noqa: E501

        :return: The end_time of this ApplianceRestore.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ApplianceRestore.

        End date and time of the restore process.    # noqa: E501

        :param end_time: The end_time of this ApplianceRestore.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def is_password_set(self):
        """Gets the is_password_set of this ApplianceRestore.  # noqa: E501


        :return: The is_password_set of this ApplianceRestore.  # noqa: E501
        :rtype: bool
        """
        return self._is_password_set

    @is_password_set.setter
    def is_password_set(self, is_password_set):
        """Sets the is_password_set of this ApplianceRestore.


        :param is_password_set: The is_password_set of this ApplianceRestore.  # noqa: E501
        :type: bool
        """

        self._is_password_set = is_password_set

    @property
    def messages(self):
        """Gets the messages of this ApplianceRestore.  # noqa: E501


        :return: The messages of this ApplianceRestore.  # noqa: E501
        :rtype: list[str]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this ApplianceRestore.


        :param messages: The messages of this ApplianceRestore.  # noqa: E501
        :type: list[str]
        """

        self._messages = messages

    @property
    def password(self):
        """Gets the password of this ApplianceRestore.  # noqa: E501

        Password for authenticating with the file server.    # noqa: E501

        :return: The password of this ApplianceRestore.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ApplianceRestore.

        Password for authenticating with the file server.    # noqa: E501

        :param password: The password of this ApplianceRestore.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def start_time(self):
        """Gets the start_time of this ApplianceRestore.  # noqa: E501

        Start date and time of the restore process.    # noqa: E501

        :return: The start_time of this ApplianceRestore.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ApplianceRestore.

        Start date and time of the restore process.    # noqa: E501

        :param start_time: The start_time of this ApplianceRestore.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this ApplianceRestore.  # noqa: E501

        Status of the restore managed object.     # noqa: E501

        :return: The status of this ApplianceRestore.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApplianceRestore.

        Status of the restore managed object.     # noqa: E501

        :param status: The status of this ApplianceRestore.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "Started", "Created", "Failed", "Completed", "Copied"
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values))

        self._status = status

    @property
    def account(self):
        """Gets the account of this ApplianceRestore.  # noqa: E501


        :return: The account of this ApplianceRestore.  # noqa: E501
        :rtype: IamAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this ApplianceRestore.


        :param account: The account of this ApplianceRestore.  # noqa: E501
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
        if not isinstance(other, ApplianceRestore):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplianceRestore):
            return True

        return self.to_dict() != other.to_dict()
