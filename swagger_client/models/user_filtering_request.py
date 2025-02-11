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

class UserFilteringRequest(object):
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
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'name': 'str',
        'project_id': 'int',
        'user_status': 'str'
    }

    attribute_map = {
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'name': 'name',
        'project_id': 'projectId',
        'user_status': 'userStatus'
    }

    def __init__(self, email=None, first_name=None, last_name=None, name=None, project_id=None, user_status=None):  # noqa: E501
        """UserFilteringRequest - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._first_name = None
        self._last_name = None
        self._name = None
        self._project_id = None
        self._user_status = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if user_status is not None:
            self.user_status = user_status

    @property
    def email(self):
        """Gets the email of this UserFilteringRequest.  # noqa: E501

        Email of the user  # noqa: E501

        :return: The email of this UserFilteringRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserFilteringRequest.

        Email of the user  # noqa: E501

        :param email: The email of this UserFilteringRequest.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this UserFilteringRequest.  # noqa: E501

        First name of the user  # noqa: E501

        :return: The first_name of this UserFilteringRequest.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserFilteringRequest.

        First name of the user  # noqa: E501

        :param first_name: The first_name of this UserFilteringRequest.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserFilteringRequest.  # noqa: E501

        Last name of the user  # noqa: E501

        :return: The last_name of this UserFilteringRequest.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserFilteringRequest.

        Last name of the user  # noqa: E501

        :param last_name: The last_name of this UserFilteringRequest.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def name(self):
        """Gets the name of this UserFilteringRequest.  # noqa: E501

        Name of the user  # noqa: E501

        :return: The name of this UserFilteringRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserFilteringRequest.

        Name of the user  # noqa: E501

        :param name: The name of this UserFilteringRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this UserFilteringRequest.  # noqa: E501

        Id of the project where the user is a member  # noqa: E501

        :return: The project_id of this UserFilteringRequest.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UserFilteringRequest.

        Id of the project where the user is a member  # noqa: E501

        :param project_id: The project_id of this UserFilteringRequest.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def user_status(self):
        """Gets the user_status of this UserFilteringRequest.  # noqa: E501

        Status of the user  # noqa: E501

        :return: The user_status of this UserFilteringRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_status

    @user_status.setter
    def user_status(self, user_status):
        """Sets the user_status of this UserFilteringRequest.

        Status of the user  # noqa: E501

        :param user_status: The user_status of this UserFilteringRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVATED", "DISABLED", "INACTIVATION"]  # noqa: E501
        if user_status not in allowed_values:
            raise ValueError(
                "Invalid value for `user_status` ({0}), must be one of {1}"  # noqa: E501
                .format(user_status, allowed_values)
            )

        self._user_status = user_status

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
        if issubclass(UserFilteringRequest, dict):
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
        if not isinstance(other, UserFilteringRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
