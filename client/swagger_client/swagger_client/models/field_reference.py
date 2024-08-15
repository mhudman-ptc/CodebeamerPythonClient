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
from swagger_client.models.abstract_reference import AbstractReference  # noqa: F401,E501

class FieldReference(AbstractReference):
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
        'shared_field_names': 'list[str]',
        'tracker_id': 'int'
    }
    if hasattr(AbstractReference, "swagger_types"):
        swagger_types.update(AbstractReference.swagger_types)

    attribute_map = {
        'shared_field_names': 'sharedFieldNames',
        'tracker_id': 'trackerId'
    }
    if hasattr(AbstractReference, "attribute_map"):
        attribute_map.update(AbstractReference.attribute_map)

    def __init__(self, shared_field_names=None, tracker_id=None, *args, **kwargs):  # noqa: E501
        """FieldReference - a model defined in Swagger"""  # noqa: E501
        self._shared_field_names = None
        self._tracker_id = None
        self.discriminator = None
        if shared_field_names is not None:
            self.shared_field_names = shared_field_names
        if tracker_id is not None:
            self.tracker_id = tracker_id
        AbstractReference.__init__(self, *args, **kwargs)

    @property
    def shared_field_names(self):
        """Gets the shared_field_names of this FieldReference.  # noqa: E501

        The names of a shared fields assigned to the field.  # noqa: E501

        :return: The shared_field_names of this FieldReference.  # noqa: E501
        :rtype: list[str]
        """
        return self._shared_field_names

    @shared_field_names.setter
    def shared_field_names(self, shared_field_names):
        """Sets the shared_field_names of this FieldReference.

        The names of a shared fields assigned to the field.  # noqa: E501

        :param shared_field_names: The shared_field_names of this FieldReference.  # noqa: E501
        :type: list[str]
        """

        self._shared_field_names = shared_field_names

    @property
    def tracker_id(self):
        """Gets the tracker_id of this FieldReference.  # noqa: E501

        Id of the tracker  # noqa: E501

        :return: The tracker_id of this FieldReference.  # noqa: E501
        :rtype: int
        """
        return self._tracker_id

    @tracker_id.setter
    def tracker_id(self, tracker_id):
        """Sets the tracker_id of this FieldReference.

        Id of the tracker  # noqa: E501

        :param tracker_id: The tracker_id of this FieldReference.  # noqa: E501
        :type: int
        """

        self._tracker_id = tracker_id

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
        if issubclass(FieldReference, dict):
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
        if not isinstance(other, FieldReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
