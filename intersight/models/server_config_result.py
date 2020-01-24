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


class ServerConfigResult(object):
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
        'profile': 'ServerProfile',
        'result_entries': 'list[ServerConfigResultEntry]'
    }

    attribute_map = {'profile': 'Profile', 'result_entries': 'ResultEntries'}

    def __init__(self,
                 profile=None,
                 result_entries=None,
                 local_vars_configuration=None):  # noqa: E501
        """ServerConfigResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._profile = None
        self._result_entries = None
        self.discriminator = None

        if profile is not None:
            self.profile = profile
        if result_entries is not None:
            self.result_entries = result_entries

    @property
    def profile(self):
        """Gets the profile of this ServerConfigResult.  # noqa: E501


        :return: The profile of this ServerConfigResult.  # noqa: E501
        :rtype: ServerProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this ServerConfigResult.


        :param profile: The profile of this ServerConfigResult.  # noqa: E501
        :type: ServerProfile
        """

        self._profile = profile

    @property
    def result_entries(self):
        """Gets the result_entries of this ServerConfigResult.  # noqa: E501

        A reference to a serverConfigResultEntry resource. When the $expand query parameter is specified, the referenced resource is returned inline. Detailed result entries for both validation & configration. Each result entry can be error/warning/info messages and the context.   # noqa: E501

        :return: The result_entries of this ServerConfigResult.  # noqa: E501
        :rtype: list[ServerConfigResultEntry]
        """
        return self._result_entries

    @result_entries.setter
    def result_entries(self, result_entries):
        """Sets the result_entries of this ServerConfigResult.

        A reference to a serverConfigResultEntry resource. When the $expand query parameter is specified, the referenced resource is returned inline. Detailed result entries for both validation & configration. Each result entry can be error/warning/info messages and the context.   # noqa: E501

        :param result_entries: The result_entries of this ServerConfigResult.  # noqa: E501
        :type: list[ServerConfigResultEntry]
        """

        self._result_entries = result_entries

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
        if not isinstance(other, ServerConfigResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServerConfigResult):
            return True

        return self.to_dict() != other.to_dict()
