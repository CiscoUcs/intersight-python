# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-255
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FirmwareDistributable(object):
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
        'ancestors': 'list[MoBaseMoRef]',
        'create_time': 'datetime',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'parent': 'MoBaseMoRef',
        'tags': 'list[MoTag]',
        'version_context': 'MoVersionContext',
        'bundle_type': 'str',
        'description': 'str',
        'guid': 'str',
        'md5sum': 'str',
        'mdfid': 'str',
        'model': 'str',
        'name': 'str',
        'page_index': 'str',
        'platform_type': 'str',
        'release_date': 'str',
        'size': 'str',
        'software_advisory_url': 'str',
        'software_type_id': 'str',
        'source': 'str',
        'supported_models': 'list[str]',
        'vendor': 'str',
        'version': 'str'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'ancestors': 'Ancestors',
        'create_time': 'CreateTime',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'parent': 'Parent',
        'tags': 'Tags',
        'version_context': 'VersionContext',
        'bundle_type': 'BundleType',
        'description': 'Description',
        'guid': 'Guid',
        'md5sum': 'Md5sum',
        'mdfid': 'Mdfid',
        'model': 'Model',
        'name': 'Name',
        'page_index': 'PageIndex',
        'platform_type': 'PlatformType',
        'release_date': 'ReleaseDate',
        'size': 'Size',
        'software_advisory_url': 'SoftwareAdvisoryUrl',
        'software_type_id': 'SoftwareTypeId',
        'source': 'Source',
        'supported_models': 'SupportedModels',
        'vendor': 'Vendor',
        'version': 'Version'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, bundle_type=None, description=None, guid=None, md5sum=None, mdfid=None, model=None, name=None, page_index=None, platform_type=None, release_date=None, size=None, software_advisory_url=None, software_type_id=None, source='CCO', supported_models=None, vendor=None, version=None):
        """
        FirmwareDistributable - a model defined in Swagger
        """

        self._account_moid = None
        self._ancestors = None
        self._create_time = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._parent = None
        self._tags = None
        self._version_context = None
        self._bundle_type = None
        self._description = None
        self._guid = None
        self._md5sum = None
        self._mdfid = None
        self._model = None
        self._name = None
        self._page_index = None
        self._platform_type = None
        self._release_date = None
        self._size = None
        self._software_advisory_url = None
        self._software_type_id = None
        self._source = None
        self._supported_models = None
        self._vendor = None
        self._version = None

        if account_moid is not None:
          self.account_moid = account_moid
        if ancestors is not None:
          self.ancestors = ancestors
        if create_time is not None:
          self.create_time = create_time
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if parent is not None:
          self.parent = parent
        if tags is not None:
          self.tags = tags
        if version_context is not None:
          self.version_context = version_context
        if bundle_type is not None:
          self.bundle_type = bundle_type
        if description is not None:
          self.description = description
        if guid is not None:
          self.guid = guid
        if md5sum is not None:
          self.md5sum = md5sum
        if mdfid is not None:
          self.mdfid = mdfid
        if model is not None:
          self.model = model
        if name is not None:
          self.name = name
        if page_index is not None:
          self.page_index = page_index
        if platform_type is not None:
          self.platform_type = platform_type
        if release_date is not None:
          self.release_date = release_date
        if size is not None:
          self.size = size
        if software_advisory_url is not None:
          self.software_advisory_url = software_advisory_url
        if software_type_id is not None:
          self.software_type_id = software_type_id
        if source is not None:
          self.source = source
        if supported_models is not None:
          self.supported_models = supported_models
        if vendor is not None:
          self.vendor = vendor
        if version is not None:
          self.version = version

    @property
    def account_moid(self):
        """
        Gets the account_moid of this FirmwareDistributable.
        The Account ID for this managed object.  

        :return: The account_moid of this FirmwareDistributable.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this FirmwareDistributable.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this FirmwareDistributable.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this FirmwareDistributable.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this FirmwareDistributable.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this FirmwareDistributable.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this FirmwareDistributable.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this FirmwareDistributable.
        The time when this managed object was created.  

        :return: The create_time of this FirmwareDistributable.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this FirmwareDistributable.
        The time when this managed object was created.  

        :param create_time: The create_time of this FirmwareDistributable.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this FirmwareDistributable.
        The time when this managed object was last modified.  

        :return: The mod_time of this FirmwareDistributable.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this FirmwareDistributable.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this FirmwareDistributable.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this FirmwareDistributable.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this FirmwareDistributable.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this FirmwareDistributable.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this FirmwareDistributable.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this FirmwareDistributable.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this FirmwareDistributable.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this FirmwareDistributable.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this FirmwareDistributable.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this FirmwareDistributable.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this FirmwareDistributable.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this FirmwareDistributable.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this FirmwareDistributable.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this FirmwareDistributable.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this FirmwareDistributable.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this FirmwareDistributable.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this FirmwareDistributable.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this FirmwareDistributable.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this FirmwareDistributable.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this FirmwareDistributable.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this FirmwareDistributable.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this FirmwareDistributable.
        The versioning info for this managed object   

        :return: The version_context of this FirmwareDistributable.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this FirmwareDistributable.
        The versioning info for this managed object   

        :param version_context: The version_context of this FirmwareDistributable.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def bundle_type(self):
        """
        Gets the bundle_type of this FirmwareDistributable.
        Bundle type of the firmware image  

        :return: The bundle_type of this FirmwareDistributable.
        :rtype: str
        """
        return self._bundle_type

    @bundle_type.setter
    def bundle_type(self, bundle_type):
        """
        Sets the bundle_type of this FirmwareDistributable.
        Bundle type of the firmware image  

        :param bundle_type: The bundle_type of this FirmwareDistributable.
        :type: str
        """

        self._bundle_type = bundle_type

    @property
    def description(self):
        """
        Gets the description of this FirmwareDistributable.
        Description of the firmware image  

        :return: The description of this FirmwareDistributable.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FirmwareDistributable.
        Description of the firmware image  

        :param description: The description of this FirmwareDistributable.
        :type: str
        """

        self._description = description

    @property
    def guid(self):
        """
        Gets the guid of this FirmwareDistributable.
        Guid of the firmware image  

        :return: The guid of this FirmwareDistributable.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """
        Sets the guid of this FirmwareDistributable.
        Guid of the firmware image  

        :param guid: The guid of this FirmwareDistributable.
        :type: str
        """

        self._guid = guid

    @property
    def md5sum(self):
        """
        Gets the md5sum of this FirmwareDistributable.
        MD5 sum of the firmware image  

        :return: The md5sum of this FirmwareDistributable.
        :rtype: str
        """
        return self._md5sum

    @md5sum.setter
    def md5sum(self, md5sum):
        """
        Sets the md5sum of this FirmwareDistributable.
        MD5 sum of the firmware image  

        :param md5sum: The md5sum of this FirmwareDistributable.
        :type: str
        """

        self._md5sum = md5sum

    @property
    def mdfid(self):
        """
        Gets the mdfid of this FirmwareDistributable.
        Mdfid of the firmware image  

        :return: The mdfid of this FirmwareDistributable.
        :rtype: str
        """
        return self._mdfid

    @mdfid.setter
    def mdfid(self, mdfid):
        """
        Sets the mdfid of this FirmwareDistributable.
        Mdfid of the firmware image  

        :param mdfid: The mdfid of this FirmwareDistributable.
        :type: str
        """

        self._mdfid = mdfid

    @property
    def model(self):
        """
        Gets the model of this FirmwareDistributable.
        Model of the endpoint the firmware image is for  

        :return: The model of this FirmwareDistributable.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this FirmwareDistributable.
        Model of the endpoint the firmware image is for  

        :param model: The model of this FirmwareDistributable.
        :type: str
        """

        self._model = model

    @property
    def name(self):
        """
        Gets the name of this FirmwareDistributable.
        Iso image name of the firmware image  

        :return: The name of this FirmwareDistributable.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FirmwareDistributable.
        Iso image name of the firmware image  

        :param name: The name of this FirmwareDistributable.
        :type: str
        """

        self._name = name

    @property
    def page_index(self):
        """
        Gets the page_index of this FirmwareDistributable.
        Page number where firmware image is present in Cisco Software Repository  

        :return: The page_index of this FirmwareDistributable.
        :rtype: str
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """
        Sets the page_index of this FirmwareDistributable.
        Page number where firmware image is present in Cisco Software Repository  

        :param page_index: The page_index of this FirmwareDistributable.
        :type: str
        """

        self._page_index = page_index

    @property
    def platform_type(self):
        """
        Gets the platform_type of this FirmwareDistributable.
        Platform type of the firmware image  

        :return: The platform_type of this FirmwareDistributable.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """
        Sets the platform_type of this FirmwareDistributable.
        Platform type of the firmware image  

        :param platform_type: The platform_type of this FirmwareDistributable.
        :type: str
        """

        self._platform_type = platform_type

    @property
    def release_date(self):
        """
        Gets the release_date of this FirmwareDistributable.
        Release date of the firmware image  

        :return: The release_date of this FirmwareDistributable.
        :rtype: str
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """
        Sets the release_date of this FirmwareDistributable.
        Release date of the firmware image  

        :param release_date: The release_date of this FirmwareDistributable.
        :type: str
        """

        self._release_date = release_date

    @property
    def size(self):
        """
        Gets the size of this FirmwareDistributable.
        Size of the firmware image  

        :return: The size of this FirmwareDistributable.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this FirmwareDistributable.
        Size of the firmware image  

        :param size: The size of this FirmwareDistributable.
        :type: str
        """

        self._size = size

    @property
    def software_advisory_url(self):
        """
        Gets the software_advisory_url of this FirmwareDistributable.
        Software Advisory for firmware image from Cisco software repository. Read and accept the software advisory before downloading the firmware image.  

        :return: The software_advisory_url of this FirmwareDistributable.
        :rtype: str
        """
        return self._software_advisory_url

    @software_advisory_url.setter
    def software_advisory_url(self, software_advisory_url):
        """
        Sets the software_advisory_url of this FirmwareDistributable.
        Software Advisory for firmware image from Cisco software repository. Read and accept the software advisory before downloading the firmware image.  

        :param software_advisory_url: The software_advisory_url of this FirmwareDistributable.
        :type: str
        """

        self._software_advisory_url = software_advisory_url

    @property
    def software_type_id(self):
        """
        Gets the software_type_id of this FirmwareDistributable.
        Software type Id of the firmware image  

        :return: The software_type_id of this FirmwareDistributable.
        :rtype: str
        """
        return self._software_type_id

    @software_type_id.setter
    def software_type_id(self, software_type_id):
        """
        Sets the software_type_id of this FirmwareDistributable.
        Software type Id of the firmware image  

        :param software_type_id: The software_type_id of this FirmwareDistributable.
        :type: str
        """

        self._software_type_id = software_type_id

    @property
    def source(self):
        """
        Gets the source of this FirmwareDistributable.
        Source of firmware images  

        :return: The source of this FirmwareDistributable.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this FirmwareDistributable.
        Source of firmware images  

        :param source: The source of this FirmwareDistributable.
        :type: str
        """
        allowed_values = ["CCO"]
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def supported_models(self):
        """
        Gets the supported_models of this FirmwareDistributable.
        Supported models of the endpoint the firmware image is for  

        :return: The supported_models of this FirmwareDistributable.
        :rtype: list[str]
        """
        return self._supported_models

    @supported_models.setter
    def supported_models(self, supported_models):
        """
        Sets the supported_models of this FirmwareDistributable.
        Supported models of the endpoint the firmware image is for  

        :param supported_models: The supported_models of this FirmwareDistributable.
        :type: list[str]
        """

        self._supported_models = supported_models

    @property
    def vendor(self):
        """
        Gets the vendor of this FirmwareDistributable.
        Vendor of the firmware image  

        :return: The vendor of this FirmwareDistributable.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this FirmwareDistributable.
        Vendor of the firmware image  

        :param vendor: The vendor of this FirmwareDistributable.
        :type: str
        """

        self._vendor = vendor

    @property
    def version(self):
        """
        Gets the version of this FirmwareDistributable.
        Version of the firmware image   

        :return: The version of this FirmwareDistributable.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this FirmwareDistributable.
        Version of the firmware image   

        :param version: The version of this FirmwareDistributable.
        :type: str
        """

        self._version = version

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
        if not isinstance(other, FirmwareDistributable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
