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

class TrackerItemReviewVote(object):
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
        'as_role': 'RoleReference',
        'decision': 'str',
        'reviewed_at': 'datetime',
        'user': 'UserReference'
    }

    attribute_map = {
        'as_role': 'asRole',
        'decision': 'decision',
        'reviewed_at': 'reviewedAt',
        'user': 'user'
    }

    def __init__(self, as_role=None, decision=None, reviewed_at=None, user=None):  # noqa: E501
        """TrackerItemReviewVote - a model defined in Swagger"""  # noqa: E501
        self._as_role = None
        self._decision = None
        self._reviewed_at = None
        self._user = None
        self.discriminator = None
        if as_role is not None:
            self.as_role = as_role
        if decision is not None:
            self.decision = decision
        if reviewed_at is not None:
            self.reviewed_at = reviewed_at
        if user is not None:
            self.user = user

    @property
    def as_role(self):
        """Gets the as_role of this TrackerItemReviewVote.  # noqa: E501


        :return: The as_role of this TrackerItemReviewVote.  # noqa: E501
        :rtype: RoleReference
        """
        return self._as_role

    @as_role.setter
    def as_role(self, as_role):
        """Sets the as_role of this TrackerItemReviewVote.


        :param as_role: The as_role of this TrackerItemReviewVote.  # noqa: E501
        :type: RoleReference
        """

        self._as_role = as_role

    @property
    def decision(self):
        """Gets the decision of this TrackerItemReviewVote.  # noqa: E501

        The result of this particular vote  # noqa: E501

        :return: The decision of this TrackerItemReviewVote.  # noqa: E501
        :rtype: str
        """
        return self._decision

    @decision.setter
    def decision(self, decision):
        """Sets the decision of this TrackerItemReviewVote.

        The result of this particular vote  # noqa: E501

        :param decision: The decision of this TrackerItemReviewVote.  # noqa: E501
        :type: str
        """
        allowed_values = ["APPROVED", "REJECTED", "UNDECIDED"]  # noqa: E501
        if decision not in allowed_values:
            raise ValueError(
                "Invalid value for `decision` ({0}), must be one of {1}"  # noqa: E501
                .format(decision, allowed_values)
            )

        self._decision = decision

    @property
    def reviewed_at(self):
        """Gets the reviewed_at of this TrackerItemReviewVote.  # noqa: E501

        Date and time of the vote  # noqa: E501

        :return: The reviewed_at of this TrackerItemReviewVote.  # noqa: E501
        :rtype: datetime
        """
        return self._reviewed_at

    @reviewed_at.setter
    def reviewed_at(self, reviewed_at):
        """Sets the reviewed_at of this TrackerItemReviewVote.

        Date and time of the vote  # noqa: E501

        :param reviewed_at: The reviewed_at of this TrackerItemReviewVote.  # noqa: E501
        :type: datetime
        """

        self._reviewed_at = reviewed_at

    @property
    def user(self):
        """Gets the user of this TrackerItemReviewVote.  # noqa: E501


        :return: The user of this TrackerItemReviewVote.  # noqa: E501
        :rtype: UserReference
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this TrackerItemReviewVote.


        :param user: The user of this TrackerItemReviewVote.  # noqa: E501
        :type: UserReference
        """

        self._user = user

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
        if issubclass(TrackerItemReviewVote, dict):
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
        if not isinstance(other, TrackerItemReviewVote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
