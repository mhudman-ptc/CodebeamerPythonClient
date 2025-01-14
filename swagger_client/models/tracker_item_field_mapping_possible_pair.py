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

class TrackerItemFieldMappingPossiblePair(object):
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
        'possible_target_fields': 'list[TrackerItemFieldMapping]',
        'source_field': 'TrackerItemFieldMapping'
    }

    attribute_map = {
        'possible_target_fields': 'possibleTargetFields',
        'source_field': 'sourceField'
    }

    def __init__(self, possible_target_fields=None, source_field=None):  # noqa: E501
        """TrackerItemFieldMappingPossiblePair - a model defined in Swagger"""  # noqa: E501
        self._possible_target_fields = None
        self._source_field = None
        self.discriminator = None
        if possible_target_fields is not None:
            self.possible_target_fields = possible_target_fields
        if source_field is not None:
            self.source_field = source_field

    @property
    def possible_target_fields(self):
        """Gets the possible_target_fields of this TrackerItemFieldMappingPossiblePair.  # noqa: E501

        Possible Target Tracker field information  # noqa: E501

        :return: The possible_target_fields of this TrackerItemFieldMappingPossiblePair.  # noqa: E501
        :rtype: list[TrackerItemFieldMapping]
        """
        return self._possible_target_fields

    @possible_target_fields.setter
    def possible_target_fields(self, possible_target_fields):
        """Sets the possible_target_fields of this TrackerItemFieldMappingPossiblePair.

        Possible Target Tracker field information  # noqa: E501

        :param possible_target_fields: The possible_target_fields of this TrackerItemFieldMappingPossiblePair.  # noqa: E501
        :type: list[TrackerItemFieldMapping]
        """

        self._possible_target_fields = possible_target_fields

    @property
    def source_field(self):
        """Gets the source_field of this TrackerItemFieldMappingPossiblePair.  # noqa: E501


        :return: The source_field of this TrackerItemFieldMappingPossiblePair.  # noqa: E501
        :rtype: TrackerItemFieldMapping
        """
        return self._source_field

    @source_field.setter
    def source_field(self, source_field):
        """Sets the source_field of this TrackerItemFieldMappingPossiblePair.


        :param source_field: The source_field of this TrackerItemFieldMappingPossiblePair.  # noqa: E501
        :type: TrackerItemFieldMapping
        """

        self._source_field = source_field

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
        if issubclass(TrackerItemFieldMappingPossiblePair, dict):
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
        if not isinstance(other, TrackerItemFieldMappingPossiblePair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
