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

class AuditPermissionsRequest(object):
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
        'duration': 'str',
        'event_types': 'list[str]',
        'from_date': 'datetime',
        'project_ids': 'list[int]',
        'show_changes': 'bool',
        'target_user_names': 'list[str]',
        'to_date': 'datetime',
        'tracker_ids': 'list[int]',
        'user_names': 'list[str]'
    }

    attribute_map = {
        'duration': 'duration',
        'event_types': 'eventTypes',
        'from_date': 'fromDate',
        'project_ids': 'projectIds',
        'show_changes': 'showChanges',
        'target_user_names': 'targetUserNames',
        'to_date': 'toDate',
        'tracker_ids': 'trackerIds',
        'user_names': 'userNames'
    }

    def __init__(self, duration=None, event_types=None, from_date=None, project_ids=None, show_changes=False, target_user_names=None, to_date=None, tracker_ids=None, user_names=None):  # noqa: E501
        """AuditPermissionsRequest - a model defined in Swagger"""  # noqa: E501
        self._duration = None
        self._event_types = None
        self._from_date = None
        self._project_ids = None
        self._show_changes = None
        self._target_user_names = None
        self._to_date = None
        self._tracker_ids = None
        self._user_names = None
        self.discriminator = None
        if duration is not None:
            self.duration = duration
        self.event_types = event_types
        if from_date is not None:
            self.from_date = from_date
        if project_ids is not None:
            self.project_ids = project_ids
        if show_changes is not None:
            self.show_changes = show_changes
        if target_user_names is not None:
            self.target_user_names = target_user_names
        if to_date is not None:
            self.to_date = to_date
        if tracker_ids is not None:
            self.tracker_ids = tracker_ids
        if user_names is not None:
            self.user_names = user_names

    @property
    def duration(self):
        """Gets the duration of this AuditPermissionsRequest.  # noqa: E501

        duration  # noqa: E501

        :return: The duration of this AuditPermissionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this AuditPermissionsRequest.

        duration  # noqa: E501

        :param duration: The duration of this AuditPermissionsRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["TODAY", "THIS_WEEK", "THIS_MONTH", "THIS_QUARTER", "THIS_YEAR", "YESTERDAY", "LAST_2_DAYS", "LAST_5_DAYS", "LAST_7_DAYS", "LAST_10_DAYS", "LAST_30_DAYS", "LAST_365_DAYS"]  # noqa: E501
        if duration not in allowed_values:
            raise ValueError(
                "Invalid value for `duration` ({0}), must be one of {1}"  # noqa: E501
                .format(duration, allowed_values)
            )

        self._duration = duration

    @property
    def event_types(self):
        """Gets the event_types of this AuditPermissionsRequest.  # noqa: E501

        Event type names  # noqa: E501

        :return: The event_types of this AuditPermissionsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        """Sets the event_types of this AuditPermissionsRequest.

        Event type names  # noqa: E501

        :param event_types: The event_types of this AuditPermissionsRequest.  # noqa: E501
        :type: list[str]
        """
        if event_types is None:
            raise ValueError("Invalid value for `event_types`, must not be `None`")  # noqa: E501

        self._event_types = event_types

    @property
    def from_date(self):
        """Gets the from_date of this AuditPermissionsRequest.  # noqa: E501

        From date  # noqa: E501

        :return: The from_date of this AuditPermissionsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this AuditPermissionsRequest.

        From date  # noqa: E501

        :param from_date: The from_date of this AuditPermissionsRequest.  # noqa: E501
        :type: datetime
        """

        self._from_date = from_date

    @property
    def project_ids(self):
        """Gets the project_ids of this AuditPermissionsRequest.  # noqa: E501

        Project ids  # noqa: E501

        :return: The project_ids of this AuditPermissionsRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._project_ids

    @project_ids.setter
    def project_ids(self, project_ids):
        """Sets the project_ids of this AuditPermissionsRequest.

        Project ids  # noqa: E501

        :param project_ids: The project_ids of this AuditPermissionsRequest.  # noqa: E501
        :type: list[int]
        """

        self._project_ids = project_ids

    @property
    def show_changes(self):
        """Gets the show_changes of this AuditPermissionsRequest.  # noqa: E501

        Show changes  # noqa: E501

        :return: The show_changes of this AuditPermissionsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._show_changes

    @show_changes.setter
    def show_changes(self, show_changes):
        """Sets the show_changes of this AuditPermissionsRequest.

        Show changes  # noqa: E501

        :param show_changes: The show_changes of this AuditPermissionsRequest.  # noqa: E501
        :type: bool
        """

        self._show_changes = show_changes

    @property
    def target_user_names(self):
        """Gets the target_user_names of this AuditPermissionsRequest.  # noqa: E501

        Target user names  # noqa: E501

        :return: The target_user_names of this AuditPermissionsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_user_names

    @target_user_names.setter
    def target_user_names(self, target_user_names):
        """Sets the target_user_names of this AuditPermissionsRequest.

        Target user names  # noqa: E501

        :param target_user_names: The target_user_names of this AuditPermissionsRequest.  # noqa: E501
        :type: list[str]
        """

        self._target_user_names = target_user_names

    @property
    def to_date(self):
        """Gets the to_date of this AuditPermissionsRequest.  # noqa: E501

        To date  # noqa: E501

        :return: The to_date of this AuditPermissionsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this AuditPermissionsRequest.

        To date  # noqa: E501

        :param to_date: The to_date of this AuditPermissionsRequest.  # noqa: E501
        :type: datetime
        """

        self._to_date = to_date

    @property
    def tracker_ids(self):
        """Gets the tracker_ids of this AuditPermissionsRequest.  # noqa: E501

        Tracker ids  # noqa: E501

        :return: The tracker_ids of this AuditPermissionsRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._tracker_ids

    @tracker_ids.setter
    def tracker_ids(self, tracker_ids):
        """Sets the tracker_ids of this AuditPermissionsRequest.

        Tracker ids  # noqa: E501

        :param tracker_ids: The tracker_ids of this AuditPermissionsRequest.  # noqa: E501
        :type: list[int]
        """

        self._tracker_ids = tracker_ids

    @property
    def user_names(self):
        """Gets the user_names of this AuditPermissionsRequest.  # noqa: E501

        User names  # noqa: E501

        :return: The user_names of this AuditPermissionsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_names

    @user_names.setter
    def user_names(self, user_names):
        """Sets the user_names of this AuditPermissionsRequest.

        User names  # noqa: E501

        :param user_names: The user_names of this AuditPermissionsRequest.  # noqa: E501
        :type: list[str]
        """

        self._user_names = user_names

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
        if issubclass(AuditPermissionsRequest, dict):
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
        if not isinstance(other, AuditPermissionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
