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

class ReportPermission(object):
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
        'project': 'ProjectReference',
        'role': 'RoleReference'
    }

    attribute_map = {
        'access': 'access',
        'project': 'project',
        'role': 'role'
    }

    def __init__(self, access=None, project=None, role=None):  # noqa: E501
        """ReportPermission - a model defined in Swagger"""  # noqa: E501
        self._access = None
        self._project = None
        self._role = None
        self.discriminator = None
        self.access = access
        self.project = project
        self.role = role

    @property
    def access(self):
        """Gets the access of this ReportPermission.  # noqa: E501

        Access level  # noqa: E501

        :return: The access of this ReportPermission.  # noqa: E501
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this ReportPermission.

        Access level  # noqa: E501

        :param access: The access of this ReportPermission.  # noqa: E501
        :type: str
        """
        if access is None:
            raise ValueError("Invalid value for `access`, must not be `None`")  # noqa: E501
        allowed_values = ["NONE", "READ", "WRITE", "READ_WRITE"]  # noqa: E501
        if access not in allowed_values:
            raise ValueError(
                "Invalid value for `access` ({0}), must be one of {1}"  # noqa: E501
                .format(access, allowed_values)
            )

        self._access = access

    @property
    def project(self):
        """Gets the project of this ReportPermission.  # noqa: E501


        :return: The project of this ReportPermission.  # noqa: E501
        :rtype: ProjectReference
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ReportPermission.


        :param project: The project of this ReportPermission.  # noqa: E501
        :type: ProjectReference
        """
        if project is None:
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def role(self):
        """Gets the role of this ReportPermission.  # noqa: E501


        :return: The role of this ReportPermission.  # noqa: E501
        :rtype: RoleReference
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ReportPermission.


        :param role: The role of this ReportPermission.  # noqa: E501
        :type: RoleReference
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

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
        if issubclass(ReportPermission, dict):
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
        if not isinstance(other, ReportPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
