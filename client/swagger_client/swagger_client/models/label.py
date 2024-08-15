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

class Label(object):
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
        'created_at': 'datetime',
        'created_by': 'UserReference',
        'hidden': 'bool',
        'id': 'int',
        'name': 'str',
        'private_label': 'bool'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'created_by': 'createdBy',
        'hidden': 'hidden',
        'id': 'id',
        'name': 'name',
        'private_label': 'privateLabel'
    }

    def __init__(self, created_at=None, created_by=None, hidden=None, id=None, name=None, private_label=None):  # noqa: E501
        """Label - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._created_by = None
        self._hidden = None
        self._id = None
        self._name = None
        self._private_label = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if hidden is not None:
            self.hidden = hidden
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if private_label is not None:
            self.private_label = private_label

    @property
    def created_at(self):
        """Gets the created_at of this Label.  # noqa: E501

        The date when the entity was created  # noqa: E501

        :return: The created_at of this Label.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Label.

        The date when the entity was created  # noqa: E501

        :param created_at: The created_at of this Label.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Label.  # noqa: E501


        :return: The created_by of this Label.  # noqa: E501
        :rtype: UserReference
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Label.


        :param created_by: The created_by of this Label.  # noqa: E501
        :type: UserReference
        """

        self._created_by = created_by

    @property
    def hidden(self):
        """Gets the hidden of this Label.  # noqa: E501

        Whether the label is hidden or not  # noqa: E501

        :return: The hidden of this Label.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this Label.

        Whether the label is hidden or not  # noqa: E501

        :param hidden: The hidden of this Label.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def id(self):
        """Gets the id of this Label.  # noqa: E501

        Id of the entity  # noqa: E501

        :return: The id of this Label.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Label.

        Id of the entity  # noqa: E501

        :param id: The id of this Label.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Label.  # noqa: E501

        Name of the entity  # noqa: E501

        :return: The name of this Label.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Label.

        Name of the entity  # noqa: E501

        :param name: The name of this Label.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def private_label(self):
        """Gets the private_label of this Label.  # noqa: E501

        Whether the label is private or not  # noqa: E501

        :return: The private_label of this Label.  # noqa: E501
        :rtype: bool
        """
        return self._private_label

    @private_label.setter
    def private_label(self, private_label):
        """Sets the private_label of this Label.

        Whether the label is private or not  # noqa: E501

        :param private_label: The private_label of this Label.  # noqa: E501
        :type: bool
        """

        self._private_label = private_label

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
        if issubclass(Label, dict):
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
        if not isinstance(other, Label):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
