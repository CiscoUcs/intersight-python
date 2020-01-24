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


class ExternalsiteAuthorization(object):
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
        'is_password_set': 'bool',
        'is_user_id_set': 'bool',
        'password': 'str',
        'repository_type': 'str',
        'user_id': 'str',
        'account': 'IamAccount'
    }

    attribute_map = {
        'is_password_set': 'IsPasswordSet',
        'is_user_id_set': 'IsUserIdSet',
        'password': 'Password',
        'repository_type': 'RepositoryType',
        'user_id': 'UserId',
        'account': 'Account'
    }

    def __init__(self,
                 is_password_set=None,
                 is_user_id_set=None,
                 password=None,
                 repository_type='cisco',
                 user_id=None,
                 account=None,
                 local_vars_configuration=None):  # noqa: E501
        """ExternalsiteAuthorization - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_password_set = None
        self._is_user_id_set = None
        self._password = None
        self._repository_type = None
        self._user_id = None
        self._account = None
        self.discriminator = None

        if is_password_set is not None:
            self.is_password_set = is_password_set
        if is_user_id_set is not None:
            self.is_user_id_set = is_user_id_set
        if password is not None:
            self.password = password
        if repository_type is not None:
            self.repository_type = repository_type
        if user_id is not None:
            self.user_id = user_id
        if account is not None:
            self.account = account

    @property
    def is_password_set(self):
        """Gets the is_password_set of this ExternalsiteAuthorization.  # noqa: E501


        :return: The is_password_set of this ExternalsiteAuthorization.  # noqa: E501
        :rtype: bool
        """
        return self._is_password_set

    @is_password_set.setter
    def is_password_set(self, is_password_set):
        """Sets the is_password_set of this ExternalsiteAuthorization.


        :param is_password_set: The is_password_set of this ExternalsiteAuthorization.  # noqa: E501
        :type: bool
        """

        self._is_password_set = is_password_set

    @property
    def is_user_id_set(self):
        """Gets the is_user_id_set of this ExternalsiteAuthorization.  # noqa: E501


        :return: The is_user_id_set of this ExternalsiteAuthorization.  # noqa: E501
        :rtype: bool
        """
        return self._is_user_id_set

    @is_user_id_set.setter
    def is_user_id_set(self, is_user_id_set):
        """Sets the is_user_id_set of this ExternalsiteAuthorization.


        :param is_user_id_set: The is_user_id_set of this ExternalsiteAuthorization.  # noqa: E501
        :type: bool
        """

        self._is_user_id_set = is_user_id_set

    @property
    def password(self):
        """Gets the password of this ExternalsiteAuthorization.  # noqa: E501

        The password of the given username to download the image from external repository like cisco.com.    # noqa: E501

        :return: The password of this ExternalsiteAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ExternalsiteAuthorization.

        The password of the given username to download the image from external repository like cisco.com.    # noqa: E501

        :param password: The password of this ExternalsiteAuthorization.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def repository_type(self):
        """Gets the repository_type of this ExternalsiteAuthorization.  # noqa: E501

        The repository type to which this authorization will be requested. Cisco is the only available repository today.    # noqa: E501

        :return: The repository_type of this ExternalsiteAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._repository_type

    @repository_type.setter
    def repository_type(self, repository_type):
        """Sets the repository_type of this ExternalsiteAuthorization.

        The repository type to which this authorization will be requested. Cisco is the only available repository today.    # noqa: E501

        :param repository_type: The repository_type of this ExternalsiteAuthorization.  # noqa: E501
        :type: str
        """
        allowed_values = ["cisco"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and repository_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `repository_type` ({0}), must be one of {1}"  # noqa: E501
                .format(repository_type, allowed_values))

        self._repository_type = repository_type

    @property
    def user_id(self):
        """Gets the user_id of this ExternalsiteAuthorization.  # noqa: E501

        The username that has permission to download the image from external repository like cisco.com.     # noqa: E501

        :return: The user_id of this ExternalsiteAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ExternalsiteAuthorization.

        The username that has permission to download the image from external repository like cisco.com.     # noqa: E501

        :param user_id: The user_id of this ExternalsiteAuthorization.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def account(self):
        """Gets the account of this ExternalsiteAuthorization.  # noqa: E501


        :return: The account of this ExternalsiteAuthorization.  # noqa: E501
        :rtype: IamAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this ExternalsiteAuthorization.


        :param account: The account of this ExternalsiteAuthorization.  # noqa: E501
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
        if not isinstance(other, ExternalsiteAuthorization):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExternalsiteAuthorization):
            return True

        return self.to_dict() != other.to_dict()
