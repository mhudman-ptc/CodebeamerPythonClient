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

class ReportPagingInformation(object):
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
        'page': 'int',
        'page_count': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'page': 'page',
        'page_count': 'pageCount',
        'page_size': 'pageSize'
    }

    def __init__(self, page=None, page_count=None, page_size=None):  # noqa: E501
        """ReportPagingInformation - a model defined in Swagger"""  # noqa: E501
        self._page = None
        self._page_count = None
        self._page_size = None
        self.discriminator = None
        if page is not None:
            self.page = page
        if page_count is not None:
            self.page_count = page_count
        if page_size is not None:
            self.page_size = page_size

    @property
    def page(self):
        """Gets the page of this ReportPagingInformation.  # noqa: E501

        Index of the page  # noqa: E501

        :return: The page of this ReportPagingInformation.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ReportPagingInformation.

        Index of the page  # noqa: E501

        :param page: The page of this ReportPagingInformation.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_count(self):
        """Gets the page_count of this ReportPagingInformation.  # noqa: E501

        Number of pages in the report  # noqa: E501

        :return: The page_count of this ReportPagingInformation.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this ReportPagingInformation.

        Number of pages in the report  # noqa: E501

        :param page_count: The page_count of this ReportPagingInformation.  # noqa: E501
        :type: int
        """

        self._page_count = page_count

    @property
    def page_size(self):
        """Gets the page_size of this ReportPagingInformation.  # noqa: E501

        Size of the found page  # noqa: E501

        :return: The page_size of this ReportPagingInformation.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ReportPagingInformation.

        Size of the found page  # noqa: E501

        :param page_size: The page_size of this ReportPagingInformation.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

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
        if issubclass(ReportPagingInformation, dict):
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
        if not isinstance(other, ReportPagingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
