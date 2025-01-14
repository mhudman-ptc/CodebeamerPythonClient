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
from swagger_client.models.abstract_outline import AbstractOutline  # noqa: F401,E501

class OutlineItem(AbstractOutline):
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
        'has_children': 'bool',
        'item_reference': 'TrackerItemReference'
    }
    if hasattr(AbstractOutline, "swagger_types"):
        swagger_types.update(AbstractOutline.swagger_types)

    attribute_map = {
        'has_children': 'hasChildren',
        'item_reference': 'itemReference'
    }
    if hasattr(AbstractOutline, "attribute_map"):
        attribute_map.update(AbstractOutline.attribute_map)

    def __init__(self, has_children=None, item_reference=None, *args, **kwargs):  # noqa: E501
        """OutlineItem - a model defined in Swagger"""  # noqa: E501
        self._has_children = None
        self._item_reference = None
        self.discriminator = None
        if has_children is not None:
            self.has_children = has_children
        if item_reference is not None:
            self.item_reference = item_reference
        AbstractOutline.__init__(self, *args, **kwargs)

    @property
    def has_children(self):
        """Gets the has_children of this OutlineItem.  # noqa: E501

        Indicator if the item has child items.  # noqa: E501

        :return: The has_children of this OutlineItem.  # noqa: E501
        :rtype: bool
        """
        return self._has_children

    @has_children.setter
    def has_children(self, has_children):
        """Sets the has_children of this OutlineItem.

        Indicator if the item has child items.  # noqa: E501

        :param has_children: The has_children of this OutlineItem.  # noqa: E501
        :type: bool
        """

        self._has_children = has_children

    @property
    def item_reference(self):
        """Gets the item_reference of this OutlineItem.  # noqa: E501


        :return: The item_reference of this OutlineItem.  # noqa: E501
        :rtype: TrackerItemReference
        """
        return self._item_reference

    @item_reference.setter
    def item_reference(self, item_reference):
        """Sets the item_reference of this OutlineItem.


        :param item_reference: The item_reference of this OutlineItem.  # noqa: E501
        :type: TrackerItemReference
        """

        self._item_reference = item_reference

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
        if issubclass(OutlineItem, dict):
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
        if not isinstance(other, OutlineItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
