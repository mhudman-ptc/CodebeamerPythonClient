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

class ReportReferenceLevelSettings(object):
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
        'columns': 'list[ReportColumnSettings]',
        'downstream_reference': 'bool',
        'level': 'int',
        'reference_tracker_types': 'list[TrackerTypeReference]',
        'reference_trackers': 'list[TrackerReference]',
        'upstream_reference': 'bool'
    }

    attribute_map = {
        'columns': 'columns',
        'downstream_reference': 'downstreamReference',
        'level': 'level',
        'reference_tracker_types': 'referenceTrackerTypes',
        'reference_trackers': 'referenceTrackers',
        'upstream_reference': 'upstreamReference'
    }

    def __init__(self, columns=None, downstream_reference=None, level=None, reference_tracker_types=None, reference_trackers=None, upstream_reference=None):  # noqa: E501
        """ReportReferenceLevelSettings - a model defined in Swagger"""  # noqa: E501
        self._columns = None
        self._downstream_reference = None
        self._level = None
        self._reference_tracker_types = None
        self._reference_trackers = None
        self._upstream_reference = None
        self.discriminator = None
        self.columns = columns
        self.downstream_reference = downstream_reference
        self.level = level
        if reference_tracker_types is not None:
            self.reference_tracker_types = reference_tracker_types
        if reference_trackers is not None:
            self.reference_trackers = reference_trackers
        self.upstream_reference = upstream_reference

    @property
    def columns(self):
        """Gets the columns of this ReportReferenceLevelSettings.  # noqa: E501

        Columns to show on this reference level.  # noqa: E501

        :return: The columns of this ReportReferenceLevelSettings.  # noqa: E501
        :rtype: list[ReportColumnSettings]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this ReportReferenceLevelSettings.

        Columns to show on this reference level.  # noqa: E501

        :param columns: The columns of this ReportReferenceLevelSettings.  # noqa: E501
        :type: list[ReportColumnSettings]
        """
        if columns is None:
            raise ValueError("Invalid value for `columns`, must not be `None`")  # noqa: E501

        self._columns = columns

    @property
    def downstream_reference(self):
        """Gets the downstream_reference of this ReportReferenceLevelSettings.  # noqa: E501

        Include downstream references indicator.  # noqa: E501

        :return: The downstream_reference of this ReportReferenceLevelSettings.  # noqa: E501
        :rtype: bool
        """
        return self._downstream_reference

    @downstream_reference.setter
    def downstream_reference(self, downstream_reference):
        """Sets the downstream_reference of this ReportReferenceLevelSettings.

        Include downstream references indicator.  # noqa: E501

        :param downstream_reference: The downstream_reference of this ReportReferenceLevelSettings.  # noqa: E501
        :type: bool
        """
        if downstream_reference is None:
            raise ValueError("Invalid value for `downstream_reference`, must not be `None`")  # noqa: E501

        self._downstream_reference = downstream_reference

    @property
    def level(self):
        """Gets the level of this ReportReferenceLevelSettings.  # noqa: E501

        Level of the reference layer  # noqa: E501

        :return: The level of this ReportReferenceLevelSettings.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ReportReferenceLevelSettings.

        Level of the reference layer  # noqa: E501

        :param level: The level of this ReportReferenceLevelSettings.  # noqa: E501
        :type: int
        """
        if level is None:
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501

        self._level = level

    @property
    def reference_tracker_types(self):
        """Gets the reference_tracker_types of this ReportReferenceLevelSettings.  # noqa: E501

        Tracker types to include on this level.  # noqa: E501

        :return: The reference_tracker_types of this ReportReferenceLevelSettings.  # noqa: E501
        :rtype: list[TrackerTypeReference]
        """
        return self._reference_tracker_types

    @reference_tracker_types.setter
    def reference_tracker_types(self, reference_tracker_types):
        """Sets the reference_tracker_types of this ReportReferenceLevelSettings.

        Tracker types to include on this level.  # noqa: E501

        :param reference_tracker_types: The reference_tracker_types of this ReportReferenceLevelSettings.  # noqa: E501
        :type: list[TrackerTypeReference]
        """

        self._reference_tracker_types = reference_tracker_types

    @property
    def reference_trackers(self):
        """Gets the reference_trackers of this ReportReferenceLevelSettings.  # noqa: E501

        Trackers to include on this level.  # noqa: E501

        :return: The reference_trackers of this ReportReferenceLevelSettings.  # noqa: E501
        :rtype: list[TrackerReference]
        """
        return self._reference_trackers

    @reference_trackers.setter
    def reference_trackers(self, reference_trackers):
        """Sets the reference_trackers of this ReportReferenceLevelSettings.

        Trackers to include on this level.  # noqa: E501

        :param reference_trackers: The reference_trackers of this ReportReferenceLevelSettings.  # noqa: E501
        :type: list[TrackerReference]
        """

        self._reference_trackers = reference_trackers

    @property
    def upstream_reference(self):
        """Gets the upstream_reference of this ReportReferenceLevelSettings.  # noqa: E501

        Include upstream references indicator.  # noqa: E501

        :return: The upstream_reference of this ReportReferenceLevelSettings.  # noqa: E501
        :rtype: bool
        """
        return self._upstream_reference

    @upstream_reference.setter
    def upstream_reference(self, upstream_reference):
        """Sets the upstream_reference of this ReportReferenceLevelSettings.

        Include upstream references indicator.  # noqa: E501

        :param upstream_reference: The upstream_reference of this ReportReferenceLevelSettings.  # noqa: E501
        :type: bool
        """
        if upstream_reference is None:
            raise ValueError("Invalid value for `upstream_reference`, must not be `None`")  # noqa: E501

        self._upstream_reference = upstream_reference

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
        if issubclass(ReportReferenceLevelSettings, dict):
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
        if not isinstance(other, ReportReferenceLevelSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
