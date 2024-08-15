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

class TrackerFieldStatusPermissions(object):
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
        'permissions': 'list[AccessPermission]',
        'status': 'ChoiceOptionReference'
    }

    attribute_map = {
        'permissions': 'permissions',
        'status': 'status'
    }

    def __init__(self, permissions=None, status=None):  # noqa: E501
        """TrackerFieldStatusPermissions - a model defined in Swagger"""  # noqa: E501
        self._permissions = None
        self._status = None
        self.discriminator = None
        if permissions is not None:
            self.permissions = permissions
        if status is not None:
            self.status = status

    @property
    def permissions(self):
        """Gets the permissions of this TrackerFieldStatusPermissions.  # noqa: E501

        Access permissions by role  # noqa: E501

        :return: The permissions of this TrackerFieldStatusPermissions.  # noqa: E501
        :rtype: list[AccessPermission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this TrackerFieldStatusPermissions.

        Access permissions by role  # noqa: E501

        :param permissions: The permissions of this TrackerFieldStatusPermissions.  # noqa: E501
        :type: list[AccessPermission]
        """

        self._permissions = permissions

    @property
    def status(self):
        """Gets the status of this TrackerFieldStatusPermissions.  # noqa: E501


        :return: The status of this TrackerFieldStatusPermissions.  # noqa: E501
        :rtype: ChoiceOptionReference
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TrackerFieldStatusPermissions.


        :param status: The status of this TrackerFieldStatusPermissions.  # noqa: E501
        :type: ChoiceOptionReference
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
        if issubclass(TrackerFieldStatusPermissions, dict):
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
        if not isinstance(other, TrackerFieldStatusPermissions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
