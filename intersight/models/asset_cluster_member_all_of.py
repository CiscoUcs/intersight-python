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


class AssetClusterMemberAllOf(object):
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
        'leadership': 'str',
        'locked_leader': 'bool',
        'member_identity': 'str',
        'parent_cluster_member_identity': 'str',
        'sudi': 'AssetSudiInfo',
        'device': 'AssetDeviceRegistration'
    }

    attribute_map = {
        'leadership': 'Leadership',
        'locked_leader': 'LockedLeader',
        'member_identity': 'MemberIdentity',
        'parent_cluster_member_identity': 'ParentClusterMemberIdentity',
        'sudi': 'Sudi',
        'device': 'Device'
    }

    def __init__(self,
                 leadership='Unknown',
                 locked_leader=None,
                 member_identity=None,
                 parent_cluster_member_identity=None,
                 sudi=None,
                 device=None,
                 local_vars_configuration=None):  # noqa: E501
        """AssetClusterMemberAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._leadership = None
        self._locked_leader = None
        self._member_identity = None
        self._parent_cluster_member_identity = None
        self._sudi = None
        self._device = None
        self.discriminator = None

        if leadership is not None:
            self.leadership = leadership
        if locked_leader is not None:
            self.locked_leader = locked_leader
        if member_identity is not None:
            self.member_identity = member_identity
        if parent_cluster_member_identity is not None:
            self.parent_cluster_member_identity = parent_cluster_member_identity
        if sudi is not None:
            self.sudi = sudi
        if device is not None:
            self.device = device

    @property
    def leadership(self):
        """Gets the leadership of this AssetClusterMemberAllOf.  # noqa: E501

        The current leadershipstate of this member. Updated by the device connector on failover or leadership change. If a member is elected as Primary within the cluster this connection will be the same as the DeviceRegistration connection. E.g a message addressed to the DeviceRegistration will be forwarded to the ClusterMember connection.    # noqa: E501

        :return: The leadership of this AssetClusterMemberAllOf.  # noqa: E501
        :rtype: str
        """
        return self._leadership

    @leadership.setter
    def leadership(self, leadership):
        """Sets the leadership of this AssetClusterMemberAllOf.

        The current leadershipstate of this member. Updated by the device connector on failover or leadership change. If a member is elected as Primary within the cluster this connection will be the same as the DeviceRegistration connection. E.g a message addressed to the DeviceRegistration will be forwarded to the ClusterMember connection.    # noqa: E501

        :param leadership: The leadership of this AssetClusterMemberAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unknown", "Primary", "Secondary"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and leadership not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `leadership` ({0}), must be one of {1}"  # noqa: E501
                .format(leadership, allowed_values))

        self._leadership = leadership

    @property
    def locked_leader(self):
        """Gets the locked_leader of this AssetClusterMemberAllOf.  # noqa: E501

        Devices lock their leadership on failure to heartbeat with peers. Value acts as a third party tie breaker in election between nodes. Intersight enforces that only one cluster member exists with this value set to true.    # noqa: E501

        :return: The locked_leader of this AssetClusterMemberAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._locked_leader

    @locked_leader.setter
    def locked_leader(self, locked_leader):
        """Sets the locked_leader of this AssetClusterMemberAllOf.

        Devices lock their leadership on failure to heartbeat with peers. Value acts as a third party tie breaker in election between nodes. Intersight enforces that only one cluster member exists with this value set to true.    # noqa: E501

        :param locked_leader: The locked_leader of this AssetClusterMemberAllOf.  # noqa: E501
        :type: bool
        """

        self._locked_leader = locked_leader

    @property
    def member_identity(self):
        """Gets the member_identity of this AssetClusterMemberAllOf.  # noqa: E501

        The unique identity of the member within the cluster. The identity is retrieved from the platform and reported by the device connector at connection time.    # noqa: E501

        :return: The member_identity of this AssetClusterMemberAllOf.  # noqa: E501
        :rtype: str
        """
        return self._member_identity

    @member_identity.setter
    def member_identity(self, member_identity):
        """Sets the member_identity of this AssetClusterMemberAllOf.

        The unique identity of the member within the cluster. The identity is retrieved from the platform and reported by the device connector at connection time.    # noqa: E501

        :param member_identity: The member_identity of this AssetClusterMemberAllOf.  # noqa: E501
        :type: str
        """

        self._member_identity = member_identity

    @property
    def parent_cluster_member_identity(self):
        """Gets the parent_cluster_member_identity of this AssetClusterMemberAllOf.  # noqa: E501

        The member idenity of the cluster member through which this device is connected if applicable.    # noqa: E501

        :return: The parent_cluster_member_identity of this AssetClusterMemberAllOf.  # noqa: E501
        :rtype: str
        """
        return self._parent_cluster_member_identity

    @parent_cluster_member_identity.setter
    def parent_cluster_member_identity(self, parent_cluster_member_identity):
        """Sets the parent_cluster_member_identity of this AssetClusterMemberAllOf.

        The member idenity of the cluster member through which this device is connected if applicable.    # noqa: E501

        :param parent_cluster_member_identity: The parent_cluster_member_identity of this AssetClusterMemberAllOf.  # noqa: E501
        :type: str
        """

        self._parent_cluster_member_identity = parent_cluster_member_identity

    @property
    def sudi(self):
        """Gets the sudi of this AssetClusterMemberAllOf.  # noqa: E501


        :return: The sudi of this AssetClusterMemberAllOf.  # noqa: E501
        :rtype: AssetSudiInfo
        """
        return self._sudi

    @sudi.setter
    def sudi(self, sudi):
        """Sets the sudi of this AssetClusterMemberAllOf.


        :param sudi: The sudi of this AssetClusterMemberAllOf.  # noqa: E501
        :type: AssetSudiInfo
        """

        self._sudi = sudi

    @property
    def device(self):
        """Gets the device of this AssetClusterMemberAllOf.  # noqa: E501


        :return: The device of this AssetClusterMemberAllOf.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this AssetClusterMemberAllOf.


        :param device: The device of this AssetClusterMemberAllOf.  # noqa: E501
        :type: AssetDeviceRegistration
        """

        self._device = device

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
        if not isinstance(other, AssetClusterMemberAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetClusterMemberAllOf):
            return True

        return self.to_dict() != other.to_dict()
