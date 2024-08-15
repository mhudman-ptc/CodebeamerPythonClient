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

class ReportResult(object):
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
        'cb_ql': 'str',
        'columns': 'list[ReportColumn]',
        'data': 'ReportGroup',
        'paging_information': 'ReportPagingInformation',
        'report': 'ReportReference',
        'show_all_children': 'bool'
    }

    attribute_map = {
        'cb_ql': 'cbQL',
        'columns': 'columns',
        'data': 'data',
        'paging_information': 'pagingInformation',
        'report': 'report',
        'show_all_children': 'showAllChildren'
    }

    def __init__(self, cb_ql=None, columns=None, data=None, paging_information=None, report=None, show_all_children=None):  # noqa: E501
        """ReportResult - a model defined in Swagger"""  # noqa: E501
        self._cb_ql = None
        self._columns = None
        self._data = None
        self._paging_information = None
        self._report = None
        self._show_all_children = None
        self.discriminator = None
        if cb_ql is not None:
            self.cb_ql = cb_ql
        if columns is not None:
            self.columns = columns
        if data is not None:
            self.data = data
        if paging_information is not None:
            self.paging_information = paging_information
        if report is not None:
            self.report = report
        if show_all_children is not None:
            self.show_all_children = show_all_children

    @property
    def cb_ql(self):
        """Gets the cb_ql of this ReportResult.  # noqa: E501

        CbQL query behind the report  # noqa: E501

        :return: The cb_ql of this ReportResult.  # noqa: E501
        :rtype: str
        """
        return self._cb_ql

    @cb_ql.setter
    def cb_ql(self, cb_ql):
        """Sets the cb_ql of this ReportResult.

        CbQL query behind the report  # noqa: E501

        :param cb_ql: The cb_ql of this ReportResult.  # noqa: E501
        :type: str
        """

        self._cb_ql = cb_ql

    @property
    def columns(self):
        """Gets the columns of this ReportResult.  # noqa: E501

        Column information  # noqa: E501

        :return: The columns of this ReportResult.  # noqa: E501
        :rtype: list[ReportColumn]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this ReportResult.

        Column information  # noqa: E501

        :param columns: The columns of this ReportResult.  # noqa: E501
        :type: list[ReportColumn]
        """

        self._columns = columns

    @property
    def data(self):
        """Gets the data of this ReportResult.  # noqa: E501


        :return: The data of this ReportResult.  # noqa: E501
        :rtype: ReportGroup
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ReportResult.


        :param data: The data of this ReportResult.  # noqa: E501
        :type: ReportGroup
        """

        self._data = data

    @property
    def paging_information(self):
        """Gets the paging_information of this ReportResult.  # noqa: E501


        :return: The paging_information of this ReportResult.  # noqa: E501
        :rtype: ReportPagingInformation
        """
        return self._paging_information

    @paging_information.setter
    def paging_information(self, paging_information):
        """Sets the paging_information of this ReportResult.


        :param paging_information: The paging_information of this ReportResult.  # noqa: E501
        :type: ReportPagingInformation
        """

        self._paging_information = paging_information

    @property
    def report(self):
        """Gets the report of this ReportResult.  # noqa: E501


        :return: The report of this ReportResult.  # noqa: E501
        :rtype: ReportReference
        """
        return self._report

    @report.setter
    def report(self, report):
        """Sets the report of this ReportResult.


        :param report: The report of this ReportResult.  # noqa: E501
        :type: ReportReference
        """

        self._report = report

    @property
    def show_all_children(self):
        """Gets the show_all_children of this ReportResult.  # noqa: E501

        Indicator to ability to collapse/expand all child items.  # noqa: E501

        :return: The show_all_children of this ReportResult.  # noqa: E501
        :rtype: bool
        """
        return self._show_all_children

    @show_all_children.setter
    def show_all_children(self, show_all_children):
        """Sets the show_all_children of this ReportResult.

        Indicator to ability to collapse/expand all child items.  # noqa: E501

        :param show_all_children: The show_all_children of this ReportResult.  # noqa: E501
        :type: bool
        """

        self._show_all_children = show_all_children

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
        if issubclass(ReportResult, dict):
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
        if not isinstance(other, ReportResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
