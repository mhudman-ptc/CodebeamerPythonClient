# coding: utf-8

"""
    Codebeamer swagger API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.abstract_field import AbstractField  # noqa: F401,E501

class TrackerChoiceField(AbstractField):
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
        'multiple_values': 'bool',
        'reference_type': 'str'
    }
    if hasattr(AbstractField, "swagger_types"):
        swagger_types.update(AbstractField.swagger_types)

    attribute_map = {
        'multiple_values': 'multipleValues',
        'reference_type': 'referenceType'
    }
    if hasattr(AbstractField, "attribute_map"):
        attribute_map.update(AbstractField.attribute_map)

    def __init__(self, multiple_values=None, reference_type=None, *args, **kwargs):  # noqa: E501
        """TrackerChoiceField - a model defined in Swagger"""  # noqa: E501
        self._multiple_values = None
        self._reference_type = None
        self.discriminator = None
        if multiple_values is not None:
            self.multiple_values = multiple_values
        if reference_type is not None:
            self.reference_type = reference_type
        AbstractField.__init__(self, *args, **kwargs)

    @property
    def multiple_values(self):
        """Gets the multiple_values of this TrackerChoiceField.  # noqa: E501

        Multiple values state of a field  # noqa: E501

        :return: The multiple_values of this TrackerChoiceField.  # noqa: E501
        :rtype: bool
        """
        return self._multiple_values

    @multiple_values.setter
    def multiple_values(self, multiple_values):
        """Sets the multiple_values of this TrackerChoiceField.

        Multiple values state of a field  # noqa: E501

        :param multiple_values: The multiple_values of this TrackerChoiceField.  # noqa: E501
        :type: bool
        """

        self._multiple_values = multiple_values

    @property
    def reference_type(self):
        """Gets the reference_type of this TrackerChoiceField.  # noqa: E501

        Type of the contained references  # noqa: E501

        :return: The reference_type of this TrackerChoiceField.  # noqa: E501
        :rtype: str
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type):
        """Sets the reference_type of this TrackerChoiceField.

        Type of the contained references  # noqa: E501

        :param reference_type: The reference_type of this TrackerChoiceField.  # noqa: E501
        :type: str
        """

        self._reference_type = reference_type

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
        if issubclass(TrackerChoiceField, dict):
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
        if not isinstance(other, TrackerChoiceField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
