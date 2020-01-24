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


class HyperflexStPlatformClusterResiliencyInfoAllOf(object):
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
        'hdd_failures_tolerable': 'int',
        'messages': 'list[str]',
        'messages_iterator': 'object',
        'messages_size': 'int',
        'node_failures_tolerable': 'int',
        'ssd_failures_tolerable': 'int',
        'state': 'str'
    }

    attribute_map = {
        'hdd_failures_tolerable': 'HddFailuresTolerable',
        'messages': 'Messages',
        'messages_iterator': 'MessagesIterator',
        'messages_size': 'MessagesSize',
        'node_failures_tolerable': 'NodeFailuresTolerable',
        'ssd_failures_tolerable': 'SsdFailuresTolerable',
        'state': 'State'
    }

    def __init__(self,
                 hdd_failures_tolerable=None,
                 messages=None,
                 messages_iterator=None,
                 messages_size=None,
                 node_failures_tolerable=None,
                 ssd_failures_tolerable=None,
                 state=None,
                 local_vars_configuration=None):  # noqa: E501
        """HyperflexStPlatformClusterResiliencyInfoAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hdd_failures_tolerable = None
        self._messages = None
        self._messages_iterator = None
        self._messages_size = None
        self._node_failures_tolerable = None
        self._ssd_failures_tolerable = None
        self._state = None
        self.discriminator = None

        if hdd_failures_tolerable is not None:
            self.hdd_failures_tolerable = hdd_failures_tolerable
        if messages is not None:
            self.messages = messages
        if messages_iterator is not None:
            self.messages_iterator = messages_iterator
        if messages_size is not None:
            self.messages_size = messages_size
        if node_failures_tolerable is not None:
            self.node_failures_tolerable = node_failures_tolerable
        if ssd_failures_tolerable is not None:
            self.ssd_failures_tolerable = ssd_failures_tolerable
        if state is not None:
            self.state = state

    @property
    def hdd_failures_tolerable(self):
        """Gets the hdd_failures_tolerable of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501


        :return: The hdd_failures_tolerable of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501
        :rtype: int
        """
        return self._hdd_failures_tolerable

    @hdd_failures_tolerable.setter
    def hdd_failures_tolerable(self, hdd_failures_tolerable):
        """Sets the hdd_failures_tolerable of this HyperflexStPlatformClusterResiliencyInfoAllOf.


        :param hdd_failures_tolerable: The hdd_failures_tolerable of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501
        :type: int
        """

        self._hdd_failures_tolerable = hdd_failures_tolerable

    @property
    def messages(self):
        """Gets the messages of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501


        :return: The messages of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this HyperflexStPlatformClusterResiliencyInfoAllOf.


        :param messages: The messages of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501
        :type: list[str]
        """

        self._messages = messages

    @property
    def messages_iterator(self):
        """Gets the messages_iterator of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501


        :return: The messages_iterator of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501
        :rtype: object
        """
        return self._messages_iterator

    @messages_iterator.setter
    def messages_iterator(self, messages_iterator):
        """Sets the messages_iterator of this HyperflexStPlatformClusterResiliencyInfoAllOf.


        :param messages_iterator: The messages_iterator of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501
        :type: object
        """

        self._messages_iterator = messages_iterator

    @property
    def messages_size(self):
        """Gets the messages_size of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501


        :return: The messages_size of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501
        :rtype: int
        """
        return self._messages_size

    @messages_size.setter
    def messages_size(self, messages_size):
        """Sets the messages_size of this HyperflexStPlatformClusterResiliencyInfoAllOf.


        :param messages_size: The messages_size of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501
        :type: int
        """

        self._messages_size = messages_size

    @property
    def node_failures_tolerable(self):
        """Gets the node_failures_tolerable of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501


        :return: The node_failures_tolerable of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501
        :rtype: int
        """
        return self._node_failures_tolerable

    @node_failures_tolerable.setter
    def node_failures_tolerable(self, node_failures_tolerable):
        """Sets the node_failures_tolerable of this HyperflexStPlatformClusterResiliencyInfoAllOf.


        :param node_failures_tolerable: The node_failures_tolerable of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501
        :type: int
        """

        self._node_failures_tolerable = node_failures_tolerable

    @property
    def ssd_failures_tolerable(self):
        """Gets the ssd_failures_tolerable of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501


        :return: The ssd_failures_tolerable of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501
        :rtype: int
        """
        return self._ssd_failures_tolerable

    @ssd_failures_tolerable.setter
    def ssd_failures_tolerable(self, ssd_failures_tolerable):
        """Sets the ssd_failures_tolerable of this HyperflexStPlatformClusterResiliencyInfoAllOf.


        :param ssd_failures_tolerable: The ssd_failures_tolerable of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501
        :type: int
        """

        self._ssd_failures_tolerable = ssd_failures_tolerable

    @property
    def state(self):
        """Gets the state of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501


        :return: The state of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this HyperflexStPlatformClusterResiliencyInfoAllOf.


        :param state: The state of this HyperflexStPlatformClusterResiliencyInfoAllOf.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if not isinstance(other,
                          HyperflexStPlatformClusterResiliencyInfoAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other,
                          HyperflexStPlatformClusterResiliencyInfoAllOf):
            return True

        return self.to_dict() != other.to_dict()
