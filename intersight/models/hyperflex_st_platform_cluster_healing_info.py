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


class HyperflexStPlatformClusterHealingInfo(object):
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
        'estimated_completion_time_in_seconds': 'int',
        'in_progress': 'bool',
        'messages': 'list[str]',
        'messages_iterator': 'object',
        'messages_size': 'int',
        'percent_complete': 'int'
    }

    attribute_map = {
        'estimated_completion_time_in_seconds':
        'EstimatedCompletionTimeInSeconds',
        'in_progress': 'InProgress',
        'messages': 'Messages',
        'messages_iterator': 'MessagesIterator',
        'messages_size': 'MessagesSize',
        'percent_complete': 'PercentComplete'
    }

    def __init__(self,
                 estimated_completion_time_in_seconds=None,
                 in_progress=None,
                 messages=None,
                 messages_iterator=None,
                 messages_size=None,
                 percent_complete=None,
                 local_vars_configuration=None):  # noqa: E501
        """HyperflexStPlatformClusterHealingInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._estimated_completion_time_in_seconds = None
        self._in_progress = None
        self._messages = None
        self._messages_iterator = None
        self._messages_size = None
        self._percent_complete = None
        self.discriminator = None

        if estimated_completion_time_in_seconds is not None:
            self.estimated_completion_time_in_seconds = estimated_completion_time_in_seconds
        if in_progress is not None:
            self.in_progress = in_progress
        if messages is not None:
            self.messages = messages
        if messages_iterator is not None:
            self.messages_iterator = messages_iterator
        if messages_size is not None:
            self.messages_size = messages_size
        if percent_complete is not None:
            self.percent_complete = percent_complete

    @property
    def estimated_completion_time_in_seconds(self):
        """Gets the estimated_completion_time_in_seconds of this HyperflexStPlatformClusterHealingInfo.  # noqa: E501


        :return: The estimated_completion_time_in_seconds of this HyperflexStPlatformClusterHealingInfo.  # noqa: E501
        :rtype: int
        """
        return self._estimated_completion_time_in_seconds

    @estimated_completion_time_in_seconds.setter
    def estimated_completion_time_in_seconds(
            self, estimated_completion_time_in_seconds):
        """Sets the estimated_completion_time_in_seconds of this HyperflexStPlatformClusterHealingInfo.


        :param estimated_completion_time_in_seconds: The estimated_completion_time_in_seconds of this HyperflexStPlatformClusterHealingInfo.  # noqa: E501
        :type: int
        """

        self._estimated_completion_time_in_seconds = estimated_completion_time_in_seconds

    @property
    def in_progress(self):
        """Gets the in_progress of this HyperflexStPlatformClusterHealingInfo.  # noqa: E501


        :return: The in_progress of this HyperflexStPlatformClusterHealingInfo.  # noqa: E501
        :rtype: bool
        """
        return self._in_progress

    @in_progress.setter
    def in_progress(self, in_progress):
        """Sets the in_progress of this HyperflexStPlatformClusterHealingInfo.


        :param in_progress: The in_progress of this HyperflexStPlatformClusterHealingInfo.  # noqa: E501
        :type: bool
        """

        self._in_progress = in_progress

    @property
    def messages(self):
        """Gets the messages of this HyperflexStPlatformClusterHealingInfo.  # noqa: E501


        :return: The messages of this HyperflexStPlatformClusterHealingInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this HyperflexStPlatformClusterHealingInfo.


        :param messages: The messages of this HyperflexStPlatformClusterHealingInfo.  # noqa: E501
        :type: list[str]
        """

        self._messages = messages

    @property
    def messages_iterator(self):
        """Gets the messages_iterator of this HyperflexStPlatformClusterHealingInfo.  # noqa: E501


        :return: The messages_iterator of this HyperflexStPlatformClusterHealingInfo.  # noqa: E501
        :rtype: object
        """
        return self._messages_iterator

    @messages_iterator.setter
    def messages_iterator(self, messages_iterator):
        """Sets the messages_iterator of this HyperflexStPlatformClusterHealingInfo.


        :param messages_iterator: The messages_iterator of this HyperflexStPlatformClusterHealingInfo.  # noqa: E501
        :type: object
        """

        self._messages_iterator = messages_iterator

    @property
    def messages_size(self):
        """Gets the messages_size of this HyperflexStPlatformClusterHealingInfo.  # noqa: E501


        :return: The messages_size of this HyperflexStPlatformClusterHealingInfo.  # noqa: E501
        :rtype: int
        """
        return self._messages_size

    @messages_size.setter
    def messages_size(self, messages_size):
        """Sets the messages_size of this HyperflexStPlatformClusterHealingInfo.


        :param messages_size: The messages_size of this HyperflexStPlatformClusterHealingInfo.  # noqa: E501
        :type: int
        """

        self._messages_size = messages_size

    @property
    def percent_complete(self):
        """Gets the percent_complete of this HyperflexStPlatformClusterHealingInfo.  # noqa: E501


        :return: The percent_complete of this HyperflexStPlatformClusterHealingInfo.  # noqa: E501
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """Sets the percent_complete of this HyperflexStPlatformClusterHealingInfo.


        :param percent_complete: The percent_complete of this HyperflexStPlatformClusterHealingInfo.  # noqa: E501
        :type: int
        """

        self._percent_complete = percent_complete

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
        if not isinstance(other, HyperflexStPlatformClusterHealingInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HyperflexStPlatformClusterHealingInfo):
            return True

        return self.to_dict() != other.to_dict()
