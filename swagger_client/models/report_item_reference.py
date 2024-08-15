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

class ReportItemReference(object):
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
        'item_id': 'int',
        'tracker_id': 'int'
    }

    attribute_map = {
        'item_id': 'itemId',
        'tracker_id': 'trackerId'
    }

    def __init__(self, item_id=None, tracker_id=None):  # noqa: E501
        """ReportItemReference - a model defined in Swagger"""  # noqa: E501
        self._item_id = None
        self._tracker_id = None
        self.discriminator = None
        if item_id is not None:
            self.item_id = item_id
        if tracker_id is not None:
            self.tracker_id = tracker_id

    @property
    def item_id(self):
        """Gets the item_id of this ReportItemReference.  # noqa: E501

        Identifier of the underlying item.  # noqa: E501

        :return: The item_id of this ReportItemReference.  # noqa: E501
        :rtype: int
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this ReportItemReference.

        Identifier of the underlying item.  # noqa: E501

        :param item_id: The item_id of this ReportItemReference.  # noqa: E501
        :type: int
        """

        self._item_id = item_id

    @property
    def tracker_id(self):
        """Gets the tracker_id of this ReportItemReference.  # noqa: E501

        Identifier of the tracker of the underlying item.  # noqa: E501

        :return: The tracker_id of this ReportItemReference.  # noqa: E501
        :rtype: int
        """
        return self._tracker_id

    @tracker_id.setter
    def tracker_id(self, tracker_id):
        """Sets the tracker_id of this ReportItemReference.

        Identifier of the tracker of the underlying item.  # noqa: E501

        :param tracker_id: The tracker_id of this ReportItemReference.  # noqa: E501
        :type: int
        """

        self._tracker_id = tracker_id

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
        if issubclass(ReportItemReference, dict):
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
        if not isinstance(other, ReportItemReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
