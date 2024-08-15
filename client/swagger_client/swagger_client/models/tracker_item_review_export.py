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

class TrackerItemReviewExport(object):
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
        'reviewers': 'list[TrackerItemReviewVoteExport]',
        'tracker_item_version': 'int'
    }

    attribute_map = {
        'reviewers': 'reviewers',
        'tracker_item_version': 'trackerItemVersion'
    }

    def __init__(self, reviewers=None, tracker_item_version=None):  # noqa: E501
        """TrackerItemReviewExport - a model defined in Swagger"""  # noqa: E501
        self._reviewers = None
        self._tracker_item_version = None
        self.discriminator = None
        if reviewers is not None:
            self.reviewers = reviewers
        if tracker_item_version is not None:
            self.tracker_item_version = tracker_item_version

    @property
    def reviewers(self):
        """Gets the reviewers of this TrackerItemReviewExport.  # noqa: E501

        List of reviewers and their votes  # noqa: E501

        :return: The reviewers of this TrackerItemReviewExport.  # noqa: E501
        :rtype: list[TrackerItemReviewVoteExport]
        """
        return self._reviewers

    @reviewers.setter
    def reviewers(self, reviewers):
        """Sets the reviewers of this TrackerItemReviewExport.

        List of reviewers and their votes  # noqa: E501

        :param reviewers: The reviewers of this TrackerItemReviewExport.  # noqa: E501
        :type: list[TrackerItemReviewVoteExport]
        """

        self._reviewers = reviewers

    @property
    def tracker_item_version(self):
        """Gets the tracker_item_version of this TrackerItemReviewExport.  # noqa: E501

        Version of the Tracker Item at the time of the review  # noqa: E501

        :return: The tracker_item_version of this TrackerItemReviewExport.  # noqa: E501
        :rtype: int
        """
        return self._tracker_item_version

    @tracker_item_version.setter
    def tracker_item_version(self, tracker_item_version):
        """Sets the tracker_item_version of this TrackerItemReviewExport.

        Version of the Tracker Item at the time of the review  # noqa: E501

        :param tracker_item_version: The tracker_item_version of this TrackerItemReviewExport.  # noqa: E501
        :type: int
        """

        self._tracker_item_version = tracker_item_version

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
        if issubclass(TrackerItemReviewExport, dict):
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
        if not isinstance(other, TrackerItemReviewExport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
