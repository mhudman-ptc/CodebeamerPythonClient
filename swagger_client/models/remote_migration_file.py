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

class RemoteMigrationFile(object):
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
        'file_name': 'str',
        'file_path': 'str',
        'md5sum': 'str',
        'sha512sum': 'str'
    }

    attribute_map = {
        'file_name': 'fileName',
        'file_path': 'filePath',
        'md5sum': 'md5sum',
        'sha512sum': 'sha512sum'
    }

    def __init__(self, file_name=None, file_path=None, md5sum=None, sha512sum=None):  # noqa: E501
        """RemoteMigrationFile - a model defined in Swagger"""  # noqa: E501
        self._file_name = None
        self._file_path = None
        self._md5sum = None
        self._sha512sum = None
        self.discriminator = None
        if file_name is not None:
            self.file_name = file_name
        if file_path is not None:
            self.file_path = file_path
        if md5sum is not None:
            self.md5sum = md5sum
        if sha512sum is not None:
            self.sha512sum = sha512sum

    @property
    def file_name(self):
        """Gets the file_name of this RemoteMigrationFile.  # noqa: E501

        File name of the newly created attachment.  # noqa: E501

        :return: The file_name of this RemoteMigrationFile.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this RemoteMigrationFile.

        File name of the newly created attachment.  # noqa: E501

        :param file_name: The file_name of this RemoteMigrationFile.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def file_path(self):
        """Gets the file_path of this RemoteMigrationFile.  # noqa: E501

        The path of the file relative to the configured migration home directory.  # noqa: E501

        :return: The file_path of this RemoteMigrationFile.  # noqa: E501
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this RemoteMigrationFile.

        The path of the file relative to the configured migration home directory.  # noqa: E501

        :param file_path: The file_path of this RemoteMigrationFile.  # noqa: E501
        :type: str
        """

        self._file_path = file_path

    @property
    def md5sum(self):
        """Gets the md5sum of this RemoteMigrationFile.  # noqa: E501

        Precomputed MD5 checksum of the file.  # noqa: E501

        :return: The md5sum of this RemoteMigrationFile.  # noqa: E501
        :rtype: str
        """
        return self._md5sum

    @md5sum.setter
    def md5sum(self, md5sum):
        """Sets the md5sum of this RemoteMigrationFile.

        Precomputed MD5 checksum of the file.  # noqa: E501

        :param md5sum: The md5sum of this RemoteMigrationFile.  # noqa: E501
        :type: str
        """

        self._md5sum = md5sum

    @property
    def sha512sum(self):
        """Gets the sha512sum of this RemoteMigrationFile.  # noqa: E501

        Precomputed SHA512 checksum of the file.  # noqa: E501

        :return: The sha512sum of this RemoteMigrationFile.  # noqa: E501
        :rtype: str
        """
        return self._sha512sum

    @sha512sum.setter
    def sha512sum(self, sha512sum):
        """Sets the sha512sum of this RemoteMigrationFile.

        Precomputed SHA512 checksum of the file.  # noqa: E501

        :param sha512sum: The sha512sum of this RemoteMigrationFile.  # noqa: E501
        :type: str
        """

        self._sha512sum = sha512sum

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
        if issubclass(RemoteMigrationFile, dict):
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
        if not isinstance(other, RemoteMigrationFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
