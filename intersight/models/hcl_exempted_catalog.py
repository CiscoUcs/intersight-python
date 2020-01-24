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


class HclExemptedCatalog(object):
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
        'comments': 'str',
        'name': 'str',
        'os_vendor': 'str',
        'os_version': 'str',
        'processor_name': 'str',
        'product_models': 'list[str]',
        'product_type': 'str',
        'server_pid': 'str',
        'ucs_version': 'str',
        'version_type': 'str'
    }

    attribute_map = {
        'comments': 'Comments',
        'name': 'Name',
        'os_vendor': 'OsVendor',
        'os_version': 'OsVersion',
        'processor_name': 'ProcessorName',
        'product_models': 'ProductModels',
        'product_type': 'ProductType',
        'server_pid': 'ServerPid',
        'ucs_version': 'UcsVersion',
        'version_type': 'VersionType'
    }

    def __init__(self,
                 comments=None,
                 name=None,
                 os_vendor=None,
                 os_version=None,
                 processor_name=None,
                 product_models=None,
                 product_type=None,
                 server_pid=None,
                 ucs_version=None,
                 version_type=None,
                 local_vars_configuration=None):  # noqa: E501
        """HclExemptedCatalog - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._comments = None
        self._name = None
        self._os_vendor = None
        self._os_version = None
        self._processor_name = None
        self._product_models = None
        self._product_type = None
        self._server_pid = None
        self._ucs_version = None
        self._version_type = None
        self.discriminator = None

        if comments is not None:
            self.comments = comments
        if name is not None:
            self.name = name
        if os_vendor is not None:
            self.os_vendor = os_vendor
        if os_version is not None:
            self.os_version = os_version
        if processor_name is not None:
            self.processor_name = processor_name
        if product_models is not None:
            self.product_models = product_models
        if product_type is not None:
            self.product_type = product_type
        if server_pid is not None:
            self.server_pid = server_pid
        if ucs_version is not None:
            self.ucs_version = ucs_version
        if version_type is not None:
            self.version_type = version_type

    @property
    def comments(self):
        """Gets the comments of this HclExemptedCatalog.  # noqa: E501

        Reason for the exemption.    # noqa: E501

        :return: The comments of this HclExemptedCatalog.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this HclExemptedCatalog.

        Reason for the exemption.    # noqa: E501

        :param comments: The comments of this HclExemptedCatalog.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def name(self):
        """Gets the name of this HclExemptedCatalog.  # noqa: E501

        A unique descriptive name of the exemption.    # noqa: E501

        :return: The name of this HclExemptedCatalog.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HclExemptedCatalog.

        A unique descriptive name of the exemption.    # noqa: E501

        :param name: The name of this HclExemptedCatalog.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def os_vendor(self):
        """Gets the os_vendor of this HclExemptedCatalog.  # noqa: E501

        Vendor of the Operating System.    # noqa: E501

        :return: The os_vendor of this HclExemptedCatalog.  # noqa: E501
        :rtype: str
        """
        return self._os_vendor

    @os_vendor.setter
    def os_vendor(self, os_vendor):
        """Sets the os_vendor of this HclExemptedCatalog.

        Vendor of the Operating System.    # noqa: E501

        :param os_vendor: The os_vendor of this HclExemptedCatalog.  # noqa: E501
        :type: str
        """

        self._os_vendor = os_vendor

    @property
    def os_version(self):
        """Gets the os_version of this HclExemptedCatalog.  # noqa: E501

        Version of the Operating system.    # noqa: E501

        :return: The os_version of this HclExemptedCatalog.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this HclExemptedCatalog.

        Version of the Operating system.    # noqa: E501

        :param os_version: The os_version of this HclExemptedCatalog.  # noqa: E501
        :type: str
        """

        self._os_version = os_version

    @property
    def processor_name(self):
        """Gets the processor_name of this HclExemptedCatalog.  # noqa: E501

        Name of the processor supported for the server.    # noqa: E501

        :return: The processor_name of this HclExemptedCatalog.  # noqa: E501
        :rtype: str
        """
        return self._processor_name

    @processor_name.setter
    def processor_name(self, processor_name):
        """Sets the processor_name of this HclExemptedCatalog.

        Name of the processor supported for the server.    # noqa: E501

        :param processor_name: The processor_name of this HclExemptedCatalog.  # noqa: E501
        :type: str
        """

        self._processor_name = processor_name

    @property
    def product_models(self):
        """Gets the product_models of this HclExemptedCatalog.  # noqa: E501


        :return: The product_models of this HclExemptedCatalog.  # noqa: E501
        :rtype: list[str]
        """
        return self._product_models

    @product_models.setter
    def product_models(self, product_models):
        """Sets the product_models of this HclExemptedCatalog.


        :param product_models: The product_models of this HclExemptedCatalog.  # noqa: E501
        :type: list[str]
        """

        self._product_models = product_models

    @property
    def product_type(self):
        """Gets the product_type of this HclExemptedCatalog.  # noqa: E501

        Type of the product/adapter say PT for Pass Through controllers.    # noqa: E501

        :return: The product_type of this HclExemptedCatalog.  # noqa: E501
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this HclExemptedCatalog.

        Type of the product/adapter say PT for Pass Through controllers.    # noqa: E501

        :param product_type: The product_type of this HclExemptedCatalog.  # noqa: E501
        :type: str
        """

        self._product_type = product_type

    @property
    def server_pid(self):
        """Gets the server_pid of this HclExemptedCatalog.  # noqa: E501

        Three part ID representing the server model as returned by UCSM/CIMC XML APIs.    # noqa: E501

        :return: The server_pid of this HclExemptedCatalog.  # noqa: E501
        :rtype: str
        """
        return self._server_pid

    @server_pid.setter
    def server_pid(self, server_pid):
        """Sets the server_pid of this HclExemptedCatalog.

        Three part ID representing the server model as returned by UCSM/CIMC XML APIs.    # noqa: E501

        :param server_pid: The server_pid of this HclExemptedCatalog.  # noqa: E501
        :type: str
        """

        self._server_pid = server_pid

    @property
    def ucs_version(self):
        """Gets the ucs_version of this HclExemptedCatalog.  # noqa: E501

        Version of the UCS software.    # noqa: E501

        :return: The ucs_version of this HclExemptedCatalog.  # noqa: E501
        :rtype: str
        """
        return self._ucs_version

    @ucs_version.setter
    def ucs_version(self, ucs_version):
        """Sets the ucs_version of this HclExemptedCatalog.

        Version of the UCS software.    # noqa: E501

        :param ucs_version: The ucs_version of this HclExemptedCatalog.  # noqa: E501
        :type: str
        """

        self._ucs_version = ucs_version

    @property
    def version_type(self):
        """Gets the version_type of this HclExemptedCatalog.  # noqa: E501

        Type of the UCS version indicating whether it is a UCSM release vesion or a IMC release.     # noqa: E501

        :return: The version_type of this HclExemptedCatalog.  # noqa: E501
        :rtype: str
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        """Sets the version_type of this HclExemptedCatalog.

        Type of the UCS version indicating whether it is a UCSM release vesion or a IMC release.     # noqa: E501

        :param version_type: The version_type of this HclExemptedCatalog.  # noqa: E501
        :type: str
        """

        self._version_type = version_type

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
        if not isinstance(other, HclExemptedCatalog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HclExemptedCatalog):
            return True

        return self.to_dict() != other.to_dict()
