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

class TrackerItemFieldMappingPair(object):
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
        'source_field': 'TrackerItemFieldMapping',
        'target_field': 'TrackerItemFieldMapping'
    }

    attribute_map = {
        'source_field': 'sourceField',
        'target_field': 'targetField'
    }

    def __init__(self, source_field=None, target_field=None):  # noqa: E501
        """TrackerItemFieldMappingPair - a model defined in Swagger"""  # noqa: E501
        self._source_field = None
        self._target_field = None
        self.discriminator = None
        self.source_field = source_field
        if target_field is not None:
            self.target_field = target_field

    @property
    def source_field(self):
        """Gets the source_field of this TrackerItemFieldMappingPair.  # noqa: E501


        :return: The source_field of this TrackerItemFieldMappingPair.  # noqa: E501
        :rtype: TrackerItemFieldMapping
        """
        return self._source_field

    @source_field.setter
    def source_field(self, source_field):
        """Sets the source_field of this TrackerItemFieldMappingPair.


        :param source_field: The source_field of this TrackerItemFieldMappingPair.  # noqa: E501
        :type: TrackerItemFieldMapping
        """
        if source_field is None:
            raise ValueError("Invalid value for `source_field`, must not be `None`")  # noqa: E501

        self._source_field = source_field

    @property
    def target_field(self):
        """Gets the target_field of this TrackerItemFieldMappingPair.  # noqa: E501


        :return: The target_field of this TrackerItemFieldMappingPair.  # noqa: E501
        :rtype: TrackerItemFieldMapping
        """
        return self._target_field

    @target_field.setter
    def target_field(self, target_field):
        """Sets the target_field of this TrackerItemFieldMappingPair.


        :param target_field: The target_field of this TrackerItemFieldMappingPair.  # noqa: E501
        :type: TrackerItemFieldMapping
        """

        self._target_field = target_field

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
        if issubclass(TrackerItemFieldMappingPair, dict):
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
        if not isinstance(other, TrackerItemFieldMappingPair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
