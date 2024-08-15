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

class Project(object):
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
        'category': 'str',
        'closed': 'bool',
        'created_at': 'datetime',
        'created_by': 'UserReference',
        'deleted': 'bool',
        'description': 'str',
        'description_format': 'str',
        'id': 'int',
        'key_name': 'str',
        'modified_at': 'datetime',
        'modified_by': 'UserReference',
        'name': 'str',
        'template': 'bool',
        'version': 'int'
    }

    attribute_map = {
        'category': 'category',
        'closed': 'closed',
        'created_at': 'createdAt',
        'created_by': 'createdBy',
        'deleted': 'deleted',
        'description': 'description',
        'description_format': 'descriptionFormat',
        'id': 'id',
        'key_name': 'keyName',
        'modified_at': 'modifiedAt',
        'modified_by': 'modifiedBy',
        'name': 'name',
        'template': 'template',
        'version': 'version'
    }

    def __init__(self, category=None, closed=None, created_at=None, created_by=None, deleted=None, description=None, description_format=None, id=None, key_name=None, modified_at=None, modified_by=None, name=None, template=None, version=None):  # noqa: E501
        """Project - a model defined in Swagger"""  # noqa: E501
        self._category = None
        self._closed = None
        self._created_at = None
        self._created_by = None
        self._deleted = None
        self._description = None
        self._description_format = None
        self._id = None
        self._key_name = None
        self._modified_at = None
        self._modified_by = None
        self._name = None
        self._template = None
        self._version = None
        self.discriminator = None
        if category is not None:
            self.category = category
        if closed is not None:
            self.closed = closed
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if deleted is not None:
            self.deleted = deleted
        if description is not None:
            self.description = description
        if description_format is not None:
            self.description_format = description_format
        if id is not None:
            self.id = id
        if key_name is not None:
            self.key_name = key_name
        if modified_at is not None:
            self.modified_at = modified_at
        if modified_by is not None:
            self.modified_by = modified_by
        if name is not None:
            self.name = name
        if template is not None:
            self.template = template
        if version is not None:
            self.version = version

    @property
    def category(self):
        """Gets the category of this Project.  # noqa: E501

        Category of a project  # noqa: E501

        :return: The category of this Project.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Project.

        Category of a project  # noqa: E501

        :param category: The category of this Project.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def closed(self):
        """Gets the closed of this Project.  # noqa: E501

        Closed status of a project  # noqa: E501

        :return: The closed of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """Sets the closed of this Project.

        Closed status of a project  # noqa: E501

        :param closed: The closed of this Project.  # noqa: E501
        :type: bool
        """

        self._closed = closed

    @property
    def created_at(self):
        """Gets the created_at of this Project.  # noqa: E501

        The date when the entity was created  # noqa: E501

        :return: The created_at of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Project.

        The date when the entity was created  # noqa: E501

        :param created_at: The created_at of this Project.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Project.  # noqa: E501


        :return: The created_by of this Project.  # noqa: E501
        :rtype: UserReference
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Project.


        :param created_by: The created_by of this Project.  # noqa: E501
        :type: UserReference
        """

        self._created_by = created_by

    @property
    def deleted(self):
        """Gets the deleted of this Project.  # noqa: E501

        Delete status of a project  # noqa: E501

        :return: The deleted of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Project.

        Delete status of a project  # noqa: E501

        :param deleted: The deleted of this Project.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def description(self):
        """Gets the description of this Project.  # noqa: E501

        Description of the entity  # noqa: E501

        :return: The description of this Project.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Project.

        Description of the entity  # noqa: E501

        :param description: The description of this Project.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def description_format(self):
        """Gets the description_format of this Project.  # noqa: E501

        Description format of the entity  # noqa: E501

        :return: The description_format of this Project.  # noqa: E501
        :rtype: str
        """
        return self._description_format

    @description_format.setter
    def description_format(self, description_format):
        """Sets the description_format of this Project.

        Description format of the entity  # noqa: E501

        :param description_format: The description_format of this Project.  # noqa: E501
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
    def id(self):
        """Gets the id of this Project.  # noqa: E501

        Id of the entity  # noqa: E501

        :return: The id of this Project.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.

        Id of the entity  # noqa: E501

        :param id: The id of this Project.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def key_name(self):
        """Gets the key_name of this Project.  # noqa: E501

        Key name of a project  # noqa: E501

        :return: The key_name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this Project.

        Key name of a project  # noqa: E501

        :param key_name: The key_name of this Project.  # noqa: E501
        :type: str
        """

        self._key_name = key_name

    @property
    def modified_at(self):
        """Gets the modified_at of this Project.  # noqa: E501

        The date when the entity was modified  # noqa: E501

        :return: The modified_at of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this Project.

        The date when the entity was modified  # noqa: E501

        :param modified_at: The modified_at of this Project.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def modified_by(self):
        """Gets the modified_by of this Project.  # noqa: E501


        :return: The modified_by of this Project.  # noqa: E501
        :rtype: UserReference
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this Project.


        :param modified_by: The modified_by of this Project.  # noqa: E501
        :type: UserReference
        """

        self._modified_by = modified_by

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501

        Name of the entity  # noqa: E501

        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.

        Name of the entity  # noqa: E501

        :param name: The name of this Project.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def template(self):
        """Gets the template of this Project.  # noqa: E501

        Template status of a project  # noqa: E501

        :return: The template of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this Project.

        Template status of a project  # noqa: E501

        :param template: The template of this Project.  # noqa: E501
        :type: bool
        """

        self._template = template

    @property
    def version(self):
        """Gets the version of this Project.  # noqa: E501

        Version of a project  # noqa: E501

        :return: The version of this Project.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Project.

        Version of a project  # noqa: E501

        :param version: The version of this Project.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if issubclass(Project, dict):
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
        if not isinstance(other, Project):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
