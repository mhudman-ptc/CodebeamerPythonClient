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

class StatusLayout(object):
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
        'layout': 'str',
        'status': 'str'
    }

    attribute_map = {
        'layout': 'layout',
        'status': 'status'
    }

    def __init__(self, layout=None, status=None):  # noqa: E501
        """StatusLayout - a model defined in Swagger"""  # noqa: E501
        self._layout = None
        self._status = None
        self.discriminator = None
        if layout is not None:
            self.layout = layout
        if status is not None:
            self.status = status

    @property
    def layout(self):
        """Gets the layout of this StatusLayout.  # noqa: E501

        layout of a statusLayout  # noqa: E501

        :return: The layout of this StatusLayout.  # noqa: E501
        :rtype: str
        """
        return self._layout

    @layout.setter
    def layout(self, layout):
        """Sets the layout of this StatusLayout.

        layout of a statusLayout  # noqa: E501

        :param layout: The layout of this StatusLayout.  # noqa: E501
        :type: str
        """

        self._layout = layout

    @property
    def status(self):
        """Gets the status of this StatusLayout.  # noqa: E501

        status of a statusLayout  # noqa: E501

        :return: The status of this StatusLayout.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StatusLayout.

        status of a statusLayout  # noqa: E501

        :param status: The status of this StatusLayout.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(StatusLayout, dict):
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
        if not isinstance(other, StatusLayout):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
