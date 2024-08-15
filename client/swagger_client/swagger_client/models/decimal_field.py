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
from swagger_client.models.abstract_field import AbstractField  # noqa: F401,E501

class DecimalField(AbstractField):
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
        'max': 'float',
        'min': 'float'
    }
    if hasattr(AbstractField, "swagger_types"):
        swagger_types.update(AbstractField.swagger_types)

    attribute_map = {
        'max': 'max',
        'min': 'min'
    }
    if hasattr(AbstractField, "attribute_map"):
        attribute_map.update(AbstractField.attribute_map)

    def __init__(self, max=None, min=None, *args, **kwargs):  # noqa: E501
        """DecimalField - a model defined in Swagger"""  # noqa: E501
        self._max = None
        self._min = None
        self.discriminator = None
        if max is not None:
            self.max = max
        if min is not None:
            self.min = min
        AbstractField.__init__(self, *args, **kwargs)

    @property
    def max(self):
        """Gets the max of this DecimalField.  # noqa: E501

        Maximum value of a field  # noqa: E501

        :return: The max of this DecimalField.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this DecimalField.

        Maximum value of a field  # noqa: E501

        :param max: The max of this DecimalField.  # noqa: E501
        :type: float
        """

        self._max = max

    @property
    def min(self):
        """Gets the min of this DecimalField.  # noqa: E501

        Minimum value of a field  # noqa: E501

        :return: The min of this DecimalField.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this DecimalField.

        Minimum value of a field  # noqa: E501

        :param min: The min of this DecimalField.  # noqa: E501
        :type: float
        """

        self._min = min

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
        if issubclass(DecimalField, dict):
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
        if not isinstance(other, DecimalField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
