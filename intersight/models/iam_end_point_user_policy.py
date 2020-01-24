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


class IamEndPointUserPolicy(object):
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
        'password_properties': 'IamEndPointPasswordProperties',
        'end_point_user_roles': 'list[IamEndPointUserRole]',
        'organization': 'OrganizationOrganization',
        'profiles': 'list[PolicyAbstractConfigProfile]'
    }

    attribute_map = {
        'password_properties': 'PasswordProperties',
        'end_point_user_roles': 'EndPointUserRoles',
        'organization': 'Organization',
        'profiles': 'Profiles'
    }

    def __init__(self,
                 password_properties=None,
                 end_point_user_roles=None,
                 organization=None,
                 profiles=None,
                 local_vars_configuration=None):  # noqa: E501
        """IamEndPointUserPolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._password_properties = None
        self._end_point_user_roles = None
        self._organization = None
        self._profiles = None
        self.discriminator = None

        if password_properties is not None:
            self.password_properties = password_properties
        if end_point_user_roles is not None:
            self.end_point_user_roles = end_point_user_roles
        if organization is not None:
            self.organization = organization
        if profiles is not None:
            self.profiles = profiles

    @property
    def password_properties(self):
        """Gets the password_properties of this IamEndPointUserPolicy.  # noqa: E501


        :return: The password_properties of this IamEndPointUserPolicy.  # noqa: E501
        :rtype: IamEndPointPasswordProperties
        """
        return self._password_properties

    @password_properties.setter
    def password_properties(self, password_properties):
        """Sets the password_properties of this IamEndPointUserPolicy.


        :param password_properties: The password_properties of this IamEndPointUserPolicy.  # noqa: E501
        :type: IamEndPointPasswordProperties
        """

        self._password_properties = password_properties

    @property
    def end_point_user_roles(self):
        """Gets the end_point_user_roles of this IamEndPointUserPolicy.  # noqa: E501

        A reference to a iamEndPointUserRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the collection of Endpoint user roles.   # noqa: E501

        :return: The end_point_user_roles of this IamEndPointUserPolicy.  # noqa: E501
        :rtype: list[IamEndPointUserRole]
        """
        return self._end_point_user_roles

    @end_point_user_roles.setter
    def end_point_user_roles(self, end_point_user_roles):
        """Sets the end_point_user_roles of this IamEndPointUserPolicy.

        A reference to a iamEndPointUserRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the collection of Endpoint user roles.   # noqa: E501

        :param end_point_user_roles: The end_point_user_roles of this IamEndPointUserPolicy.  # noqa: E501
        :type: list[IamEndPointUserRole]
        """

        self._end_point_user_roles = end_point_user_roles

    @property
    def organization(self):
        """Gets the organization of this IamEndPointUserPolicy.  # noqa: E501


        :return: The organization of this IamEndPointUserPolicy.  # noqa: E501
        :rtype: OrganizationOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this IamEndPointUserPolicy.


        :param organization: The organization of this IamEndPointUserPolicy.  # noqa: E501
        :type: OrganizationOrganization
        """

        self._organization = organization

    @property
    def profiles(self):
        """Gets the profiles of this IamEndPointUserPolicy.  # noqa: E501

        A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the server profile object.   # noqa: E501

        :return: The profiles of this IamEndPointUserPolicy.  # noqa: E501
        :rtype: list[PolicyAbstractConfigProfile]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """Sets the profiles of this IamEndPointUserPolicy.

        A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the server profile object.   # noqa: E501

        :param profiles: The profiles of this IamEndPointUserPolicy.  # noqa: E501
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
        if not isinstance(other, IamEndPointUserPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IamEndPointUserPolicy):
            return True

        return self.to_dict() != other.to_dict()
