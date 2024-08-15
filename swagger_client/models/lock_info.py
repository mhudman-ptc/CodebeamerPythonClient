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

class LockInfo(object):
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
        'expires': 'bool',
        'user': 'UserReference'
    }

    attribute_map = {
        'expires': 'expires',
        'user': 'user'
    }

    def __init__(self, expires=None, user=None):  # noqa: E501
        """LockInfo - a model defined in Swagger"""  # noqa: E501
        self._expires = None
        self._user = None
        self.discriminator = None
        if expires is not None:
            self.expires = expires
        if user is not None:
            self.user = user

    @property
    def expires(self):
        """Gets the expires of this LockInfo.  # noqa: E501

        Whether the lock will expire on its own, eg. if it is a soft lock  # noqa: E501

        :return: The expires of this LockInfo.  # noqa: E501
        :rtype: bool
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this LockInfo.

        Whether the lock will expire on its own, eg. if it is a soft lock  # noqa: E501

        :param expires: The expires of this LockInfo.  # noqa: E501
        :type: bool
        """

        self._expires = expires

    @property
    def user(self):
        """Gets the user of this LockInfo.  # noqa: E501


        :return: The user of this LockInfo.  # noqa: E501
        :rtype: UserReference
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this LockInfo.


        :param user: The user of this LockInfo.  # noqa: E501
        :type: UserReference
        """

        self._user = user

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
        if issubclass(LockInfo, dict):
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
        if not isinstance(other, LockInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other