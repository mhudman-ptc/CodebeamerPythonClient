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

class RestException(object):
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
        'message': 'str',
        'resource_uri': 'str'
    }

    attribute_map = {
        'message': 'message',
        'resource_uri': 'resourceUri'
    }

    def __init__(self, message=None, resource_uri=None):  # noqa: E501
        """RestException - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._resource_uri = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if resource_uri is not None:
            self.resource_uri = resource_uri

    @property
    def message(self):
        """Gets the message of this RestException.  # noqa: E501


        :return: The message of this RestException.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this RestException.


        :param message: The message of this RestException.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def resource_uri(self):
        """Gets the resource_uri of this RestException.  # noqa: E501


        :return: The resource_uri of this RestException.  # noqa: E501
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """Sets the resource_uri of this RestException.


        :param resource_uri: The resource_uri of this RestException.  # noqa: E501
        :type: str
        """

        self._resource_uri = resource_uri

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
        if issubclass(RestException, dict):
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
        if not isinstance(other, RestException):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
