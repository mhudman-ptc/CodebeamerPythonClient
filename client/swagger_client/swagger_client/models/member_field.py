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

class MemberField(AbstractField):
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
        'member_types': 'list[str]',
        'multiple_values': 'bool'
    }
    if hasattr(AbstractField, "swagger_types"):
        swagger_types.update(AbstractField.swagger_types)

    attribute_map = {
        'member_types': 'memberTypes',
        'multiple_values': 'multipleValues'
    }
    if hasattr(AbstractField, "attribute_map"):
        attribute_map.update(AbstractField.attribute_map)

    def __init__(self, member_types=None, multiple_values=None, *args, **kwargs):  # noqa: E501
        """MemberField - a model defined in Swagger"""  # noqa: E501
        self._member_types = None
        self._multiple_values = None
        self.discriminator = None
        if member_types is not None:
            self.member_types = member_types
        if multiple_values is not None:
            self.multiple_values = multiple_values
        AbstractField.__init__(self, *args, **kwargs)

    @property
    def member_types(self):
        """Gets the member_types of this MemberField.  # noqa: E501

        Supported member type of a member field  # noqa: E501

        :return: The member_types of this MemberField.  # noqa: E501
        :rtype: list[str]
        """
        return self._member_types

    @member_types.setter
    def member_types(self, member_types):
        """Sets the member_types of this MemberField.

        Supported member type of a member field  # noqa: E501

        :param member_types: The member_types of this MemberField.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["USER", "ROLE", "GROUP"]  # noqa: E501
        if not set(member_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `member_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(member_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._member_types = member_types

    @property
    def multiple_values(self):
        """Gets the multiple_values of this MemberField.  # noqa: E501

        Multiple values state of a field  # noqa: E501

        :return: The multiple_values of this MemberField.  # noqa: E501
        :rtype: bool
        """
        return self._multiple_values

    @multiple_values.setter
    def multiple_values(self, multiple_values):
        """Sets the multiple_values of this MemberField.

        Multiple values state of a field  # noqa: E501

        :param multiple_values: The multiple_values of this MemberField.  # noqa: E501
        :type: bool
        """

        self._multiple_values = multiple_values

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
        if issubclass(MemberField, dict):
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
        if not isinstance(other, MemberField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
