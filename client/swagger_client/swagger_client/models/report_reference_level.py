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

class ReportReferenceLevel(object):
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
        'columns': 'list[ReportColumn]',
        'downstream_reference_rows': 'list[ReportReferencedRow]',
        'reference_level': 'int',
        'upstream_reference_rows': 'list[ReportReferencedRow]'
    }

    attribute_map = {
        'columns': 'columns',
        'downstream_reference_rows': 'downstreamReferenceRows',
        'reference_level': 'referenceLevel',
        'upstream_reference_rows': 'upstreamReferenceRows'
    }

    def __init__(self, columns=None, downstream_reference_rows=None, reference_level=None, upstream_reference_rows=None):  # noqa: E501
        """ReportReferenceLevel - a model defined in Swagger"""  # noqa: E501
        self._columns = None
        self._downstream_reference_rows = None
        self._reference_level = None
        self._upstream_reference_rows = None
        self.discriminator = None
        if columns is not None:
            self.columns = columns
        if downstream_reference_rows is not None:
            self.downstream_reference_rows = downstream_reference_rows
        if reference_level is not None:
            self.reference_level = reference_level
        if upstream_reference_rows is not None:
            self.upstream_reference_rows = upstream_reference_rows

    @property
    def columns(self):
        """Gets the columns of this ReportReferenceLevel.  # noqa: E501

        Columns to show on this reference level.  # noqa: E501

        :return: The columns of this ReportReferenceLevel.  # noqa: E501
        :rtype: list[ReportColumn]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this ReportReferenceLevel.

        Columns to show on this reference level.  # noqa: E501

        :param columns: The columns of this ReportReferenceLevel.  # noqa: E501
        :type: list[ReportColumn]
        """

        self._columns = columns

    @property
    def downstream_reference_rows(self):
        """Gets the downstream_reference_rows of this ReportReferenceLevel.  # noqa: E501

        Downstream reference results.  # noqa: E501

        :return: The downstream_reference_rows of this ReportReferenceLevel.  # noqa: E501
        :rtype: list[ReportReferencedRow]
        """
        return self._downstream_reference_rows

    @downstream_reference_rows.setter
    def downstream_reference_rows(self, downstream_reference_rows):
        """Sets the downstream_reference_rows of this ReportReferenceLevel.

        Downstream reference results.  # noqa: E501

        :param downstream_reference_rows: The downstream_reference_rows of this ReportReferenceLevel.  # noqa: E501
        :type: list[ReportReferencedRow]
        """

        self._downstream_reference_rows = downstream_reference_rows

    @property
    def reference_level(self):
        """Gets the reference_level of this ReportReferenceLevel.  # noqa: E501

        Reference level.  # noqa: E501

        :return: The reference_level of this ReportReferenceLevel.  # noqa: E501
        :rtype: int
        """
        return self._reference_level

    @reference_level.setter
    def reference_level(self, reference_level):
        """Sets the reference_level of this ReportReferenceLevel.

        Reference level.  # noqa: E501

        :param reference_level: The reference_level of this ReportReferenceLevel.  # noqa: E501
        :type: int
        """

        self._reference_level = reference_level

    @property
    def upstream_reference_rows(self):
        """Gets the upstream_reference_rows of this ReportReferenceLevel.  # noqa: E501

        Upstream reference results.  # noqa: E501

        :return: The upstream_reference_rows of this ReportReferenceLevel.  # noqa: E501
        :rtype: list[ReportReferencedRow]
        """
        return self._upstream_reference_rows

    @upstream_reference_rows.setter
    def upstream_reference_rows(self, upstream_reference_rows):
        """Sets the upstream_reference_rows of this ReportReferenceLevel.

        Upstream reference results.  # noqa: E501

        :param upstream_reference_rows: The upstream_reference_rows of this ReportReferenceLevel.  # noqa: E501
        :type: list[ReportReferencedRow]
        """

        self._upstream_reference_rows = upstream_reference_rows

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
        if issubclass(ReportReferenceLevel, dict):
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
        if not isinstance(other, ReportReferenceLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
