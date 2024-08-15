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
from swagger_client.models.abstract_tracker_item_change import AbstractTrackerItemChange  # noqa: F401,E501

class TrackerItemRowChange(AbstractTrackerItemChange):
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
        'row_number': 'int'
    }
    if hasattr(AbstractTrackerItemChange, "swagger_types"):
        swagger_types.update(AbstractTrackerItemChange.swagger_types)

    attribute_map = {
        'row_number': 'rowNumber'
    }
    if hasattr(AbstractTrackerItemChange, "attribute_map"):
        attribute_map.update(AbstractTrackerItemChange.attribute_map)

    def __init__(self, row_number=None, *args, **kwargs):  # noqa: E501
        """TrackerItemRowChange - a model defined in Swagger"""  # noqa: E501
        self._row_number = None
        self.discriminator = None
        if row_number is not None:
            self.row_number = row_number
        AbstractTrackerItemChange.__init__(self, *args, **kwargs)

    @property
    def row_number(self):
        """Gets the row_number of this TrackerItemRowChange.  # noqa: E501

        Index of the changed row  # noqa: E501

        :return: The row_number of this TrackerItemRowChange.  # noqa: E501
        :rtype: int
        """
        return self._row_number

    @row_number.setter
    def row_number(self, row_number):
        """Sets the row_number of this TrackerItemRowChange.

        Index of the changed row  # noqa: E501

        :param row_number: The row_number of this TrackerItemRowChange.  # noqa: E501
        :type: int
        """

        self._row_number = row_number

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
        if issubclass(TrackerItemRowChange, dict):
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
        if not isinstance(other, TrackerItemRowChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
