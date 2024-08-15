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

class UpdateAttachment(object):
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
        'content': 'str',
        'description': 'str',
        'description_format': 'str'
    }

    attribute_map = {
        'content': 'content',
        'description': 'description',
        'description_format': 'descriptionFormat'
    }

    def __init__(self, content=None, description=None, description_format='PlainText'):  # noqa: E501
        """UpdateAttachment - a model defined in Swagger"""  # noqa: E501
        self._content = None
        self._description = None
        self._description_format = None
        self.discriminator = None
        if content is not None:
            self.content = content
        if description is not None:
            self.description = description
        if description_format is not None:
            self.description_format = description_format

    @property
    def content(self):
        """Gets the content of this UpdateAttachment.  # noqa: E501


        :return: The content of this UpdateAttachment.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this UpdateAttachment.


        :param content: The content of this UpdateAttachment.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def description(self):
        """Gets the description of this UpdateAttachment.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this UpdateAttachment.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateAttachment.

        Description  # noqa: E501

        :param description: The description of this UpdateAttachment.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def description_format(self):
        """Gets the description_format of this UpdateAttachment.  # noqa: E501

        Format of description  # noqa: E501

        :return: The description_format of this UpdateAttachment.  # noqa: E501
        :rtype: str
        """
        return self._description_format

    @description_format.setter
    def description_format(self, description_format):
        """Sets the description_format of this UpdateAttachment.

        Format of description  # noqa: E501

        :param description_format: The description_format of this UpdateAttachment.  # noqa: E501
        :type: str
        """
        allowed_values = ["PlainText", "Html", "Wiki"]  # noqa: E501
        if description_format not in allowed_values:
            raise ValueError(
                "Invalid value for `description_format` ({0}), must be one of {1}"  # noqa: E501
                .format(description_format, allowed_values)
            )

        self._description_format = description_format

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
        if issubclass(UpdateAttachment, dict):
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
        if not isinstance(other, UpdateAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
