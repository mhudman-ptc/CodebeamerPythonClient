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

class TrackerFieldComputedFieldReference(object):
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
        'referred_field_id': 'int',
        'referred_field_tracker_id': 'int',
        'referred_tracker_id': 'int'
    }

    attribute_map = {
        'referred_field_id': 'referredFieldId',
        'referred_field_tracker_id': 'referredFieldTrackerId',
        'referred_tracker_id': 'referredTrackerId'
    }

    def __init__(self, referred_field_id=None, referred_field_tracker_id=None, referred_tracker_id=None):  # noqa: E501
        """TrackerFieldComputedFieldReference - a model defined in Swagger"""  # noqa: E501
        self._referred_field_id = None
        self._referred_field_tracker_id = None
        self._referred_tracker_id = None
        self.discriminator = None
        if referred_field_id is not None:
            self.referred_field_id = referred_field_id
        if referred_field_tracker_id is not None:
            self.referred_field_tracker_id = referred_field_tracker_id
        if referred_tracker_id is not None:
            self.referred_tracker_id = referred_tracker_id

    @property
    def referred_field_id(self):
        """Gets the referred_field_id of this TrackerFieldComputedFieldReference.  # noqa: E501


        :return: The referred_field_id of this TrackerFieldComputedFieldReference.  # noqa: E501
        :rtype: int
        """
        return self._referred_field_id

    @referred_field_id.setter
    def referred_field_id(self, referred_field_id):
        """Sets the referred_field_id of this TrackerFieldComputedFieldReference.


        :param referred_field_id: The referred_field_id of this TrackerFieldComputedFieldReference.  # noqa: E501
        :type: int
        """

        self._referred_field_id = referred_field_id

    @property
    def referred_field_tracker_id(self):
        """Gets the referred_field_tracker_id of this TrackerFieldComputedFieldReference.  # noqa: E501


        :return: The referred_field_tracker_id of this TrackerFieldComputedFieldReference.  # noqa: E501
        :rtype: int
        """
        return self._referred_field_tracker_id

    @referred_field_tracker_id.setter
    def referred_field_tracker_id(self, referred_field_tracker_id):
        """Sets the referred_field_tracker_id of this TrackerFieldComputedFieldReference.


        :param referred_field_tracker_id: The referred_field_tracker_id of this TrackerFieldComputedFieldReference.  # noqa: E501
        :type: int
        """

        self._referred_field_tracker_id = referred_field_tracker_id

    @property
    def referred_tracker_id(self):
        """Gets the referred_tracker_id of this TrackerFieldComputedFieldReference.  # noqa: E501


        :return: The referred_tracker_id of this TrackerFieldComputedFieldReference.  # noqa: E501
        :rtype: int
        """
        return self._referred_tracker_id

    @referred_tracker_id.setter
    def referred_tracker_id(self, referred_tracker_id):
        """Sets the referred_tracker_id of this TrackerFieldComputedFieldReference.


        :param referred_tracker_id: The referred_tracker_id of this TrackerFieldComputedFieldReference.  # noqa: E501
        :type: int
        """

        self._referred_tracker_id = referred_tracker_id

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
        if issubclass(TrackerFieldComputedFieldReference, dict):
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
        if not isinstance(other, TrackerFieldComputedFieldReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
