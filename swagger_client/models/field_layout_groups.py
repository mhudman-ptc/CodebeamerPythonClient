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

class FieldLayoutGroups(object):
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
        'collapsed': 'bool',
        'color': 'str',
        'default': 'bool',
        'fields': 'list[LayoutField]',
        'name': 'str'
    }

    attribute_map = {
        'collapsed': 'collapsed',
        'color': 'color',
        'default': 'default',
        'fields': 'fields',
        'name': 'name'
    }

    def __init__(self, collapsed=None, color=None, default=None, fields=None, name=None):  # noqa: E501
        """FieldLayoutGroups - a model defined in Swagger"""  # noqa: E501
        self._collapsed = None
        self._color = None
        self._default = None
        self._fields = None
        self._name = None
        self.discriminator = None
        if collapsed is not None:
            self.collapsed = collapsed
        if color is not None:
            self.color = color
        if default is not None:
            self.default = default
        if fields is not None:
            self.fields = fields
        if name is not None:
            self.name = name

    @property
    def collapsed(self):
        """Gets the collapsed of this FieldLayoutGroups.  # noqa: E501

        collapsed of a groupsModel  # noqa: E501

        :return: The collapsed of this FieldLayoutGroups.  # noqa: E501
        :rtype: bool
        """
        return self._collapsed

    @collapsed.setter
    def collapsed(self, collapsed):
        """Sets the collapsed of this FieldLayoutGroups.

        collapsed of a groupsModel  # noqa: E501

        :param collapsed: The collapsed of this FieldLayoutGroups.  # noqa: E501
        :type: bool
        """

        self._collapsed = collapsed

    @property
    def color(self):
        """Gets the color of this FieldLayoutGroups.  # noqa: E501

        color of a groupsModel  # noqa: E501

        :return: The color of this FieldLayoutGroups.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this FieldLayoutGroups.

        color of a groupsModel  # noqa: E501

        :param color: The color of this FieldLayoutGroups.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def default(self):
        """Gets the default of this FieldLayoutGroups.  # noqa: E501

        default of a groupsModel  # noqa: E501

        :return: The default of this FieldLayoutGroups.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this FieldLayoutGroups.

        default of a groupsModel  # noqa: E501

        :param default: The default of this FieldLayoutGroups.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def fields(self):
        """Gets the fields of this FieldLayoutGroups.  # noqa: E501

        fieldModel of a groupsModel  # noqa: E501

        :return: The fields of this FieldLayoutGroups.  # noqa: E501
        :rtype: list[LayoutField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this FieldLayoutGroups.

        fieldModel of a groupsModel  # noqa: E501

        :param fields: The fields of this FieldLayoutGroups.  # noqa: E501
        :type: list[LayoutField]
        """

        self._fields = fields

    @property
    def name(self):
        """Gets the name of this FieldLayoutGroups.  # noqa: E501

        name of a groupsModel  # noqa: E501

        :return: The name of this FieldLayoutGroups.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FieldLayoutGroups.

        name of a groupsModel  # noqa: E501

        :param name: The name of this FieldLayoutGroups.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(FieldLayoutGroups, dict):
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
        if not isinstance(other, FieldLayoutGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other