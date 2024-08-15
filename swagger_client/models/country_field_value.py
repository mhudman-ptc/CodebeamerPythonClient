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
from swagger_client.models.abstract_field_value import AbstractFieldValue  # noqa: F401,E501

class CountryFieldValue(AbstractFieldValue):
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
        'values': 'list[str]'
    }
    if hasattr(AbstractFieldValue, "swagger_types"):
        swagger_types.update(AbstractFieldValue.swagger_types)

    attribute_map = {
        'values': 'values'
    }
    if hasattr(AbstractFieldValue, "attribute_map"):
        attribute_map.update(AbstractFieldValue.attribute_map)

    def __init__(self, values=None, *args, **kwargs):  # noqa: E501
        """CountryFieldValue - a model defined in Swagger"""  # noqa: E501
        self._values = None
        self.discriminator = None
        if values is not None:
            self.values = values
        AbstractFieldValue.__init__(self, *args, **kwargs)

    @property
    def values(self):
        """Gets the values of this CountryFieldValue.  # noqa: E501

        Country codes  # noqa: E501

        :return: The values of this CountryFieldValue.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this CountryFieldValue.

        Country codes  # noqa: E501

        :param values: The values of this CountryFieldValue.  # noqa: E501
        :type: list[str]
        """

        self._values = values

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
        if issubclass(CountryFieldValue, dict):
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
        if not isinstance(other, CountryFieldValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other