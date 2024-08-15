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
from swagger_client.models.report_group import ReportGroup  # noqa: F401,E501

class ReportGroupWithReferencedRows(ReportGroup):
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
        'grouping_level': 'int',
        'rows': 'list[ReportReferencedRow]',
        'star_row': 'int'
    }
    if hasattr(ReportGroup, "swagger_types"):
        swagger_types.update(ReportGroup.swagger_types)

    attribute_map = {
        'grouping_level': 'groupingLevel',
        'rows': 'rows',
        'star_row': 'starRow'
    }
    if hasattr(ReportGroup, "attribute_map"):
        attribute_map.update(ReportGroup.attribute_map)

    def __init__(self, grouping_level=None, rows=None, star_row=None, *args, **kwargs):  # noqa: E501
        """ReportGroupWithReferencedRows - a model defined in Swagger"""  # noqa: E501
        self._grouping_level = None
        self._rows = None
        self._star_row = None
        self.discriminator = None
        if grouping_level is not None:
            self.grouping_level = grouping_level
        if rows is not None:
            self.rows = rows
        if star_row is not None:
            self.star_row = star_row
        ReportGroup.__init__(self, *args, **kwargs)

    @property
    def grouping_level(self):
        """Gets the grouping_level of this ReportGroupWithReferencedRows.  # noqa: E501


        :return: The grouping_level of this ReportGroupWithReferencedRows.  # noqa: E501
        :rtype: int
        """
        return self._grouping_level

    @grouping_level.setter
    def grouping_level(self, grouping_level):
        """Sets the grouping_level of this ReportGroupWithReferencedRows.


        :param grouping_level: The grouping_level of this ReportGroupWithReferencedRows.  # noqa: E501
        :type: int
        """

        self._grouping_level = grouping_level

    @property
    def rows(self):
        """Gets the rows of this ReportGroupWithReferencedRows.  # noqa: E501


        :return: The rows of this ReportGroupWithReferencedRows.  # noqa: E501
        :rtype: list[ReportReferencedRow]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this ReportGroupWithReferencedRows.


        :param rows: The rows of this ReportGroupWithReferencedRows.  # noqa: E501
        :type: list[ReportReferencedRow]
        """

        self._rows = rows

    @property
    def star_row(self):
        """Gets the star_row of this ReportGroupWithReferencedRows.  # noqa: E501


        :return: The star_row of this ReportGroupWithReferencedRows.  # noqa: E501
        :rtype: int
        """
        return self._star_row

    @star_row.setter
    def star_row(self, star_row):
        """Sets the star_row of this ReportGroupWithReferencedRows.


        :param star_row: The star_row of this ReportGroupWithReferencedRows.  # noqa: E501
        :type: int
        """

        self._star_row = star_row

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
        if issubclass(ReportGroupWithReferencedRows, dict):
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
        if not isinstance(other, ReportGroupWithReferencedRows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other