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

class TrackerItemReview(object):
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
        'config': 'TrackerItemReviewConfig',
        'result': 'str',
        'reviewers': 'list[TrackerItemReviewVote]',
        'tracker_item': 'TrackerItemRevision'
    }

    attribute_map = {
        'config': 'config',
        'result': 'result',
        'reviewers': 'reviewers',
        'tracker_item': 'trackerItem'
    }

    def __init__(self, config=None, result=None, reviewers=None, tracker_item=None):  # noqa: E501
        """TrackerItemReview - a model defined in Swagger"""  # noqa: E501
        self._config = None
        self._result = None
        self._reviewers = None
        self._tracker_item = None
        self.discriminator = None
        if config is not None:
            self.config = config
        if result is not None:
            self.result = result
        if reviewers is not None:
            self.reviewers = reviewers
        if tracker_item is not None:
            self.tracker_item = tracker_item

    @property
    def config(self):
        """Gets the config of this TrackerItemReview.  # noqa: E501


        :return: The config of this TrackerItemReview.  # noqa: E501
        :rtype: TrackerItemReviewConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this TrackerItemReview.


        :param config: The config of this TrackerItemReview.  # noqa: E501
        :type: TrackerItemReviewConfig
        """

        self._config = config

    @property
    def result(self):
        """Gets the result of this TrackerItemReview.  # noqa: E501

        Whether the review is approved or rejected  # noqa: E501

        :return: The result of this TrackerItemReview.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this TrackerItemReview.

        Whether the review is approved or rejected  # noqa: E501

        :param result: The result of this TrackerItemReview.  # noqa: E501
        :type: str
        """
        allowed_values = ["APPROVED", "REJECTED", "UNDECIDED"]  # noqa: E501
        if result not in allowed_values:
            raise ValueError(
                "Invalid value for `result` ({0}), must be one of {1}"  # noqa: E501
                .format(result, allowed_values)
            )

        self._result = result

    @property
    def reviewers(self):
        """Gets the reviewers of this TrackerItemReview.  # noqa: E501

        List of reviewers, and their votes  # noqa: E501

        :return: The reviewers of this TrackerItemReview.  # noqa: E501
        :rtype: list[TrackerItemReviewVote]
        """
        return self._reviewers

    @reviewers.setter
    def reviewers(self, reviewers):
        """Sets the reviewers of this TrackerItemReview.

        List of reviewers, and their votes  # noqa: E501

        :param reviewers: The reviewers of this TrackerItemReview.  # noqa: E501
        :type: list[TrackerItemReviewVote]
        """

        self._reviewers = reviewers

    @property
    def tracker_item(self):
        """Gets the tracker_item of this TrackerItemReview.  # noqa: E501


        :return: The tracker_item of this TrackerItemReview.  # noqa: E501
        :rtype: TrackerItemRevision
        """
        return self._tracker_item

    @tracker_item.setter
    def tracker_item(self, tracker_item):
        """Sets the tracker_item of this TrackerItemReview.


        :param tracker_item: The tracker_item of this TrackerItemReview.  # noqa: E501
        :type: TrackerItemRevision
        """

        self._tracker_item = tracker_item

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
        if issubclass(TrackerItemReview, dict):
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
        if not isinstance(other, TrackerItemReview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
