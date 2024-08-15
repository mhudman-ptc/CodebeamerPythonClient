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
from swagger_client.models.abstract_background_job_status_info import AbstractBackgroundJobStatusInfo  # noqa: F401,E501

class DependencyFinderJobStatusInfo(AbstractBackgroundJobStatusInfo):
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
        'closed_project_warnings': 'list[str]',
        'dependencies': 'list[CrossProjectDependency]',
        'missing_permission_warnings': 'list[str]',
        'projects_checked': 'int',
        'projects_scheduled': 'int'
    }
    if hasattr(AbstractBackgroundJobStatusInfo, "swagger_types"):
        swagger_types.update(AbstractBackgroundJobStatusInfo.swagger_types)

    attribute_map = {
        'closed_project_warnings': 'closedProjectWarnings',
        'dependencies': 'dependencies',
        'missing_permission_warnings': 'missingPermissionWarnings',
        'projects_checked': 'projectsChecked',
        'projects_scheduled': 'projectsScheduled'
    }
    if hasattr(AbstractBackgroundJobStatusInfo, "attribute_map"):
        attribute_map.update(AbstractBackgroundJobStatusInfo.attribute_map)

    def __init__(self, closed_project_warnings=None, dependencies=None, missing_permission_warnings=None, projects_checked=None, projects_scheduled=None, *args, **kwargs):  # noqa: E501
        """DependencyFinderJobStatusInfo - a model defined in Swagger"""  # noqa: E501
        self._closed_project_warnings = None
        self._dependencies = None
        self._missing_permission_warnings = None
        self._projects_checked = None
        self._projects_scheduled = None
        self.discriminator = None
        if closed_project_warnings is not None:
            self.closed_project_warnings = closed_project_warnings
        if dependencies is not None:
            self.dependencies = dependencies
        if missing_permission_warnings is not None:
            self.missing_permission_warnings = missing_permission_warnings
        if projects_checked is not None:
            self.projects_checked = projects_checked
        if projects_scheduled is not None:
            self.projects_scheduled = projects_scheduled
        AbstractBackgroundJobStatusInfo.__init__(self, *args, **kwargs)

    @property
    def closed_project_warnings(self):
        """Gets the closed_project_warnings of this DependencyFinderJobStatusInfo.  # noqa: E501

        Warnings due to closed projects.  # noqa: E501

        :return: The closed_project_warnings of this DependencyFinderJobStatusInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._closed_project_warnings

    @closed_project_warnings.setter
    def closed_project_warnings(self, closed_project_warnings):
        """Sets the closed_project_warnings of this DependencyFinderJobStatusInfo.

        Warnings due to closed projects.  # noqa: E501

        :param closed_project_warnings: The closed_project_warnings of this DependencyFinderJobStatusInfo.  # noqa: E501
        :type: list[str]
        """

        self._closed_project_warnings = closed_project_warnings

    @property
    def dependencies(self):
        """Gets the dependencies of this DependencyFinderJobStatusInfo.  # noqa: E501

        Dependencies found among projects.  # noqa: E501

        :return: The dependencies of this DependencyFinderJobStatusInfo.  # noqa: E501
        :rtype: list[CrossProjectDependency]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this DependencyFinderJobStatusInfo.

        Dependencies found among projects.  # noqa: E501

        :param dependencies: The dependencies of this DependencyFinderJobStatusInfo.  # noqa: E501
        :type: list[CrossProjectDependency]
        """

        self._dependencies = dependencies

    @property
    def missing_permission_warnings(self):
        """Gets the missing_permission_warnings of this DependencyFinderJobStatusInfo.  # noqa: E501

        Permission warnings.  # noqa: E501

        :return: The missing_permission_warnings of this DependencyFinderJobStatusInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._missing_permission_warnings

    @missing_permission_warnings.setter
    def missing_permission_warnings(self, missing_permission_warnings):
        """Sets the missing_permission_warnings of this DependencyFinderJobStatusInfo.

        Permission warnings.  # noqa: E501

        :param missing_permission_warnings: The missing_permission_warnings of this DependencyFinderJobStatusInfo.  # noqa: E501
        :type: list[str]
        """

        self._missing_permission_warnings = missing_permission_warnings

    @property
    def projects_checked(self):
        """Gets the projects_checked of this DependencyFinderJobStatusInfo.  # noqa: E501

        Number of projects already checked for dependencies  # noqa: E501

        :return: The projects_checked of this DependencyFinderJobStatusInfo.  # noqa: E501
        :rtype: int
        """
        return self._projects_checked

    @projects_checked.setter
    def projects_checked(self, projects_checked):
        """Sets the projects_checked of this DependencyFinderJobStatusInfo.

        Number of projects already checked for dependencies  # noqa: E501

        :param projects_checked: The projects_checked of this DependencyFinderJobStatusInfo.  # noqa: E501
        :type: int
        """

        self._projects_checked = projects_checked

    @property
    def projects_scheduled(self):
        """Gets the projects_scheduled of this DependencyFinderJobStatusInfo.  # noqa: E501

        Number of projects scheduled for dependency collection  # noqa: E501

        :return: The projects_scheduled of this DependencyFinderJobStatusInfo.  # noqa: E501
        :rtype: int
        """
        return self._projects_scheduled

    @projects_scheduled.setter
    def projects_scheduled(self, projects_scheduled):
        """Sets the projects_scheduled of this DependencyFinderJobStatusInfo.

        Number of projects scheduled for dependency collection  # noqa: E501

        :param projects_scheduled: The projects_scheduled of this DependencyFinderJobStatusInfo.  # noqa: E501
        :type: int
        """

        self._projects_scheduled = projects_scheduled

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
        if issubclass(DependencyFinderJobStatusInfo, dict):
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
        if not isinstance(other, DependencyFinderJobStatusInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
