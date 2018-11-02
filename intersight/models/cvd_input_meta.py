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


class CvdInputMeta(object):
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
        'field_filter': 'str',
        'field_label': 'str',
        'field_name': 'str',
        'field_value': 'str'
    }

    attribute_map = {
        'field_filter': 'FieldFilter',
        'field_label': 'FieldLabel',
        'field_name': 'FieldName',
        'field_value': 'FieldValue'
    }

    def __init__(self, field_filter=None, field_label=None, field_name=None, field_value=None):
        """
        CvdInputMeta - a model defined in Swagger
        """

        self._field_filter = None
        self._field_label = None
        self._field_name = None
        self._field_value = None

        if field_filter is not None:
          self.field_filter = field_filter
        if field_label is not None:
          self.field_label = field_label
        if field_name is not None:
          self.field_name = field_name
        if field_value is not None:
          self.field_value = field_value

    @property
    def field_filter(self):
        """
        Gets the field_filter of this CvdInputMeta.
        Input field filter(REST API path with filter which will return the list of applicable values for this field)  

        :return: The field_filter of this CvdInputMeta.
        :rtype: str
        """
        return self._field_filter

    @field_filter.setter
    def field_filter(self, field_filter):
        """
        Sets the field_filter of this CvdInputMeta.
        Input field filter(REST API path with filter which will return the list of applicable values for this field)  

        :param field_filter: The field_filter of this CvdInputMeta.
        :type: str
        """

        self._field_filter = field_filter

    @property
    def field_label(self):
        """
        Gets the field_label of this CvdInputMeta.
        Input field label(for GUI use)  

        :return: The field_label of this CvdInputMeta.
        :rtype: str
        """
        return self._field_label

    @field_label.setter
    def field_label(self, field_label):
        """
        Sets the field_label of this CvdInputMeta.
        Input field label(for GUI use)  

        :param field_label: The field_label of this CvdInputMeta.
        :type: str
        """

        self._field_label = field_label

    @property
    def field_name(self):
        """
        Gets the field_name of this CvdInputMeta.
        Input field name  

        :return: The field_name of this CvdInputMeta.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """
        Sets the field_name of this CvdInputMeta.
        Input field name  

        :param field_name: The field_name of this CvdInputMeta.
        :type: str
        """

        self._field_name = field_name

    @property
    def field_value(self):
        """
        Gets the field_value of this CvdInputMeta.
        Input field value   

        :return: The field_value of this CvdInputMeta.
        :rtype: str
        """
        return self._field_value

    @field_value.setter
    def field_value(self, field_value):
        """
        Sets the field_value of this CvdInputMeta.
        Input field value   

        :param field_value: The field_value of this CvdInputMeta.
        :type: str
        """

        self._field_value = field_value

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
        if not isinstance(other, CvdInputMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
