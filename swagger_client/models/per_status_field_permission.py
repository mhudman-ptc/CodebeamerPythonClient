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
from swagger_client.models.base_tracker_field_permission import BaseTrackerFieldPermission  # noqa: F401,E501

class PerStatusFieldPermission(BaseTrackerFieldPermission):
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
        'access_permissions_per_status_map': 'dict(str, list[TrackerFieldPermissionAccessPermission])'
    }
    if hasattr(BaseTrackerFieldPermission, "swagger_types"):
        swagger_types.update(BaseTrackerFieldPermission.swagger_types)

    attribute_map = {
        'access_permissions_per_status_map': 'accessPermissionsPerStatusMap'
    }
    if hasattr(BaseTrackerFieldPermission, "attribute_map"):
        attribute_map.update(BaseTrackerFieldPermission.attribute_map)

    def __init__(self, access_permissions_per_status_map=None, *args, **kwargs):  # noqa: E501
        """PerStatusFieldPermission - a model defined in Swagger"""  # noqa: E501
        self._access_permissions_per_status_map = None
        self.discriminator = None
        if access_permissions_per_status_map is not None:
            self.access_permissions_per_status_map = access_permissions_per_status_map
        BaseTrackerFieldPermission.__init__(self, *args, **kwargs)

    @property
    def access_permissions_per_status_map(self):
        """Gets the access_permissions_per_status_map of this PerStatusFieldPermission.  # noqa: E501


        :return: The access_permissions_per_status_map of this PerStatusFieldPermission.  # noqa: E501
        :rtype: dict(str, list[TrackerFieldPermissionAccessPermission])
        """
        return self._access_permissions_per_status_map

    @access_permissions_per_status_map.setter
    def access_permissions_per_status_map(self, access_permissions_per_status_map):
        """Sets the access_permissions_per_status_map of this PerStatusFieldPermission.


        :param access_permissions_per_status_map: The access_permissions_per_status_map of this PerStatusFieldPermission.  # noqa: E501
        :type: dict(str, list[TrackerFieldPermissionAccessPermission])
        """

        self._access_permissions_per_status_map = access_permissions_per_status_map

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
        if issubclass(PerStatusFieldPermission, dict):
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
        if not isinstance(other, PerStatusFieldPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
