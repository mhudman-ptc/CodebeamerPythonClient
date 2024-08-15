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

class AbstractTrackerItemChange(object):
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
        'field': 'FieldReference',
        'name': 'str',
        'new_value': 'AbstractFieldValue',
        'old_value': 'AbstractFieldValue',
        'type': 'str'
    }

    attribute_map = {
        'field': 'field',
        'name': 'name',
        'new_value': 'newValue',
        'old_value': 'oldValue',
        'type': 'type'
    }

    discriminator_value_class_map = {
          'TrackerItemChange': 'TrackerItemChange',
'TrackerItemRowChange': 'TrackerItemRowChange'    }

    def __init__(self, field=None, name=None, new_value=None, old_value=None, type=None):  # noqa: E501
        """AbstractTrackerItemChange - a model defined in Swagger"""  # noqa: E501
        self._field = None
        self._name = None
        self._new_value = None
        self._old_value = None
        self._type = None
        self.discriminator = 'type'
        if field is not None:
            self.field = field
        if name is not None:
            self.name = name
        if new_value is not None:
            self.new_value = new_value
        if old_value is not None:
            self.old_value = old_value
        if type is not None:
            self.type = type

    @property
    def field(self):
        """Gets the field of this AbstractTrackerItemChange.  # noqa: E501


        :return: The field of this AbstractTrackerItemChange.  # noqa: E501
        :rtype: FieldReference
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this AbstractTrackerItemChange.


        :param field: The field of this AbstractTrackerItemChange.  # noqa: E501
        :type: FieldReference
        """

        self._field = field

    @property
    def name(self):
        """Gets the name of this AbstractTrackerItemChange.  # noqa: E501

        Name of the field  # noqa: E501

        :return: The name of this AbstractTrackerItemChange.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AbstractTrackerItemChange.

        Name of the field  # noqa: E501

        :param name: The name of this AbstractTrackerItemChange.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def new_value(self):
        """Gets the new_value of this AbstractTrackerItemChange.  # noqa: E501


        :return: The new_value of this AbstractTrackerItemChange.  # noqa: E501
        :rtype: AbstractFieldValue
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """Sets the new_value of this AbstractTrackerItemChange.


        :param new_value: The new_value of this AbstractTrackerItemChange.  # noqa: E501
        :type: AbstractFieldValue
        """

        self._new_value = new_value

    @property
    def old_value(self):
        """Gets the old_value of this AbstractTrackerItemChange.  # noqa: E501


        :return: The old_value of this AbstractTrackerItemChange.  # noqa: E501
        :rtype: AbstractFieldValue
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """Sets the old_value of this AbstractTrackerItemChange.


        :param old_value: The old_value of this AbstractTrackerItemChange.  # noqa: E501
        :type: AbstractFieldValue
        """

        self._old_value = old_value

    @property
    def type(self):
        """Gets the type of this AbstractTrackerItemChange.  # noqa: E501

        Change model type  # noqa: E501

        :return: The type of this AbstractTrackerItemChange.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AbstractTrackerItemChange.

        Change model type  # noqa: E501

        :param type: The type of this AbstractTrackerItemChange.  # noqa: E501
        :type: str
        """

        self._type = type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(AbstractTrackerItemChange, dict):
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
        if not isinstance(other, AbstractTrackerItemChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
