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

class TrackerItemChildReference(object):
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
        'item_reference': 'TrackerItemReference'
    }

    attribute_map = {
        'index': 'index',
        'item_reference': 'itemReference'
    }

    def __init__(self, index=None, item_reference=None):  # noqa: E501
        """TrackerItemChildReference - a model defined in Swagger"""  # noqa: E501
        self._index = None
        self._item_reference = None
        self.discriminator = None
        self.index = index
        self.item_reference = item_reference

    @property
    def index(self):
        """Gets the index of this TrackerItemChildReference.  # noqa: E501

        Ordinal in the tracker outline.  # noqa: E501

        :return: The index of this TrackerItemChildReference.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this TrackerItemChildReference.

        Ordinal in the tracker outline.  # noqa: E501

        :param index: The index of this TrackerItemChildReference.  # noqa: E501
        :type: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def item_reference(self):
        """Gets the item_reference of this TrackerItemChildReference.  # noqa: E501


        :return: The item_reference of this TrackerItemChildReference.  # noqa: E501
        :rtype: TrackerItemReference
        """
        return self._item_reference

    @item_reference.setter
    def item_reference(self, item_reference):
        """Sets the item_reference of this TrackerItemChildReference.


        :param item_reference: The item_reference of this TrackerItemChildReference.  # noqa: E501
        :type: TrackerItemReference
        """
        if item_reference is None:
            raise ValueError("Invalid value for `item_reference`, must not be `None`")  # noqa: E501

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
        if issubclass(TrackerItemChildReference, dict):
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
        if not isinstance(other, TrackerItemChildReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
