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

class TrackerFilteringRequest(object):
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
        'deleted': 'bool',
        'hidden': 'bool',
        'key_name': 'str',
        'types': 'list[TrackerTypeReference]'
    }

    attribute_map = {
        'deleted': 'deleted',
        'hidden': 'hidden',
        'key_name': 'keyName',
        'types': 'types'
    }

    def __init__(self, deleted=None, hidden=None, key_name=None, types=None):  # noqa: E501
        """TrackerFilteringRequest - a model defined in Swagger"""  # noqa: E501
        self._deleted = None
        self._hidden = None
        self._key_name = None
        self._types = None
        self.discriminator = None
        if deleted is not None:
            self.deleted = deleted
        if hidden is not None:
            self.hidden = hidden
        if key_name is not None:
            self.key_name = key_name
        if types is not None:
            self.types = types

    @property
    def deleted(self):
        """Gets the deleted of this TrackerFilteringRequest.  # noqa: E501

        True to also show removed trackers.  # noqa: E501

        :return: The deleted of this TrackerFilteringRequest.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this TrackerFilteringRequest.

        True to also show removed trackers.  # noqa: E501

        :param deleted: The deleted of this TrackerFilteringRequest.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def hidden(self):
        """Gets the hidden of this TrackerFilteringRequest.  # noqa: E501

        True to also show hidden trackers.  # noqa: E501

        :return: The hidden of this TrackerFilteringRequest.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this TrackerFilteringRequest.

        True to also show hidden trackers.  # noqa: E501

        :param hidden: The hidden of this TrackerFilteringRequest.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def key_name(self):
        """Gets the key_name of this TrackerFilteringRequest.  # noqa: E501

        Filter by project key name  # noqa: E501

        :return: The key_name of this TrackerFilteringRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this TrackerFilteringRequest.

        Filter by project key name  # noqa: E501

        :param key_name: The key_name of this TrackerFilteringRequest.  # noqa: E501
        :type: str
        """

        self._key_name = key_name

    @property
    def types(self):
        """Gets the types of this TrackerFilteringRequest.  # noqa: E501

        List of tracker type references, to only show trackers of these types.  # noqa: E501

        :return: The types of this TrackerFilteringRequest.  # noqa: E501
        :rtype: list[TrackerTypeReference]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this TrackerFilteringRequest.

        List of tracker type references, to only show trackers of these types.  # noqa: E501

        :param types: The types of this TrackerFilteringRequest.  # noqa: E501
        :type: list[TrackerTypeReference]
        """

        self._types = types

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
        if issubclass(TrackerFilteringRequest, dict):
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
        if not isinstance(other, TrackerFilteringRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
