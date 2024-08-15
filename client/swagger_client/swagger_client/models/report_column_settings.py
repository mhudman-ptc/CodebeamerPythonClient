# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ReportColumnSettings(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'column_index': 'int',
        'field': 'FieldReference'
    }

    attribute_map = {
        'column_index': 'columnIndex',
        'field': 'field'
    }

    def __init__(self, column_index=None, field=None):  # noqa: E501
        """ReportColumnSettings - a model defined in Swagger"""  # noqa: E501
        self._column_index = None
        self._field = None
        self.discriminator = None
        self.column_index = column_index
        self.field = field

    @property
    def column_index(self):
        """Gets the column_index of this ReportColumnSettings.  # noqa: E501

        Index of the column in the report table.  # noqa: E501

        :return: The column_index of this ReportColumnSettings.  # noqa: E501
        :rtype: int
        """
        return self._column_index

    @column_index.setter
    def column_index(self, column_index):
        """Sets the column_index of this ReportColumnSettings.

        Index of the column in the report table.  # noqa: E501

        :param column_index: The column_index of this ReportColumnSettings.  # noqa: E501
        :type: int
        """
        if column_index is None:
            raise ValueError("Invalid value for `column_index`, must not be `None`")  # noqa: E501

        self._column_index = column_index

    @property
    def field(self):
        """Gets the field of this ReportColumnSettings.  # noqa: E501


        :return: The field of this ReportColumnSettings.  # noqa: E501
        :rtype: FieldReference
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this ReportColumnSettings.


        :param field: The field of this ReportColumnSettings.  # noqa: E501
        :type: FieldReference
        """
        if field is None:
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501

        self._field = field

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ReportColumnSettings, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReportColumnSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other