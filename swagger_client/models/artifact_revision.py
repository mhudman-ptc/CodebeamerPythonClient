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

class ArtifactRevision(object):
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
        'change_summary': 'str',
        'id': 'int',
        'modified_at': 'datetime',
        'modified_by': 'UserReference',
        'version': 'int'
    }

    attribute_map = {
        'change_summary': 'changeSummary',
        'id': 'id',
        'modified_at': 'modifiedAt',
        'modified_by': 'modifiedBy',
        'version': 'version'
    }

    def __init__(self, change_summary=None, id=None, modified_at=None, modified_by=None, version=None):  # noqa: E501
        """ArtifactRevision - a model defined in Swagger"""  # noqa: E501
        self._change_summary = None
        self._id = None
        self._modified_at = None
        self._modified_by = None
        self._version = None
        self.discriminator = None
        if change_summary is not None:
            self.change_summary = change_summary
        if id is not None:
            self.id = id
        if modified_at is not None:
            self.modified_at = modified_at
        if modified_by is not None:
            self.modified_by = modified_by
        if version is not None:
            self.version = version

    @property
    def change_summary(self):
        """Gets the change_summary of this ArtifactRevision.  # noqa: E501

        Summary of the change  # noqa: E501

        :return: The change_summary of this ArtifactRevision.  # noqa: E501
        :rtype: str
        """
        return self._change_summary

    @change_summary.setter
    def change_summary(self, change_summary):
        """Sets the change_summary of this ArtifactRevision.

        Summary of the change  # noqa: E501

        :param change_summary: The change_summary of this ArtifactRevision.  # noqa: E501
        :type: str
        """

        self._change_summary = change_summary

    @property
    def id(self):
        """Gets the id of this ArtifactRevision.  # noqa: E501

        Id of the entity  # noqa: E501

        :return: The id of this ArtifactRevision.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ArtifactRevision.

        Id of the entity  # noqa: E501

        :param id: The id of this ArtifactRevision.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def modified_at(self):
        """Gets the modified_at of this ArtifactRevision.  # noqa: E501

        The date when the entity was modified  # noqa: E501

        :return: The modified_at of this ArtifactRevision.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this ArtifactRevision.

        The date when the entity was modified  # noqa: E501

        :param modified_at: The modified_at of this ArtifactRevision.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def modified_by(self):
        """Gets the modified_by of this ArtifactRevision.  # noqa: E501


        :return: The modified_by of this ArtifactRevision.  # noqa: E501
        :rtype: UserReference
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this ArtifactRevision.


        :param modified_by: The modified_by of this ArtifactRevision.  # noqa: E501
        :type: UserReference
        """

        self._modified_by = modified_by

    @property
    def version(self):
        """Gets the version of this ArtifactRevision.  # noqa: E501

        Version of the artifact  # noqa: E501

        :return: The version of this ArtifactRevision.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ArtifactRevision.

        Version of the artifact  # noqa: E501

        :param version: The version of this ArtifactRevision.  # noqa: E501
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
        if issubclass(ArtifactRevision, dict):
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
        if not isinstance(other, ArtifactRevision):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
