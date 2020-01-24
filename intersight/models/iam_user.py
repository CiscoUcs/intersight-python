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


class IamUser(object):
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
        'client_ip_address': 'str',
        'email': 'str',
        'first_name': 'str',
        'last_login_time': 'datetime',
        'last_name': 'str',
        'name': 'str',
        'user_type': 'str',
        'api_keys': 'list[IamApiKey]',
        'app_registrations': 'list[IamAppRegistration]',
        'idp': 'IamIdp',
        'idpreference': 'IamIdpReference',
        'local_user_password': 'IamLocalUserPassword',
        'oauth_tokens': 'list[IamOAuthToken]',
        'permissions': 'list[IamPermission]',
        'sessions': 'list[IamSession]'
    }

    attribute_map = {
        'client_ip_address': 'ClientIpAddress',
        'email': 'Email',
        'first_name': 'FirstName',
        'last_login_time': 'LastLoginTime',
        'last_name': 'LastName',
        'name': 'Name',
        'user_type': 'UserType',
        'api_keys': 'ApiKeys',
        'app_registrations': 'AppRegistrations',
        'idp': 'Idp',
        'idpreference': 'Idpreference',
        'local_user_password': 'LocalUserPassword',
        'oauth_tokens': 'OauthTokens',
        'permissions': 'Permissions',
        'sessions': 'Sessions'
    }

    def __init__(self,
                 client_ip_address=None,
                 email=None,
                 first_name=None,
                 last_login_time=None,
                 last_name=None,
                 name=None,
                 user_type=None,
                 api_keys=None,
                 app_registrations=None,
                 idp=None,
                 idpreference=None,
                 local_user_password=None,
                 oauth_tokens=None,
                 permissions=None,
                 sessions=None,
                 local_vars_configuration=None):  # noqa: E501
        """IamUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_ip_address = None
        self._email = None
        self._first_name = None
        self._last_login_time = None
        self._last_name = None
        self._name = None
        self._user_type = None
        self._api_keys = None
        self._app_registrations = None
        self._idp = None
        self._idpreference = None
        self._local_user_password = None
        self._oauth_tokens = None
        self._permissions = None
        self._sessions = None
        self.discriminator = None

        if client_ip_address is not None:
            self.client_ip_address = client_ip_address
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_login_time is not None:
            self.last_login_time = last_login_time
        if last_name is not None:
            self.last_name = last_name
        if name is not None:
            self.name = name
        if user_type is not None:
            self.user_type = user_type
        if api_keys is not None:
            self.api_keys = api_keys
        if app_registrations is not None:
            self.app_registrations = app_registrations
        if idp is not None:
            self.idp = idp
        if idpreference is not None:
            self.idpreference = idpreference
        if local_user_password is not None:
            self.local_user_password = local_user_password
        if oauth_tokens is not None:
            self.oauth_tokens = oauth_tokens
        if permissions is not None:
            self.permissions = permissions
        if sessions is not None:
            self.sessions = sessions

    @property
    def client_ip_address(self):
        """Gets the client_ip_address of this IamUser.  # noqa: E501

        IP address from which the user last logged in to Intersight.    # noqa: E501

        :return: The client_ip_address of this IamUser.  # noqa: E501
        :rtype: str
        """
        return self._client_ip_address

    @client_ip_address.setter
    def client_ip_address(self, client_ip_address):
        """Sets the client_ip_address of this IamUser.

        IP address from which the user last logged in to Intersight.    # noqa: E501

        :param client_ip_address: The client_ip_address of this IamUser.  # noqa: E501
        :type: str
        """

        self._client_ip_address = client_ip_address

    @property
    def email(self):
        """Gets the email of this IamUser.  # noqa: E501

        Email of the user. Users are added to Intersight using the email configured in the IdP.    # noqa: E501

        :return: The email of this IamUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this IamUser.

        Email of the user. Users are added to Intersight using the email configured in the IdP.    # noqa: E501

        :param email: The email of this IamUser.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this IamUser.  # noqa: E501

        First name of the user. This field is populated from the IdP attributes received after authentication.    # noqa: E501

        :return: The first_name of this IamUser.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this IamUser.

        First name of the user. This field is populated from the IdP attributes received after authentication.    # noqa: E501

        :param first_name: The first_name of this IamUser.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_login_time(self):
        """Gets the last_login_time of this IamUser.  # noqa: E501

        Last successful login time for user.    # noqa: E501

        :return: The last_login_time of this IamUser.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login_time

    @last_login_time.setter
    def last_login_time(self, last_login_time):
        """Sets the last_login_time of this IamUser.

        Last successful login time for user.    # noqa: E501

        :param last_login_time: The last_login_time of this IamUser.  # noqa: E501
        :type: datetime
        """

        self._last_login_time = last_login_time

    @property
    def last_name(self):
        """Gets the last_name of this IamUser.  # noqa: E501

        Last name of the user. This field is populated from the IdP attributes received after authentication.    # noqa: E501

        :return: The last_name of this IamUser.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this IamUser.

        Last name of the user. This field is populated from the IdP attributes received after authentication.    # noqa: E501

        :param last_name: The last_name of this IamUser.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def name(self):
        """Gets the name of this IamUser.  # noqa: E501

        UserID as configured in the IdP.    # noqa: E501

        :return: The name of this IamUser.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IamUser.

        UserID as configured in the IdP.    # noqa: E501

        :param name: The name of this IamUser.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def user_type(self):
        """Gets the user_type of this IamUser.  # noqa: E501

        Type of the User. If a user is added manually by specifying the email address, or has logged in using groups, based on the IdP attributes received during authentication. If added manually, the user type will be static, otherwise dynamic.     # noqa: E501

        :return: The user_type of this IamUser.  # noqa: E501
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this IamUser.

        Type of the User. If a user is added manually by specifying the email address, or has logged in using groups, based on the IdP attributes received during authentication. If added manually, the user type will be static, otherwise dynamic.     # noqa: E501

        :param user_type: The user_type of this IamUser.  # noqa: E501
        :type: str
        """

        self._user_type = user_type

    @property
    def api_keys(self):
        """Gets the api_keys of this IamUser.  # noqa: E501

        A reference to a iamApiKey resource. When the $expand query parameter is specified, the referenced resource is returned inline. Current user's API keys. API keys are used to programatically perform API calls.   # noqa: E501

        :return: The api_keys of this IamUser.  # noqa: E501
        :rtype: list[IamApiKey]
        """
        return self._api_keys

    @api_keys.setter
    def api_keys(self, api_keys):
        """Sets the api_keys of this IamUser.

        A reference to a iamApiKey resource. When the $expand query parameter is specified, the referenced resource is returned inline. Current user's API keys. API keys are used to programatically perform API calls.   # noqa: E501

        :param api_keys: The api_keys of this IamUser.  # noqa: E501
        :type: list[IamApiKey]
        """

        self._api_keys = api_keys

    @property
    def app_registrations(self):
        """Gets the app_registrations of this IamUser.  # noqa: E501

        A reference to a iamAppRegistration resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of registered OAuth2 applications created by the User.   # noqa: E501

        :return: The app_registrations of this IamUser.  # noqa: E501
        :rtype: list[IamAppRegistration]
        """
        return self._app_registrations

    @app_registrations.setter
    def app_registrations(self, app_registrations):
        """Sets the app_registrations of this IamUser.

        A reference to a iamAppRegistration resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of registered OAuth2 applications created by the User.   # noqa: E501

        :param app_registrations: The app_registrations of this IamUser.  # noqa: E501
        :type: list[IamAppRegistration]
        """

        self._app_registrations = app_registrations

    @property
    def idp(self):
        """Gets the idp of this IamUser.  # noqa: E501


        :return: The idp of this IamUser.  # noqa: E501
        :rtype: IamIdp
        """
        return self._idp

    @idp.setter
    def idp(self, idp):
        """Sets the idp of this IamUser.


        :param idp: The idp of this IamUser.  # noqa: E501
        :type: IamIdp
        """

        self._idp = idp

    @property
    def idpreference(self):
        """Gets the idpreference of this IamUser.  # noqa: E501


        :return: The idpreference of this IamUser.  # noqa: E501
        :rtype: IamIdpReference
        """
        return self._idpreference

    @idpreference.setter
    def idpreference(self, idpreference):
        """Sets the idpreference of this IamUser.


        :param idpreference: The idpreference of this IamUser.  # noqa: E501
        :type: IamIdpReference
        """

        self._idpreference = idpreference

    @property
    def local_user_password(self):
        """Gets the local_user_password of this IamUser.  # noqa: E501


        :return: The local_user_password of this IamUser.  # noqa: E501
        :rtype: IamLocalUserPassword
        """
        return self._local_user_password

    @local_user_password.setter
    def local_user_password(self, local_user_password):
        """Sets the local_user_password of this IamUser.


        :param local_user_password: The local_user_password of this IamUser.  # noqa: E501
        :type: IamLocalUserPassword
        """

        self._local_user_password = local_user_password

    @property
    def oauth_tokens(self):
        """Gets the oauth_tokens of this IamUser.  # noqa: E501

        A reference to a iamOAuthToken resource. When the $expand query parameter is specified, the referenced resource is returned inline. Collection of the available OAuthTokens. Each OAuthToken lives 30 days unless it is deleted manually by User. OAuthToken is created when Login performed via OAuth Client (AppRegistration). OAuthToken itself is not sensitive data since it doesn't contain salt, salt is stored in Vault.   # noqa: E501

        :return: The oauth_tokens of this IamUser.  # noqa: E501
        :rtype: list[IamOAuthToken]
        """
        return self._oauth_tokens

    @oauth_tokens.setter
    def oauth_tokens(self, oauth_tokens):
        """Sets the oauth_tokens of this IamUser.

        A reference to a iamOAuthToken resource. When the $expand query parameter is specified, the referenced resource is returned inline. Collection of the available OAuthTokens. Each OAuthToken lives 30 days unless it is deleted manually by User. OAuthToken is created when Login performed via OAuth Client (AppRegistration). OAuthToken itself is not sensitive data since it doesn't contain salt, salt is stored in Vault.   # noqa: E501

        :param oauth_tokens: The oauth_tokens of this IamUser.  # noqa: E501
        :type: list[IamOAuthToken]
        """

        self._oauth_tokens = oauth_tokens

    @property
    def permissions(self):
        """Gets the permissions of this IamUser.  # noqa: E501

        A reference to a iamPermission resource. When the $expand query parameter is specified, the referenced resource is returned inline. Permissions assigned to the user. Permission provides a way to assign roles to a user or user group to perform operations on object hierarchy.   # noqa: E501

        :return: The permissions of this IamUser.  # noqa: E501
        :rtype: list[IamPermission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this IamUser.

        A reference to a iamPermission resource. When the $expand query parameter is specified, the referenced resource is returned inline. Permissions assigned to the user. Permission provides a way to assign roles to a user or user group to perform operations on object hierarchy.   # noqa: E501

        :param permissions: The permissions of this IamUser.  # noqa: E501
        :type: list[IamPermission]
        """

        self._permissions = permissions

    @property
    def sessions(self):
        """Gets the sessions of this IamUser.  # noqa: E501

        A reference to a iamSession resource. When the $expand query parameter is specified, the referenced resource is returned inline. Current user's web sessions. After a user logs into Intersight, a session object is created. This session object is deleted upon logout, idle timeout, expiry timeout, or manual deletion.   # noqa: E501

        :return: The sessions of this IamUser.  # noqa: E501
        :rtype: list[IamSession]
        """
        return self._sessions

    @sessions.setter
    def sessions(self, sessions):
        """Sets the sessions of this IamUser.

        A reference to a iamSession resource. When the $expand query parameter is specified, the referenced resource is returned inline. Current user's web sessions. After a user logs into Intersight, a session object is created. This session object is deleted upon logout, idle timeout, expiry timeout, or manual deletion.   # noqa: E501

        :param sessions: The sessions of this IamUser.  # noqa: E501
        :type: list[IamSession]
        """

        self._sessions = sessions

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
        if not isinstance(other, IamUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IamUser):
            return True

        return self.to_dict() != other.to_dict()
