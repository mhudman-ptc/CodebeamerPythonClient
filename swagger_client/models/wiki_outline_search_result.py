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

class WikiOutlineSearchResult(object):
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
        'outline_wiki_pages': 'list[OutlineWiki]',
        'page': 'int',
        'page_size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'outline_wiki_pages': 'outlineWikiPages',
        'page': 'page',
        'page_size': 'pageSize',
        'total': 'total'
    }

    def __init__(self, outline_wiki_pages=None, page=None, page_size=None, total=None):  # noqa: E501
        """WikiOutlineSearchResult - a model defined in Swagger"""  # noqa: E501
        self._outline_wiki_pages = None
        self._page = None
        self._page_size = None
        self._total = None
        self.discriminator = None
        if outline_wiki_pages is not None:
            self.outline_wiki_pages = outline_wiki_pages
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if total is not None:
            self.total = total

    @property
    def outline_wiki_pages(self):
        """Gets the outline_wiki_pages of this WikiOutlineSearchResult.  # noqa: E501

        Found outline wiki pages  # noqa: E501

        :return: The outline_wiki_pages of this WikiOutlineSearchResult.  # noqa: E501
        :rtype: list[OutlineWiki]
        """
        return self._outline_wiki_pages

    @outline_wiki_pages.setter
    def outline_wiki_pages(self, outline_wiki_pages):
        """Sets the outline_wiki_pages of this WikiOutlineSearchResult.

        Found outline wiki pages  # noqa: E501

        :param outline_wiki_pages: The outline_wiki_pages of this WikiOutlineSearchResult.  # noqa: E501
        :type: list[OutlineWiki]
        """

        self._outline_wiki_pages = outline_wiki_pages

    @property
    def page(self):
        """Gets the page of this WikiOutlineSearchResult.  # noqa: E501

        Index of the page  # noqa: E501

        :return: The page of this WikiOutlineSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this WikiOutlineSearchResult.

        Index of the page  # noqa: E501

        :param page: The page of this WikiOutlineSearchResult.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this WikiOutlineSearchResult.  # noqa: E501

        Size of the found page  # noqa: E501

        :return: The page_size of this WikiOutlineSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this WikiOutlineSearchResult.

        Size of the found page  # noqa: E501

        :param page_size: The page_size of this WikiOutlineSearchResult.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def total(self):
        """Gets the total of this WikiOutlineSearchResult.  # noqa: E501

        Number of matched tracker items by the search criteria  # noqa: E501

        :return: The total of this WikiOutlineSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this WikiOutlineSearchResult.

        Number of matched tracker items by the search criteria  # noqa: E501

        :param total: The total of this WikiOutlineSearchResult.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(WikiOutlineSearchResult, dict):
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
        if not isinstance(other, WikiOutlineSearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
