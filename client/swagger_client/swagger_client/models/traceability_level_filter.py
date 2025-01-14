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

class TraceabilityLevelFilter(object):
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
        'folders_and_information': 'bool',
        'history_baseline_id': 'int',
        'history_date': 'datetime',
        'incoming_association': 'bool',
        'incoming_reference': 'bool',
        'outgoing_association': 'bool',
        'outgoing_reference': 'bool',
        'previous_level_items': 'list[TrackerItemRevision]',
        'show_test_step_references': 'bool'
    }

    attribute_map = {
        'cb_ql': 'cbQL',
        'folders_and_information': 'foldersAndInformation',
        'history_baseline_id': 'historyBaselineId',
        'history_date': 'historyDate',
        'incoming_association': 'incomingAssociation',
        'incoming_reference': 'incomingReference',
        'outgoing_association': 'outgoingAssociation',
        'outgoing_reference': 'outgoingReference',
        'previous_level_items': 'previousLevelItems',
        'show_test_step_references': 'showTestStepReferences'
    }

    def __init__(self, cb_ql=None, folders_and_information=False, history_baseline_id=None, history_date=None, incoming_association=True, incoming_reference=True, outgoing_association=True, outgoing_reference=True, previous_level_items=None, show_test_step_references=None):  # noqa: E501
        """TraceabilityLevelFilter - a model defined in Swagger"""  # noqa: E501
        self._cb_ql = None
        self._folders_and_information = None
        self._history_baseline_id = None
        self._history_date = None
        self._incoming_association = None
        self._incoming_reference = None
        self._outgoing_association = None
        self._outgoing_reference = None
        self._previous_level_items = None
        self._show_test_step_references = None
        self.discriminator = None
        self.cb_ql = cb_ql
        if folders_and_information is not None:
            self.folders_and_information = folders_and_information
        if history_baseline_id is not None:
            self.history_baseline_id = history_baseline_id
        if history_date is not None:
            self.history_date = history_date
        if incoming_association is not None:
            self.incoming_association = incoming_association
        if incoming_reference is not None:
            self.incoming_reference = incoming_reference
        if outgoing_association is not None:
            self.outgoing_association = outgoing_association
        if outgoing_reference is not None:
            self.outgoing_reference = outgoing_reference
        if previous_level_items is not None:
            self.previous_level_items = previous_level_items
        if show_test_step_references is not None:
            self.show_test_step_references = show_test_step_references

    @property
    def cb_ql(self):
        """Gets the cb_ql of this TraceabilityLevelFilter.  # noqa: E501

        cbQL  # noqa: E501

        :return: The cb_ql of this TraceabilityLevelFilter.  # noqa: E501
        :rtype: str
        """
        return self._cb_ql

    @cb_ql.setter
    def cb_ql(self, cb_ql):
        """Sets the cb_ql of this TraceabilityLevelFilter.

        cbQL  # noqa: E501

        :param cb_ql: The cb_ql of this TraceabilityLevelFilter.  # noqa: E501
        :type: str
        """
        if cb_ql is None:
            raise ValueError("Invalid value for `cb_ql`, must not be `None`")  # noqa: E501

        self._cb_ql = cb_ql

    @property
    def folders_and_information(self):
        """Gets the folders_and_information of this TraceabilityLevelFilter.  # noqa: E501

        Show folders and information  # noqa: E501

        :return: The folders_and_information of this TraceabilityLevelFilter.  # noqa: E501
        :rtype: bool
        """
        return self._folders_and_information

    @folders_and_information.setter
    def folders_and_information(self, folders_and_information):
        """Sets the folders_and_information of this TraceabilityLevelFilter.

        Show folders and information  # noqa: E501

        :param folders_and_information: The folders_and_information of this TraceabilityLevelFilter.  # noqa: E501
        :type: bool
        """

        self._folders_and_information = folders_and_information

    @property
    def history_baseline_id(self):
        """Gets the history_baseline_id of this TraceabilityLevelFilter.  # noqa: E501

        History Baseline Id - Snapshot view of the given baseline  # noqa: E501

        :return: The history_baseline_id of this TraceabilityLevelFilter.  # noqa: E501
        :rtype: int
        """
        return self._history_baseline_id

    @history_baseline_id.setter
    def history_baseline_id(self, history_baseline_id):
        """Sets the history_baseline_id of this TraceabilityLevelFilter.

        History Baseline Id - Snapshot view of the given baseline  # noqa: E501

        :param history_baseline_id: The history_baseline_id of this TraceabilityLevelFilter.  # noqa: E501
        :type: int
        """

        self._history_baseline_id = history_baseline_id

    @property
    def history_date(self):
        """Gets the history_date of this TraceabilityLevelFilter.  # noqa: E501

        History Date - Snapshot view of the given date  # noqa: E501

        :return: The history_date of this TraceabilityLevelFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._history_date

    @history_date.setter
    def history_date(self, history_date):
        """Sets the history_date of this TraceabilityLevelFilter.

        History Date - Snapshot view of the given date  # noqa: E501

        :param history_date: The history_date of this TraceabilityLevelFilter.  # noqa: E501
        :type: datetime
        """

        self._history_date = history_date

    @property
    def incoming_association(self):
        """Gets the incoming_association of this TraceabilityLevelFilter.  # noqa: E501

        Show incoming association  # noqa: E501

        :return: The incoming_association of this TraceabilityLevelFilter.  # noqa: E501
        :rtype: bool
        """
        return self._incoming_association

    @incoming_association.setter
    def incoming_association(self, incoming_association):
        """Sets the incoming_association of this TraceabilityLevelFilter.

        Show incoming association  # noqa: E501

        :param incoming_association: The incoming_association of this TraceabilityLevelFilter.  # noqa: E501
        :type: bool
        """

        self._incoming_association = incoming_association

    @property
    def incoming_reference(self):
        """Gets the incoming_reference of this TraceabilityLevelFilter.  # noqa: E501

        Show incoming references  # noqa: E501

        :return: The incoming_reference of this TraceabilityLevelFilter.  # noqa: E501
        :rtype: bool
        """
        return self._incoming_reference

    @incoming_reference.setter
    def incoming_reference(self, incoming_reference):
        """Sets the incoming_reference of this TraceabilityLevelFilter.

        Show incoming references  # noqa: E501

        :param incoming_reference: The incoming_reference of this TraceabilityLevelFilter.  # noqa: E501
        :type: bool
        """

        self._incoming_reference = incoming_reference

    @property
    def outgoing_association(self):
        """Gets the outgoing_association of this TraceabilityLevelFilter.  # noqa: E501

        Show outgoing association  # noqa: E501

        :return: The outgoing_association of this TraceabilityLevelFilter.  # noqa: E501
        :rtype: bool
        """
        return self._outgoing_association

    @outgoing_association.setter
    def outgoing_association(self, outgoing_association):
        """Sets the outgoing_association of this TraceabilityLevelFilter.

        Show outgoing association  # noqa: E501

        :param outgoing_association: The outgoing_association of this TraceabilityLevelFilter.  # noqa: E501
        :type: bool
        """

        self._outgoing_association = outgoing_association

    @property
    def outgoing_reference(self):
        """Gets the outgoing_reference of this TraceabilityLevelFilter.  # noqa: E501

        Show outgoing references  # noqa: E501

        :return: The outgoing_reference of this TraceabilityLevelFilter.  # noqa: E501
        :rtype: bool
        """
        return self._outgoing_reference

    @outgoing_reference.setter
    def outgoing_reference(self, outgoing_reference):
        """Sets the outgoing_reference of this TraceabilityLevelFilter.

        Show outgoing references  # noqa: E501

        :param outgoing_reference: The outgoing_reference of this TraceabilityLevelFilter.  # noqa: E501
        :type: bool
        """

        self._outgoing_reference = outgoing_reference

    @property
    def previous_level_items(self):
        """Gets the previous_level_items of this TraceabilityLevelFilter.  # noqa: E501

        Previous Level Items  # noqa: E501

        :return: The previous_level_items of this TraceabilityLevelFilter.  # noqa: E501
        :rtype: list[TrackerItemRevision]
        """
        return self._previous_level_items

    @previous_level_items.setter
    def previous_level_items(self, previous_level_items):
        """Sets the previous_level_items of this TraceabilityLevelFilter.

        Previous Level Items  # noqa: E501

        :param previous_level_items: The previous_level_items of this TraceabilityLevelFilter.  # noqa: E501
        :type: list[TrackerItemRevision]
        """

        self._previous_level_items = previous_level_items

    @property
    def show_test_step_references(self):
        """Gets the show_test_step_references of this TraceabilityLevelFilter.  # noqa: E501


        :return: The show_test_step_references of this TraceabilityLevelFilter.  # noqa: E501
        :rtype: bool
        """
        return self._show_test_step_references

    @show_test_step_references.setter
    def show_test_step_references(self, show_test_step_references):
        """Sets the show_test_step_references of this TraceabilityLevelFilter.


        :param show_test_step_references: The show_test_step_references of this TraceabilityLevelFilter.  # noqa: E501
        :type: bool
        """

        self._show_test_step_references = show_test_step_references

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
        if issubclass(TraceabilityLevelFilter, dict):
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
        if not isinstance(other, TraceabilityLevelFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
