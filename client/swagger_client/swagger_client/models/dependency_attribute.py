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

class DependencyAttribute(object):
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
        'lookup_direction': 'str',
        'path': 'list[DependencyEntityReference]'
    }

    attribute_map = {
        'lookup_direction': 'lookupDirection',
        'path': 'path'
    }

    def __init__(self, lookup_direction=None, path=None):  # noqa: E501
        """DependencyAttribute - a model defined in Swagger"""  # noqa: E501
        self._lookup_direction = None
        self._path = None
        self.discriminator = None
        if lookup_direction is not None:
            self.lookup_direction = lookup_direction
        if path is not None:
            self.path = path

    @property
    def lookup_direction(self):
        """Gets the lookup_direction of this DependencyAttribute.  # noqa: E501

        Direction in which dependency finder discovered the reference.  # noqa: E501

        :return: The lookup_direction of this DependencyAttribute.  # noqa: E501
        :rtype: str
        """
        return self._lookup_direction

    @lookup_direction.setter
    def lookup_direction(self, lookup_direction):
        """Sets the lookup_direction of this DependencyAttribute.

        Direction in which dependency finder discovered the reference.  # noqa: E501

        :param lookup_direction: The lookup_direction of this DependencyAttribute.  # noqa: E501
        :type: str
        """
        allowed_values = ["Forward", "Bidirectional"]  # noqa: E501
        if lookup_direction not in allowed_values:
            raise ValueError(
                "Invalid value for `lookup_direction` ({0}), must be one of {1}"  # noqa: E501
                .format(lookup_direction, allowed_values)
            )

        self._lookup_direction = lookup_direction

    @property
    def path(self):
        """Gets the path of this DependencyAttribute.  # noqa: E501

        Trace in source project model where the reference was found.  # noqa: E501

        :return: The path of this DependencyAttribute.  # noqa: E501
        :rtype: list[DependencyEntityReference]
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DependencyAttribute.

        Trace in source project model where the reference was found.  # noqa: E501

        :param path: The path of this DependencyAttribute.  # noqa: E501
        :type: list[DependencyEntityReference]
        """

        self._path = path

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
        if issubclass(DependencyAttribute, dict):
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
        if not isinstance(other, DependencyAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
