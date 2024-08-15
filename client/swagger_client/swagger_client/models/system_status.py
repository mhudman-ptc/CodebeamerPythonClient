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

class SystemStatus(object):
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
        'system_mode': 'str'
    }

    attribute_map = {
        'system_mode': 'systemMode'
    }

    def __init__(self, system_mode=None):  # noqa: E501
        """SystemStatus - a model defined in Swagger"""  # noqa: E501
        self._system_mode = None
        self.discriminator = None
        if system_mode is not None:
            self.system_mode = system_mode

    @property
    def system_mode(self):
        """Gets the system_mode of this SystemStatus.  # noqa: E501

        System mode  # noqa: E501

        :return: The system_mode of this SystemStatus.  # noqa: E501
        :rtype: str
        """
        return self._system_mode

    @system_mode.setter
    def system_mode(self, system_mode):
        """Sets the system_mode of this SystemStatus.

        System mode  # noqa: E501

        :param system_mode: The system_mode of this SystemStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["NORMAL", "MAINTENANCE"]  # noqa: E501
        if system_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `system_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(system_mode, allowed_values)
            )

        self._system_mode = system_mode

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
        if issubclass(SystemStatus, dict):
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
        if not isinstance(other, SystemStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
