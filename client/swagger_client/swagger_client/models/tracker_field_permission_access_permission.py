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

class TrackerFieldPermissionAccessPermission(object):
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
        'access': 'str',
        'subject_id': 'int',
        'subject_type': 'str'
    }

    attribute_map = {
        'access': 'access',
        'subject_id': 'subjectId',
        'subject_type': 'subjectType'
    }

    def __init__(self, access=None, subject_id=None, subject_type=None):  # noqa: E501
        """TrackerFieldPermissionAccessPermission - a model defined in Swagger"""  # noqa: E501
        self._access = None
        self._subject_id = None
        self._subject_type = None
        self.discriminator = None
        if access is not None:
            self.access = access
        if subject_id is not None:
            self.subject_id = subject_id
        if subject_type is not None:
            self.subject_type = subject_type

    @property
    def access(self):
        """Gets the access of this TrackerFieldPermissionAccessPermission.  # noqa: E501

        The level of the access.  # noqa: E501

        :return: The access of this TrackerFieldPermissionAccessPermission.  # noqa: E501
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this TrackerFieldPermissionAccessPermission.

        The level of the access.  # noqa: E501

        :param access: The access of this TrackerFieldPermissionAccessPermission.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "READ", "READ_WRITE"]  # noqa: E501
        if access not in allowed_values:
            raise ValueError(
                "Invalid value for `access` ({0}), must be one of {1}"  # noqa: E501
                .format(access, allowed_values)
            )

        self._access = access

    @property
    def subject_id(self):
        """Gets the subject_id of this TrackerFieldPermissionAccessPermission.  # noqa: E501


        :return: The subject_id of this TrackerFieldPermissionAccessPermission.  # noqa: E501
        :rtype: int
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        """Sets the subject_id of this TrackerFieldPermissionAccessPermission.


        :param subject_id: The subject_id of this TrackerFieldPermissionAccessPermission.  # noqa: E501
        :type: int
        """

        self._subject_id = subject_id

    @property
    def subject_type(self):
        """Gets the subject_type of this TrackerFieldPermissionAccessPermission.  # noqa: E501

        The type of the subject of the permission.  # noqa: E501

        :return: The subject_type of this TrackerFieldPermissionAccessPermission.  # noqa: E501
        :rtype: str
        """
        return self._subject_type

    @subject_type.setter
    def subject_type(self, subject_type):
        """Sets the subject_type of this TrackerFieldPermissionAccessPermission.

        The type of the subject of the permission.  # noqa: E501

        :param subject_type: The subject_type of this TrackerFieldPermissionAccessPermission.  # noqa: E501
        :type: str
        """
        allowed_values = ["FIELD", "ROLE"]  # noqa: E501
        if subject_type not in allowed_values:
            raise ValueError(
                "Invalid value for `subject_type` ({0}), must be one of {1}"  # noqa: E501
                .format(subject_type, allowed_values)
            )

        self._subject_type = subject_type

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
        if issubclass(TrackerFieldPermissionAccessPermission, dict):
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
        if not isinstance(other, TrackerFieldPermissionAccessPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
