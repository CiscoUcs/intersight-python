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


class GraphicsCard(object):
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
        'device_mo_id': 'str',
        'dn': 'str',
        'rn': 'str',
        'model': 'str',
        'revision': 'str',
        'serial': 'str',
        'vendor': 'str',
        'card_id': 'int',
        'device_id': 'int',
        'expander_slot': 'str',
        'firmware_version': 'str',
        'mode': 'str',
        'num_gpus': 'str',
        'oper_state': 'str',
        'pci_address': 'str',
        'pci_address_list': 'str',
        'pci_slot': 'str',
        'compute_board': 'ComputeBoardRef',
        'graphics_controllers': 'list[GraphicsControllerRef]',
        'registered_device': 'AssetDeviceRegistrationRef'
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
        'device_mo_id': 'DeviceMoId',
        'dn': 'Dn',
        'rn': 'Rn',
        'model': 'Model',
        'revision': 'Revision',
        'serial': 'Serial',
        'vendor': 'Vendor',
        'card_id': 'CardId',
        'device_id': 'DeviceId',
        'expander_slot': 'ExpanderSlot',
        'firmware_version': 'FirmwareVersion',
        'mode': 'Mode',
        'num_gpus': 'NumGpus',
        'oper_state': 'OperState',
        'pci_address': 'PciAddress',
        'pci_address_list': 'PciAddressList',
        'pci_slot': 'PciSlot',
        'compute_board': 'ComputeBoard',
        'graphics_controllers': 'GraphicsControllers',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, card_id=None, device_id=None, expander_slot=None, firmware_version=None, mode=None, num_gpus=None, oper_state=None, pci_address=None, pci_address_list=None, pci_slot=None, compute_board=None, graphics_controllers=None, registered_device=None):
        """
        GraphicsCard - a model defined in Swagger
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
        self._device_mo_id = None
        self._dn = None
        self._rn = None
        self._model = None
        self._revision = None
        self._serial = None
        self._vendor = None
        self._card_id = None
        self._device_id = None
        self._expander_slot = None
        self._firmware_version = None
        self._mode = None
        self._num_gpus = None
        self._oper_state = None
        self._pci_address = None
        self._pci_address_list = None
        self._pci_slot = None
        self._compute_board = None
        self._graphics_controllers = None
        self._registered_device = None

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
        if device_mo_id is not None:
          self.device_mo_id = device_mo_id
        if dn is not None:
          self.dn = dn
        if rn is not None:
          self.rn = rn
        if model is not None:
          self.model = model
        if revision is not None:
          self.revision = revision
        if serial is not None:
          self.serial = serial
        if vendor is not None:
          self.vendor = vendor
        if card_id is not None:
          self.card_id = card_id
        if device_id is not None:
          self.device_id = device_id
        if expander_slot is not None:
          self.expander_slot = expander_slot
        if firmware_version is not None:
          self.firmware_version = firmware_version
        if mode is not None:
          self.mode = mode
        if num_gpus is not None:
          self.num_gpus = num_gpus
        if oper_state is not None:
          self.oper_state = oper_state
        if pci_address is not None:
          self.pci_address = pci_address
        if pci_address_list is not None:
          self.pci_address_list = pci_address_list
        if pci_slot is not None:
          self.pci_slot = pci_slot
        if compute_board is not None:
          self.compute_board = compute_board
        if graphics_controllers is not None:
          self.graphics_controllers = graphics_controllers
        if registered_device is not None:
          self.registered_device = registered_device

    @property
    def account_moid(self):
        """
        Gets the account_moid of this GraphicsCard.
        The Account ID for this managed object.  

        :return: The account_moid of this GraphicsCard.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this GraphicsCard.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this GraphicsCard.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this GraphicsCard.
        The time when this managed object was created.  

        :return: The create_time of this GraphicsCard.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this GraphicsCard.
        The time when this managed object was created.  

        :param create_time: The create_time of this GraphicsCard.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this GraphicsCard.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this GraphicsCard.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this GraphicsCard.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this GraphicsCard.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this GraphicsCard.
        The time when this managed object was last modified.  

        :return: The mod_time of this GraphicsCard.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this GraphicsCard.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this GraphicsCard.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this GraphicsCard.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this GraphicsCard.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this GraphicsCard.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this GraphicsCard.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this GraphicsCard.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this GraphicsCard.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this GraphicsCard.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this GraphicsCard.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this GraphicsCard.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this GraphicsCard.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this GraphicsCard.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this GraphicsCard.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this GraphicsCard.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this GraphicsCard.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this GraphicsCard.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this GraphicsCard.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this GraphicsCard.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this GraphicsCard.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this GraphicsCard.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this GraphicsCard.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this GraphicsCard.
        The versioning info for this managed object.   

        :return: The version_context of this GraphicsCard.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this GraphicsCard.
        The versioning info for this managed object.   

        :param version_context: The version_context of this GraphicsCard.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this GraphicsCard.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this GraphicsCard.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this GraphicsCard.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this GraphicsCard.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this GraphicsCard.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this GraphicsCard.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this GraphicsCard.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this GraphicsCard.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this GraphicsCard.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this GraphicsCard.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this GraphicsCard.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this GraphicsCard.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this GraphicsCard.

        :return: The device_mo_id of this GraphicsCard.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this GraphicsCard.

        :param device_mo_id: The device_mo_id of this GraphicsCard.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this GraphicsCard.
        The Distinguished Name unambiguously identifies an object in the system.  

        :return: The dn of this GraphicsCard.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this GraphicsCard.
        The Distinguished Name unambiguously identifies an object in the system.  

        :param dn: The dn of this GraphicsCard.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this GraphicsCard.
        The Relative Name uniquely identifies an object within a given context.   

        :return: The rn of this GraphicsCard.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this GraphicsCard.
        The Relative Name uniquely identifies an object within a given context.   

        :param rn: The rn of this GraphicsCard.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this GraphicsCard.
        This field identifies the model of the given component.  

        :return: The model of this GraphicsCard.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this GraphicsCard.
        This field identifies the model of the given component.  

        :param model: The model of this GraphicsCard.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this GraphicsCard.

        :return: The revision of this GraphicsCard.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this GraphicsCard.

        :param revision: The revision of this GraphicsCard.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this GraphicsCard.
        This field identifies the serial of the given component.  

        :return: The serial of this GraphicsCard.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this GraphicsCard.
        This field identifies the serial of the given component.  

        :param serial: The serial of this GraphicsCard.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this GraphicsCard.
        This field identifies the vendor of the given component.   

        :return: The vendor of this GraphicsCard.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this GraphicsCard.
        This field identifies the vendor of the given component.   

        :param vendor: The vendor of this GraphicsCard.
        :type: str
        """

        self._vendor = vendor

    @property
    def card_id(self):
        """
        Gets the card_id of this GraphicsCard.
        It shows the id of graphics card.  

        :return: The card_id of this GraphicsCard.
        :rtype: int
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id):
        """
        Sets the card_id of this GraphicsCard.
        It shows the id of graphics card.  

        :param card_id: The card_id of this GraphicsCard.
        :type: int
        """

        self._card_id = card_id

    @property
    def device_id(self):
        """
        Gets the device_id of this GraphicsCard.
        It shows the device id of grphics card.  

        :return: The device_id of this GraphicsCard.
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this GraphicsCard.
        It shows the device id of grphics card.  

        :param device_id: The device_id of this GraphicsCard.
        :type: int
        """

        self._device_id = device_id

    @property
    def expander_slot(self):
        """
        Gets the expander_slot of this GraphicsCard.
        It shows the expander slot inforamtion for the card.  

        :return: The expander_slot of this GraphicsCard.
        :rtype: str
        """
        return self._expander_slot

    @expander_slot.setter
    def expander_slot(self, expander_slot):
        """
        Sets the expander_slot of this GraphicsCard.
        It shows the expander slot inforamtion for the card.  

        :param expander_slot: The expander_slot of this GraphicsCard.
        :type: str
        """

        self._expander_slot = expander_slot

    @property
    def firmware_version(self):
        """
        Gets the firmware_version of this GraphicsCard.
        It shows current firmware version of graphics card.  

        :return: The firmware_version of this GraphicsCard.
        :rtype: str
        """
        return self._firmware_version

    @firmware_version.setter
    def firmware_version(self, firmware_version):
        """
        Sets the firmware_version of this GraphicsCard.
        It shows current firmware version of graphics card.  

        :param firmware_version: The firmware_version of this GraphicsCard.
        :type: str
        """

        self._firmware_version = firmware_version

    @property
    def mode(self):
        """
        Gets the mode of this GraphicsCard.
        It shows the current mode of graphics card.  

        :return: The mode of this GraphicsCard.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this GraphicsCard.
        It shows the current mode of graphics card.  

        :param mode: The mode of this GraphicsCard.
        :type: str
        """

        self._mode = mode

    @property
    def num_gpus(self):
        """
        Gets the num_gpus of this GraphicsCard.
        It shows number of controllers under each card.  

        :return: The num_gpus of this GraphicsCard.
        :rtype: str
        """
        return self._num_gpus

    @num_gpus.setter
    def num_gpus(self, num_gpus):
        """
        Sets the num_gpus of this GraphicsCard.
        It shows number of controllers under each card.  

        :param num_gpus: The num_gpus of this GraphicsCard.
        :type: str
        """

        self._num_gpus = num_gpus

    @property
    def oper_state(self):
        """
        Gets the oper_state of this GraphicsCard.
        It shows the current operational state of graphics card.  

        :return: The oper_state of this GraphicsCard.
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """
        Sets the oper_state of this GraphicsCard.
        It shows the current operational state of graphics card.  

        :param oper_state: The oper_state of this GraphicsCard.
        :type: str
        """

        self._oper_state = oper_state

    @property
    def pci_address(self):
        """
        Gets the pci_address of this GraphicsCard.
        It shows the pci address of graphics card.  

        :return: The pci_address of this GraphicsCard.
        :rtype: str
        """
        return self._pci_address

    @pci_address.setter
    def pci_address(self, pci_address):
        """
        Sets the pci_address of this GraphicsCard.
        It shows the pci address of graphics card.  

        :param pci_address: The pci_address of this GraphicsCard.
        :type: str
        """

        self._pci_address = pci_address

    @property
    def pci_address_list(self):
        """
        Gets the pci_address_list of this GraphicsCard.
        This list contains the pci address of all controllers for corresponding card.  

        :return: The pci_address_list of this GraphicsCard.
        :rtype: str
        """
        return self._pci_address_list

    @pci_address_list.setter
    def pci_address_list(self, pci_address_list):
        """
        Sets the pci_address_list of this GraphicsCard.
        This list contains the pci address of all controllers for corresponding card.  

        :param pci_address_list: The pci_address_list of this GraphicsCard.
        :type: str
        """

        self._pci_address_list = pci_address_list

    @property
    def pci_slot(self):
        """
        Gets the pci_slot of this GraphicsCard.
        It shows the pci slot name for grapchics card.   

        :return: The pci_slot of this GraphicsCard.
        :rtype: str
        """
        return self._pci_slot

    @pci_slot.setter
    def pci_slot(self, pci_slot):
        """
        Sets the pci_slot of this GraphicsCard.
        It shows the pci slot name for grapchics card.   

        :param pci_slot: The pci_slot of this GraphicsCard.
        :type: str
        """

        self._pci_slot = pci_slot

    @property
    def compute_board(self):
        """
        Gets the compute_board of this GraphicsCard.
        A collection of references to the [compute.Board](mo://compute.Board) Managed Object.  When this managed object is deleted, the referenced [compute.Board](mo://compute.Board) MO unsets its reference to this deleted MO. 

        :return: The compute_board of this GraphicsCard.
        :rtype: ComputeBoardRef
        """
        return self._compute_board

    @compute_board.setter
    def compute_board(self, compute_board):
        """
        Sets the compute_board of this GraphicsCard.
        A collection of references to the [compute.Board](mo://compute.Board) Managed Object.  When this managed object is deleted, the referenced [compute.Board](mo://compute.Board) MO unsets its reference to this deleted MO. 

        :param compute_board: The compute_board of this GraphicsCard.
        :type: ComputeBoardRef
        """

        self._compute_board = compute_board

    @property
    def graphics_controllers(self):
        """
        Gets the graphics_controllers of this GraphicsCard.
        It shows the controllers under each graphics card. 

        :return: The graphics_controllers of this GraphicsCard.
        :rtype: list[GraphicsControllerRef]
        """
        return self._graphics_controllers

    @graphics_controllers.setter
    def graphics_controllers(self, graphics_controllers):
        """
        Sets the graphics_controllers of this GraphicsCard.
        It shows the controllers under each graphics card. 

        :param graphics_controllers: The graphics_controllers of this GraphicsCard.
        :type: list[GraphicsControllerRef]
        """

        self._graphics_controllers = graphics_controllers

    @property
    def registered_device(self):
        """
        Gets the registered_device of this GraphicsCard.
        The Device to which this Managed Object is associated. 

        :return: The registered_device of this GraphicsCard.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this GraphicsCard.
        The Device to which this Managed Object is associated. 

        :param registered_device: The registered_device of this GraphicsCard.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

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
        if not isinstance(other, GraphicsCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
