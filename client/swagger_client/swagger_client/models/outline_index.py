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

class OutlineIndex(object):
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
        'index': 'int',
        'level': 'int'
    }

    attribute_map = {
        'index': 'index',
        'level': 'level'
    }

    def __init__(self, index=None, level=None):  # noqa: E501
        """OutlineIndex - a model defined in Swagger"""  # noqa: E501
        self._index = None
        self._level = None
        self.discriminator = None
        if index is not None:
            self.index = index
        if level is not None:
            self.level = level

    @property
    def index(self):
        """Gets the index of this OutlineIndex.  # noqa: E501

        Outline index  # noqa: E501

        :return: The index of this OutlineIndex.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this OutlineIndex.

        Outline index  # noqa: E501

        :param index: The index of this OutlineIndex.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def level(self):
        """Gets the level of this OutlineIndex.  # noqa: E501

        Outline level  # noqa: E501

        :return: The level of this OutlineIndex.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this OutlineIndex.

        Outline level  # noqa: E501

        :param level: The level of this OutlineIndex.  # noqa: E501
        :type: int
        """

        self._level = level

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
        if issubclass(OutlineIndex, dict):
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
        if not isinstance(other, OutlineIndex):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
