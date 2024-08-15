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

class AbstractReference(object):
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
        'id': 'int',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type'
    }

    discriminator_value_class_map = {
          'ProjectBaselineReference': 'ProjectBaselineReference',
'UserReference': 'UserReference',
'WikiPageReference': 'WikiPageReference',
'ProjectRoleReference': 'ProjectRoleReference',
'BranchReference': 'BranchReference',
'UserGroupReference': 'UserGroupReference',
'RoleReference': 'RoleReference',
'TrackerItemReference': 'TrackerItemReference',
'CommentReference': 'CommentReference',
'TrackerReference': 'TrackerReference',
'ChoiceOptionReference': 'ChoiceOptionReference',
'AttachmentReference': 'AttachmentReference',
'AssociationTypeReference': 'AssociationTypeReference',
'DependencyEntityReference': 'DependencyEntityReference',
'TrackerBaselineReference': 'TrackerBaselineReference',
'FieldReference': 'FieldReference',
'TrackerTypeReference': 'TrackerTypeReference',
'RepositoryReference': 'RepositoryReference',
'ArtifactReference': 'ArtifactReference',
'ProjectReference': 'ProjectReference',
'WorkingSetReference': 'WorkingSetReference',
'SharedFieldReference': 'SharedFieldReference',
'TrackerPermissionReference': 'TrackerPermissionReference',
'ReportReference': 'ReportReference'    }

    def __init__(self, id=None, name=None, type=None):  # noqa: E501
        """AbstractReference - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._type = None
        self.discriminator = 'type'
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this AbstractReference.  # noqa: E501

        Id of the entity  # noqa: E501

        :return: The id of this AbstractReference.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AbstractReference.

        Id of the entity  # noqa: E501

        :param id: The id of this AbstractReference.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AbstractReference.  # noqa: E501

        Name of the entity  # noqa: E501

        :return: The name of this AbstractReference.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AbstractReference.

        Name of the entity  # noqa: E501

        :param name: The name of this AbstractReference.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this AbstractReference.  # noqa: E501

        Type of a referenced object  # noqa: E501

        :return: The type of this AbstractReference.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AbstractReference.

        Type of a referenced object  # noqa: E501

        :param type: The type of this AbstractReference.  # noqa: E501
        :type: str
        """

        self._type = type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(AbstractReference, dict):
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
        if not isinstance(other, AbstractReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
