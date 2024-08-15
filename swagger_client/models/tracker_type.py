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

class TrackerType(object):
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
        'branchable': 'bool',
        'color': 'str',
        'doc_edit_view': 'bool',
        'editor_url': 'str',
        'id': 'int',
        'item_icon_url': 'str',
        'name': 'str',
        'outline': 'bool',
        'tracker_icon_url': 'str',
        'url_link_format': 'str',
        'var_name': 'str'
    }

    attribute_map = {
        'branchable': 'branchable',
        'color': 'color',
        'doc_edit_view': 'docEditView',
        'editor_url': 'editorUrl',
        'id': 'id',
        'item_icon_url': 'itemIconUrl',
        'name': 'name',
        'outline': 'outline',
        'tracker_icon_url': 'trackerIconUrl',
        'url_link_format': 'urlLinkFormat',
        'var_name': 'varName'
    }

    def __init__(self, branchable=None, color=None, doc_edit_view=None, editor_url=None, id=None, item_icon_url=None, name=None, outline=None, tracker_icon_url=None, url_link_format=None, var_name=None):  # noqa: E501
        """TrackerType - a model defined in Swagger"""  # noqa: E501
        self._branchable = None
        self._color = None
        self._doc_edit_view = None
        self._editor_url = None
        self._id = None
        self._item_icon_url = None
        self._name = None
        self._outline = None
        self._tracker_icon_url = None
        self._url_link_format = None
        self._var_name = None
        self.discriminator = None
        if branchable is not None:
            self.branchable = branchable
        if color is not None:
            self.color = color
        if doc_edit_view is not None:
            self.doc_edit_view = doc_edit_view
        if editor_url is not None:
            self.editor_url = editor_url
        if id is not None:
            self.id = id
        if item_icon_url is not None:
            self.item_icon_url = item_icon_url
        if name is not None:
            self.name = name
        if outline is not None:
            self.outline = outline
        if tracker_icon_url is not None:
            self.tracker_icon_url = tracker_icon_url
        if url_link_format is not None:
            self.url_link_format = url_link_format
        if var_name is not None:
            self.var_name = var_name

    @property
    def branchable(self):
        """Gets the branchable of this TrackerType.  # noqa: E501

        True if tracker type is branchable  # noqa: E501

        :return: The branchable of this TrackerType.  # noqa: E501
        :rtype: bool
        """
        return self._branchable

    @branchable.setter
    def branchable(self, branchable):
        """Sets the branchable of this TrackerType.

        True if tracker type is branchable  # noqa: E501

        :param branchable: The branchable of this TrackerType.  # noqa: E501
        :type: bool
        """

        self._branchable = branchable

    @property
    def color(self):
        """Gets the color of this TrackerType.  # noqa: E501

        Color of a tracker type  # noqa: E501

        :return: The color of this TrackerType.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this TrackerType.

        Color of a tracker type  # noqa: E501

        :param color: The color of this TrackerType.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def doc_edit_view(self):
        """Gets the doc_edit_view of this TrackerType.  # noqa: E501

        True if tracker type has document view  # noqa: E501

        :return: The doc_edit_view of this TrackerType.  # noqa: E501
        :rtype: bool
        """
        return self._doc_edit_view

    @doc_edit_view.setter
    def doc_edit_view(self, doc_edit_view):
        """Sets the doc_edit_view of this TrackerType.

        True if tracker type has document view  # noqa: E501

        :param doc_edit_view: The doc_edit_view of this TrackerType.  # noqa: E501
        :type: bool
        """

        self._doc_edit_view = doc_edit_view

    @property
    def editor_url(self):
        """Gets the editor_url of this TrackerType.  # noqa: E501

        Editor URL of a tracker type  # noqa: E501

        :return: The editor_url of this TrackerType.  # noqa: E501
        :rtype: str
        """
        return self._editor_url

    @editor_url.setter
    def editor_url(self, editor_url):
        """Sets the editor_url of this TrackerType.

        Editor URL of a tracker type  # noqa: E501

        :param editor_url: The editor_url of this TrackerType.  # noqa: E501
        :type: str
        """

        self._editor_url = editor_url

    @property
    def id(self):
        """Gets the id of this TrackerType.  # noqa: E501

        Id of the entity  # noqa: E501

        :return: The id of this TrackerType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrackerType.

        Id of the entity  # noqa: E501

        :param id: The id of this TrackerType.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def item_icon_url(self):
        """Gets the item_icon_url of this TrackerType.  # noqa: E501

        Item icon URL of a tracker type  # noqa: E501

        :return: The item_icon_url of this TrackerType.  # noqa: E501
        :rtype: str
        """
        return self._item_icon_url

    @item_icon_url.setter
    def item_icon_url(self, item_icon_url):
        """Sets the item_icon_url of this TrackerType.

        Item icon URL of a tracker type  # noqa: E501

        :param item_icon_url: The item_icon_url of this TrackerType.  # noqa: E501
        :type: str
        """

        self._item_icon_url = item_icon_url

    @property
    def name(self):
        """Gets the name of this TrackerType.  # noqa: E501

        Name of the entity  # noqa: E501

        :return: The name of this TrackerType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrackerType.

        Name of the entity  # noqa: E501

        :param name: The name of this TrackerType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def outline(self):
        """Gets the outline of this TrackerType.  # noqa: E501

        True if outline is enabled  # noqa: E501

        :return: The outline of this TrackerType.  # noqa: E501
        :rtype: bool
        """
        return self._outline

    @outline.setter
    def outline(self, outline):
        """Sets the outline of this TrackerType.

        True if outline is enabled  # noqa: E501

        :param outline: The outline of this TrackerType.  # noqa: E501
        :type: bool
        """

        self._outline = outline

    @property
    def tracker_icon_url(self):
        """Gets the tracker_icon_url of this TrackerType.  # noqa: E501

        Tracker icon URL of a tracker type  # noqa: E501

        :return: The tracker_icon_url of this TrackerType.  # noqa: E501
        :rtype: str
        """
        return self._tracker_icon_url

    @tracker_icon_url.setter
    def tracker_icon_url(self, tracker_icon_url):
        """Sets the tracker_icon_url of this TrackerType.

        Tracker icon URL of a tracker type  # noqa: E501

        :param tracker_icon_url: The tracker_icon_url of this TrackerType.  # noqa: E501
        :type: str
        """

        self._tracker_icon_url = tracker_icon_url

    @property
    def url_link_format(self):
        """Gets the url_link_format of this TrackerType.  # noqa: E501

        URL link format of a tracker type  # noqa: E501

        :return: The url_link_format of this TrackerType.  # noqa: E501
        :rtype: str
        """
        return self._url_link_format

    @url_link_format.setter
    def url_link_format(self, url_link_format):
        """Sets the url_link_format of this TrackerType.

        URL link format of a tracker type  # noqa: E501

        :param url_link_format: The url_link_format of this TrackerType.  # noqa: E501
        :type: str
        """

        self._url_link_format = url_link_format

    @property
    def var_name(self):
        """Gets the var_name of this TrackerType.  # noqa: E501

        Internal/variable name of a tracker type  # noqa: E501

        :return: The var_name of this TrackerType.  # noqa: E501
        :rtype: str
        """
        return self._var_name

    @var_name.setter
    def var_name(self, var_name):
        """Sets the var_name of this TrackerType.

        Internal/variable name of a tracker type  # noqa: E501

        :param var_name: The var_name of this TrackerType.  # noqa: E501
        :type: str
        """

        self._var_name = var_name

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
        if issubclass(TrackerType, dict):
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
        if not isinstance(other, TrackerType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
