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

class TrackerConfiguration(object):
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
        'basic_information': 'TrackerBasicInformation',
        'fields': 'list[TrackerField]'
    }

    attribute_map = {
        'basic_information': 'basicInformation',
        'fields': 'fields'
    }

    def __init__(self, basic_information=None, fields=None):  # noqa: E501
        """TrackerConfiguration - a model defined in Swagger"""  # noqa: E501
        self._basic_information = None
        self._fields = None
        self.discriminator = None
        if basic_information is not None:
            self.basic_information = basic_information
        if fields is not None:
            self.fields = fields

    @property
    def basic_information(self):
        """Gets the basic_information of this TrackerConfiguration.  # noqa: E501


        :return: The basic_information of this TrackerConfiguration.  # noqa: E501
        :rtype: TrackerBasicInformation
        """
        return self._basic_information

    @basic_information.setter
    def basic_information(self, basic_information):
        """Sets the basic_information of this TrackerConfiguration.


        :param basic_information: The basic_information of this TrackerConfiguration.  # noqa: E501
        :type: TrackerBasicInformation
        """

        self._basic_information = basic_information

    @property
    def fields(self):
        """Gets the fields of this TrackerConfiguration.  # noqa: E501


        :return: The fields of this TrackerConfiguration.  # noqa: E501
        :rtype: list[TrackerField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this TrackerConfiguration.


        :param fields: The fields of this TrackerConfiguration.  # noqa: E501
        :type: list[TrackerField]
        """

        self._fields = fields

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
        if issubclass(TrackerConfiguration, dict):
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
        if not isinstance(other, TrackerConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other