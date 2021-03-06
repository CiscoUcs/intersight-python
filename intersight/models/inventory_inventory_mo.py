# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1461
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InventoryInventoryMo(object):
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
        'object_type': 'str',
        'mo_dn': 'str',
        'mo_id': 'str',
        'mo_type': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'mo_dn': 'MoDn',
        'mo_id': 'MoId',
        'mo_type': 'MoType'
    }

    def __init__(self, object_type=None, mo_dn=None, mo_id=None, mo_type=None):
        """
        InventoryInventoryMo - a model defined in Swagger
        """

        self._object_type = None
        self._mo_dn = None
        self._mo_id = None
        self._mo_type = None

        if object_type is not None:
          self.object_type = object_type
        if mo_dn is not None:
          self.mo_dn = mo_dn
        if mo_id is not None:
          self.mo_id = mo_id
        if mo_type is not None:
          self.mo_type = mo_type

    @property
    def object_type(self):
        """
        Gets the object_type of this InventoryInventoryMo.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :return: The object_type of this InventoryInventoryMo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this InventoryInventoryMo.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :param object_type: The object_type of this InventoryInventoryMo.
        :type: str
        """

        self._object_type = object_type

    @property
    def mo_dn(self):
        """
        Gets the mo_dn of this InventoryInventoryMo.
        The UCS DN of the MO for which the latest inventory to be fetched. If this property is empty and moId property has the Moid of the MO to be updated, the Moid will be used. If this property is empty and moId is also empty, all the MOs of the given moType will be updated.

        :return: The mo_dn of this InventoryInventoryMo.
        :rtype: str
        """
        return self._mo_dn

    @mo_dn.setter
    def mo_dn(self, mo_dn):
        """
        Sets the mo_dn of this InventoryInventoryMo.
        The UCS DN of the MO for which the latest inventory to be fetched. If this property is empty and moId property has the Moid of the MO to be updated, the Moid will be used. If this property is empty and moId is also empty, all the MOs of the given moType will be updated.

        :param mo_dn: The mo_dn of this InventoryInventoryMo.
        :type: str
        """

        self._mo_dn = mo_dn

    @property
    def mo_id(self):
        """
        Gets the mo_id of this InventoryInventoryMo.
        The MO id of an MO for which the latest inventory to be fetched. If this property is empty and moDn property has the UCS DN of the MO to be updated, the DN will be used. If this property is empty and moDn is also empty, all the MOs of the given moType will be updated.

        :return: The mo_id of this InventoryInventoryMo.
        :rtype: str
        """
        return self._mo_id

    @mo_id.setter
    def mo_id(self, mo_id):
        """
        Sets the mo_id of this InventoryInventoryMo.
        The MO id of an MO for which the latest inventory to be fetched. If this property is empty and moDn property has the UCS DN of the MO to be updated, the DN will be used. If this property is empty and moDn is also empty, all the MOs of the given moType will be updated.

        :param mo_id: The mo_id of this InventoryInventoryMo.
        :type: str
        """

        self._mo_id = mo_id

    @property
    def mo_type(self):
        """
        Gets the mo_type of this InventoryInventoryMo.
        The type of the MO for which the latest inventory to be fetched.

        :return: The mo_type of this InventoryInventoryMo.
        :rtype: str
        """
        return self._mo_type

    @mo_type.setter
    def mo_type(self, mo_type):
        """
        Sets the mo_type of this InventoryInventoryMo.
        The type of the MO for which the latest inventory to be fetched.

        :param mo_type: The mo_type of this InventoryInventoryMo.
        :type: str
        """

        self._mo_type = mo_type

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
        if not isinstance(other, InventoryInventoryMo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
