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

class WorkflowTransition(object):
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
        'description': 'str',
        'description_format': 'str',
        'from_status': 'ChoiceOptionReference',
        'hidden': 'bool',
        'id': 'int',
        'name': 'str',
        'permissions': 'list[AccessPermission]',
        'to_status': 'ChoiceOptionReference'
    }

    attribute_map = {
        'description': 'description',
        'description_format': 'descriptionFormat',
        'from_status': 'fromStatus',
        'hidden': 'hidden',
        'id': 'id',
        'name': 'name',
        'permissions': 'permissions',
        'to_status': 'toStatus'
    }

    def __init__(self, description=None, description_format=None, from_status=None, hidden=None, id=None, name=None, permissions=None, to_status=None):  # noqa: E501
        """WorkflowTransition - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._description_format = None
        self._from_status = None
        self._hidden = None
        self._id = None
        self._name = None
        self._permissions = None
        self._to_status = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if description_format is not None:
            self.description_format = description_format
        if from_status is not None:
            self.from_status = from_status
        if hidden is not None:
            self.hidden = hidden
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if permissions is not None:
            self.permissions = permissions
        self.to_status = to_status

    @property
    def description(self):
        """Gets the description of this WorkflowTransition.  # noqa: E501

        Description of the entity  # noqa: E501

        :return: The description of this WorkflowTransition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkflowTransition.

        Description of the entity  # noqa: E501

        :param description: The description of this WorkflowTransition.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def description_format(self):
        """Gets the description_format of this WorkflowTransition.  # noqa: E501

        Description format of the entity  # noqa: E501

        :return: The description_format of this WorkflowTransition.  # noqa: E501
        :rtype: str
        """
        return self._description_format

    @description_format.setter
    def description_format(self, description_format):
        """Sets the description_format of this WorkflowTransition.

        Description format of the entity  # noqa: E501

        :param description_format: The description_format of this WorkflowTransition.  # noqa: E501
        :type: str
        """
        allowed_values = ["PlainText", "Html", "Wiki"]  # noqa: E501
        if description_format not in allowed_values:
            raise ValueError(
                "Invalid value for `description_format` ({0}), must be one of {1}"  # noqa: E501
                .format(description_format, allowed_values)
            )

        self._description_format = description_format

    @property
    def from_status(self):
        """Gets the from_status of this WorkflowTransition.  # noqa: E501


        :return: The from_status of this WorkflowTransition.  # noqa: E501
        :rtype: ChoiceOptionReference
        """
        return self._from_status

    @from_status.setter
    def from_status(self, from_status):
        """Sets the from_status of this WorkflowTransition.


        :param from_status: The from_status of this WorkflowTransition.  # noqa: E501
        :type: ChoiceOptionReference
        """

        self._from_status = from_status

    @property
    def hidden(self):
        """Gets the hidden of this WorkflowTransition.  # noqa: E501

        Indicator if the transition is hidden  # noqa: E501

        :return: The hidden of this WorkflowTransition.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this WorkflowTransition.

        Indicator if the transition is hidden  # noqa: E501

        :param hidden: The hidden of this WorkflowTransition.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def id(self):
        """Gets the id of this WorkflowTransition.  # noqa: E501

        Id of the entity  # noqa: E501

        :return: The id of this WorkflowTransition.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkflowTransition.

        Id of the entity  # noqa: E501

        :param id: The id of this WorkflowTransition.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this WorkflowTransition.  # noqa: E501

        Name of the entity  # noqa: E501

        :return: The name of this WorkflowTransition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowTransition.

        Name of the entity  # noqa: E501

        :param name: The name of this WorkflowTransition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def permissions(self):
        """Gets the permissions of this WorkflowTransition.  # noqa: E501

        Access permissions of the transition  # noqa: E501

        :return: The permissions of this WorkflowTransition.  # noqa: E501
        :rtype: list[AccessPermission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this WorkflowTransition.

        Access permissions of the transition  # noqa: E501

        :param permissions: The permissions of this WorkflowTransition.  # noqa: E501
        :type: list[AccessPermission]
        """

        self._permissions = permissions

    @property
    def to_status(self):
        """Gets the to_status of this WorkflowTransition.  # noqa: E501


        :return: The to_status of this WorkflowTransition.  # noqa: E501
        :rtype: ChoiceOptionReference
        """
        return self._to_status

    @to_status.setter
    def to_status(self, to_status):
        """Sets the to_status of this WorkflowTransition.


        :param to_status: The to_status of this WorkflowTransition.  # noqa: E501
        :type: ChoiceOptionReference
        """
        if to_status is None:
            raise ValueError("Invalid value for `to_status`, must not be `None`")  # noqa: E501

        self._to_status = to_status

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
        if issubclass(WorkflowTransition, dict):
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
        if not isinstance(other, WorkflowTransition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other