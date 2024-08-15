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

class TrackerItemField(object):
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
        'editable_fields': 'list[AbstractFieldValue]',
        'editable_table_fields': 'list[TableFieldValue]',
        'read_only_fields': 'list[AbstractFieldValue]',
        'read_only_table_fields': 'list[TableFieldValue]'
    }

    attribute_map = {
        'editable_fields': 'editableFields',
        'editable_table_fields': 'editableTableFields',
        'read_only_fields': 'readOnlyFields',
        'read_only_table_fields': 'readOnlyTableFields'
    }

    def __init__(self, editable_fields=None, editable_table_fields=None, read_only_fields=None, read_only_table_fields=None):  # noqa: E501
        """TrackerItemField - a model defined in Swagger"""  # noqa: E501
        self._editable_fields = None
        self._editable_table_fields = None
        self._read_only_fields = None
        self._read_only_table_fields = None
        self.discriminator = None
        if editable_fields is not None:
            self.editable_fields = editable_fields
        if editable_table_fields is not None:
            self.editable_table_fields = editable_table_fields
        if read_only_fields is not None:
            self.read_only_fields = read_only_fields
        if read_only_table_fields is not None:
            self.read_only_table_fields = read_only_table_fields

    @property
    def editable_fields(self):
        """Gets the editable_fields of this TrackerItemField.  # noqa: E501

        Fields which can be modified  # noqa: E501

        :return: The editable_fields of this TrackerItemField.  # noqa: E501
        :rtype: list[AbstractFieldValue]
        """
        return self._editable_fields

    @editable_fields.setter
    def editable_fields(self, editable_fields):
        """Sets the editable_fields of this TrackerItemField.

        Fields which can be modified  # noqa: E501

        :param editable_fields: The editable_fields of this TrackerItemField.  # noqa: E501
        :type: list[AbstractFieldValue]
        """

        self._editable_fields = editable_fields

    @property
    def editable_table_fields(self):
        """Gets the editable_table_fields of this TrackerItemField.  # noqa: E501

        Table fields which can be modified  # noqa: E501

        :return: The editable_table_fields of this TrackerItemField.  # noqa: E501
        :rtype: list[TableFieldValue]
        """
        return self._editable_table_fields

    @editable_table_fields.setter
    def editable_table_fields(self, editable_table_fields):
        """Sets the editable_table_fields of this TrackerItemField.

        Table fields which can be modified  # noqa: E501

        :param editable_table_fields: The editable_table_fields of this TrackerItemField.  # noqa: E501
        :type: list[TableFieldValue]
        """

        self._editable_table_fields = editable_table_fields

    @property
    def read_only_fields(self):
        """Gets the read_only_fields of this TrackerItemField.  # noqa: E501

        Fields which are not writable in the current state  # noqa: E501

        :return: The read_only_fields of this TrackerItemField.  # noqa: E501
        :rtype: list[AbstractFieldValue]
        """
        return self._read_only_fields

    @read_only_fields.setter
    def read_only_fields(self, read_only_fields):
        """Sets the read_only_fields of this TrackerItemField.

        Fields which are not writable in the current state  # noqa: E501

        :param read_only_fields: The read_only_fields of this TrackerItemField.  # noqa: E501
        :type: list[AbstractFieldValue]
        """

        self._read_only_fields = read_only_fields

    @property
    def read_only_table_fields(self):
        """Gets the read_only_table_fields of this TrackerItemField.  # noqa: E501

        Table fields which are not writable in the current state  # noqa: E501

        :return: The read_only_table_fields of this TrackerItemField.  # noqa: E501
        :rtype: list[TableFieldValue]
        """
        return self._read_only_table_fields

    @read_only_table_fields.setter
    def read_only_table_fields(self, read_only_table_fields):
        """Sets the read_only_table_fields of this TrackerItemField.

        Table fields which are not writable in the current state  # noqa: E501

        :param read_only_table_fields: The read_only_table_fields of this TrackerItemField.  # noqa: E501
        :type: list[TableFieldValue]
        """

        self._read_only_table_fields = read_only_table_fields

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
        if issubclass(TrackerItemField, dict):
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
        if not isinstance(other, TrackerItemField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other