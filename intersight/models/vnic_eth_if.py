# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1295
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VnicEthIf(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_moid': 'str',
        'create_time': 'datetime',
        'domain_group_moid': 'str',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'shared_scope': 'str',
        'tags': 'list[MoTag]',
        'version_context': 'MoVersionContext',
        'ancestors': 'list[MoBaseMoRef]',
        'parent': 'MoBaseMoRef',
        'permission_resources': 'list[MoBaseMoRef]',
        'cdn': 'VnicCdn',
        'name': 'str',
        'order': 'int',
        'placement': 'VnicPlacementSettings',
        'usnic_settings': 'VnicUsnicSettings',
        'vmq_settings': 'VnicVmqSettings',
        'eth_adapter_policy': 'VnicEthAdapterPolicyRef',
        'eth_network_policy': 'VnicEthNetworkPolicyRef',
        'eth_qos_policy': 'VnicEthQosPolicyRef',
        'lan_connectivity_policy': 'VnicLanConnectivityPolicyRef',
        'organization': 'OrganizationOrganizationRef'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'create_time': 'CreateTime',
        'domain_group_moid': 'DomainGroupMoid',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'shared_scope': 'SharedScope',
        'tags': 'Tags',
        'version_context': 'VersionContext',
        'ancestors': 'Ancestors',
        'parent': 'Parent',
        'permission_resources': 'PermissionResources',
        'cdn': 'Cdn',
        'name': 'Name',
        'order': 'Order',
        'placement': 'Placement',
        'usnic_settings': 'UsnicSettings',
        'vmq_settings': 'VmqSettings',
        'eth_adapter_policy': 'EthAdapterPolicy',
        'eth_network_policy': 'EthNetworkPolicy',
        'eth_qos_policy': 'EthQosPolicy',
        'lan_connectivity_policy': 'LanConnectivityPolicy',
        'organization': 'Organization'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, cdn=None, name=None, order=None, placement=None, usnic_settings=None, vmq_settings=None, eth_adapter_policy=None, eth_network_policy=None, eth_qos_policy=None, lan_connectivity_policy=None, organization=None):
        """
        VnicEthIf - a model defined in Swagger
        """

        self._account_moid = None
        self._create_time = None
        self._domain_group_moid = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._shared_scope = None
        self._tags = None
        self._version_context = None
        self._ancestors = None
        self._parent = None
        self._permission_resources = None
        self._cdn = None
        self._name = None
        self._order = None
        self._placement = None
        self._usnic_settings = None
        self._vmq_settings = None
        self._eth_adapter_policy = None
        self._eth_network_policy = None
        self._eth_qos_policy = None
        self._lan_connectivity_policy = None
        self._organization = None

        if account_moid is not None:
          self.account_moid = account_moid
        if create_time is not None:
          self.create_time = create_time
        if domain_group_moid is not None:
          self.domain_group_moid = domain_group_moid
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if shared_scope is not None:
          self.shared_scope = shared_scope
        if tags is not None:
          self.tags = tags
        if version_context is not None:
          self.version_context = version_context
        if ancestors is not None:
          self.ancestors = ancestors
        if parent is not None:
          self.parent = parent
        if permission_resources is not None:
          self.permission_resources = permission_resources
        if cdn is not None:
          self.cdn = cdn
        if name is not None:
          self.name = name
        if order is not None:
          self.order = order
        if placement is not None:
          self.placement = placement
        if usnic_settings is not None:
          self.usnic_settings = usnic_settings
        if vmq_settings is not None:
          self.vmq_settings = vmq_settings
        if eth_adapter_policy is not None:
          self.eth_adapter_policy = eth_adapter_policy
        if eth_network_policy is not None:
          self.eth_network_policy = eth_network_policy
        if eth_qos_policy is not None:
          self.eth_qos_policy = eth_qos_policy
        if lan_connectivity_policy is not None:
          self.lan_connectivity_policy = lan_connectivity_policy
        if organization is not None:
          self.organization = organization

    @property
    def account_moid(self):
        """
        Gets the account_moid of this VnicEthIf.
        The Account ID for this managed object.  

        :return: The account_moid of this VnicEthIf.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this VnicEthIf.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this VnicEthIf.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this VnicEthIf.
        The time when this managed object was created.  

        :return: The create_time of this VnicEthIf.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this VnicEthIf.
        The time when this managed object was created.  

        :param create_time: The create_time of this VnicEthIf.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this VnicEthIf.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this VnicEthIf.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this VnicEthIf.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this VnicEthIf.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this VnicEthIf.
        The time when this managed object was last modified.  

        :return: The mod_time of this VnicEthIf.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this VnicEthIf.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this VnicEthIf.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this VnicEthIf.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this VnicEthIf.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this VnicEthIf.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this VnicEthIf.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this VnicEthIf.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this VnicEthIf.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this VnicEthIf.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this VnicEthIf.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this VnicEthIf.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this VnicEthIf.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this VnicEthIf.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this VnicEthIf.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this VnicEthIf.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this VnicEthIf.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this VnicEthIf.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this VnicEthIf.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this VnicEthIf.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this VnicEthIf.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this VnicEthIf.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this VnicEthIf.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this VnicEthIf.
        The versioning info for this managed object.   

        :return: The version_context of this VnicEthIf.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this VnicEthIf.
        The versioning info for this managed object.   

        :param version_context: The version_context of this VnicEthIf.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this VnicEthIf.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this VnicEthIf.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this VnicEthIf.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this VnicEthIf.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this VnicEthIf.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this VnicEthIf.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this VnicEthIf.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this VnicEthIf.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this VnicEthIf.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this VnicEthIf.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this VnicEthIf.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this VnicEthIf.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def cdn(self):
        """
        Gets the cdn of this VnicEthIf.
        Consistent Device Naming configuration for the virtual NIC.  

        :return: The cdn of this VnicEthIf.
        :rtype: VnicCdn
        """
        return self._cdn

    @cdn.setter
    def cdn(self, cdn):
        """
        Sets the cdn of this VnicEthIf.
        Consistent Device Naming configuration for the virtual NIC.  

        :param cdn: The cdn of this VnicEthIf.
        :type: VnicCdn
        """

        self._cdn = cdn

    @property
    def name(self):
        """
        Gets the name of this VnicEthIf.
        Name of the virtual ethernet interface.  

        :return: The name of this VnicEthIf.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VnicEthIf.
        Name of the virtual ethernet interface.  

        :param name: The name of this VnicEthIf.
        :type: str
        """

        self._name = name

    @property
    def order(self):
        """
        Gets the order of this VnicEthIf.
        The order in which the virtual interface is brought up. The order assigned to an interface should be unique for all the Ethernet and Fibre-Channel interfaces on each PCI link on a VIC adapter. The maximum value of PCI order is limited by the number of virtual interfaces (Ethernet and Fibre-Channel) on each PCI link on a VIC adapter. All VIC adapters have a single PCI link except VIC 1385 which has two.  

        :return: The order of this VnicEthIf.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this VnicEthIf.
        The order in which the virtual interface is brought up. The order assigned to an interface should be unique for all the Ethernet and Fibre-Channel interfaces on each PCI link on a VIC adapter. The maximum value of PCI order is limited by the number of virtual interfaces (Ethernet and Fibre-Channel) on each PCI link on a VIC adapter. All VIC adapters have a single PCI link except VIC 1385 which has two.  

        :param order: The order of this VnicEthIf.
        :type: int
        """

        self._order = order

    @property
    def placement(self):
        """
        Gets the placement of this VnicEthIf.
        Placement Settings for the virtual interface.  

        :return: The placement of this VnicEthIf.
        :rtype: VnicPlacementSettings
        """
        return self._placement

    @placement.setter
    def placement(self, placement):
        """
        Sets the placement of this VnicEthIf.
        Placement Settings for the virtual interface.  

        :param placement: The placement of this VnicEthIf.
        :type: VnicPlacementSettings
        """

        self._placement = placement

    @property
    def usnic_settings(self):
        """
        Gets the usnic_settings of this VnicEthIf.
        User Space NIC Settings that enable low-latency and higher throughput by bypassing the kernel layer when sending/receiving packets.  

        :return: The usnic_settings of this VnicEthIf.
        :rtype: VnicUsnicSettings
        """
        return self._usnic_settings

    @usnic_settings.setter
    def usnic_settings(self, usnic_settings):
        """
        Sets the usnic_settings of this VnicEthIf.
        User Space NIC Settings that enable low-latency and higher throughput by bypassing the kernel layer when sending/receiving packets.  

        :param usnic_settings: The usnic_settings of this VnicEthIf.
        :type: VnicUsnicSettings
        """

        self._usnic_settings = usnic_settings

    @property
    def vmq_settings(self):
        """
        Gets the vmq_settings of this VnicEthIf.
        Virtual Machine Queue Settings for the virtual interface that allow efficient transfer of network traffic to the guest OS.   

        :return: The vmq_settings of this VnicEthIf.
        :rtype: VnicVmqSettings
        """
        return self._vmq_settings

    @vmq_settings.setter
    def vmq_settings(self, vmq_settings):
        """
        Sets the vmq_settings of this VnicEthIf.
        Virtual Machine Queue Settings for the virtual interface that allow efficient transfer of network traffic to the guest OS.   

        :param vmq_settings: The vmq_settings of this VnicEthIf.
        :type: VnicVmqSettings
        """

        self._vmq_settings = vmq_settings

    @property
    def eth_adapter_policy(self):
        """
        Gets the eth_adapter_policy of this VnicEthIf.
        Relationship to the the Ethernet Adapter Policy. 

        :return: The eth_adapter_policy of this VnicEthIf.
        :rtype: VnicEthAdapterPolicyRef
        """
        return self._eth_adapter_policy

    @eth_adapter_policy.setter
    def eth_adapter_policy(self, eth_adapter_policy):
        """
        Sets the eth_adapter_policy of this VnicEthIf.
        Relationship to the the Ethernet Adapter Policy. 

        :param eth_adapter_policy: The eth_adapter_policy of this VnicEthIf.
        :type: VnicEthAdapterPolicyRef
        """

        self._eth_adapter_policy = eth_adapter_policy

    @property
    def eth_network_policy(self):
        """
        Gets the eth_network_policy of this VnicEthIf.
        Relationship to the Ethernet Network Policy. 

        :return: The eth_network_policy of this VnicEthIf.
        :rtype: VnicEthNetworkPolicyRef
        """
        return self._eth_network_policy

    @eth_network_policy.setter
    def eth_network_policy(self, eth_network_policy):
        """
        Sets the eth_network_policy of this VnicEthIf.
        Relationship to the Ethernet Network Policy. 

        :param eth_network_policy: The eth_network_policy of this VnicEthIf.
        :type: VnicEthNetworkPolicyRef
        """

        self._eth_network_policy = eth_network_policy

    @property
    def eth_qos_policy(self):
        """
        Gets the eth_qos_policy of this VnicEthIf.
        Relationship to the Ethernet QoS Policy. 

        :return: The eth_qos_policy of this VnicEthIf.
        :rtype: VnicEthQosPolicyRef
        """
        return self._eth_qos_policy

    @eth_qos_policy.setter
    def eth_qos_policy(self, eth_qos_policy):
        """
        Sets the eth_qos_policy of this VnicEthIf.
        Relationship to the Ethernet QoS Policy. 

        :param eth_qos_policy: The eth_qos_policy of this VnicEthIf.
        :type: VnicEthQosPolicyRef
        """

        self._eth_qos_policy = eth_qos_policy

    @property
    def lan_connectivity_policy(self):
        """
        Gets the lan_connectivity_policy of this VnicEthIf.
        Relationship to the LAN Connectivity Policy. 

        :return: The lan_connectivity_policy of this VnicEthIf.
        :rtype: VnicLanConnectivityPolicyRef
        """
        return self._lan_connectivity_policy

    @lan_connectivity_policy.setter
    def lan_connectivity_policy(self, lan_connectivity_policy):
        """
        Sets the lan_connectivity_policy of this VnicEthIf.
        Relationship to the LAN Connectivity Policy. 

        :param lan_connectivity_policy: The lan_connectivity_policy of this VnicEthIf.
        :type: VnicLanConnectivityPolicyRef
        """

        self._lan_connectivity_policy = lan_connectivity_policy

    @property
    def organization(self):
        """
        Gets the organization of this VnicEthIf.
        Relationship to the Organization that owns the Managed Object. 

        :return: The organization of this VnicEthIf.
        :rtype: OrganizationOrganizationRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this VnicEthIf.
        Relationship to the Organization that owns the Managed Object. 

        :param organization: The organization of this VnicEthIf.
        :type: OrganizationOrganizationRef
        """

        self._organization = organization

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, VnicEthIf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
