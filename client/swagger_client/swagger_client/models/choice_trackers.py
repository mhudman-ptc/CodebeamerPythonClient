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
from swagger_client.models.base_tracker_field_choice_option import BaseTrackerFieldChoiceOption  # noqa: F401,E501

class ChoiceTrackers(BaseTrackerFieldChoiceOption):
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
        'reference_filters': 'list[ReferenceFilterBasedChoiceReferenceFilter]'
    }
    if hasattr(BaseTrackerFieldChoiceOption, "swagger_types"):
        swagger_types.update(BaseTrackerFieldChoiceOption.swagger_types)

    attribute_map = {
        'reference_filters': 'referenceFilters'
    }
    if hasattr(BaseTrackerFieldChoiceOption, "attribute_map"):
        attribute_map.update(BaseTrackerFieldChoiceOption.attribute_map)

    def __init__(self, reference_filters=None, *args, **kwargs):  # noqa: E501
        """ChoiceTrackers - a model defined in Swagger"""  # noqa: E501
        self._reference_filters = None
        self.discriminator = None
        if reference_filters is not None:
            self.reference_filters = reference_filters
        BaseTrackerFieldChoiceOption.__init__(self, *args, **kwargs)

    @property
    def reference_filters(self):
        """Gets the reference_filters of this ChoiceTrackers.  # noqa: E501


        :return: The reference_filters of this ChoiceTrackers.  # noqa: E501
        :rtype: list[ReferenceFilterBasedChoiceReferenceFilter]
        """
        return self._reference_filters

    @reference_filters.setter
    def reference_filters(self, reference_filters):
        """Sets the reference_filters of this ChoiceTrackers.


        :param reference_filters: The reference_filters of this ChoiceTrackers.  # noqa: E501
        :type: list[ReferenceFilterBasedChoiceReferenceFilter]
        """

        self._reference_filters = reference_filters

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
        if issubclass(ChoiceTrackers, dict):
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
        if not isinstance(other, ChoiceTrackers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
