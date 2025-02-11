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
from swagger_client.models.abstract_field_value import AbstractFieldValue  # noqa: F401,E501

class ReferredTestStepFieldValue(AbstractFieldValue):
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
        'referred_step_id': 'str',
        'referred_test_case_id': 'int',
        'value': 'str'
    }
    if hasattr(AbstractFieldValue, "swagger_types"):
        swagger_types.update(AbstractFieldValue.swagger_types)

    attribute_map = {
        'referred_step_id': 'referredStepId',
        'referred_test_case_id': 'referredTestCaseId',
        'value': 'value'
    }
    if hasattr(AbstractFieldValue, "attribute_map"):
        attribute_map.update(AbstractFieldValue.attribute_map)

    def __init__(self, referred_step_id=None, referred_test_case_id=None, value=None, *args, **kwargs):  # noqa: E501
        """ReferredTestStepFieldValue - a model defined in Swagger"""  # noqa: E501
        self._referred_step_id = None
        self._referred_test_case_id = None
        self._value = None
        self.discriminator = None
        self.referred_step_id = referred_step_id
        self.referred_test_case_id = referred_test_case_id
        if value is not None:
            self.value = value
        AbstractFieldValue.__init__(self, *args, **kwargs)

    @property
    def referred_step_id(self):
        """Gets the referred_step_id of this ReferredTestStepFieldValue.  # noqa: E501

        Id of the referred test step  # noqa: E501

        :return: The referred_step_id of this ReferredTestStepFieldValue.  # noqa: E501
        :rtype: str
        """
        return self._referred_step_id

    @referred_step_id.setter
    def referred_step_id(self, referred_step_id):
        """Sets the referred_step_id of this ReferredTestStepFieldValue.

        Id of the referred test step  # noqa: E501

        :param referred_step_id: The referred_step_id of this ReferredTestStepFieldValue.  # noqa: E501
        :type: str
        """
        if referred_step_id is None:
            raise ValueError("Invalid value for `referred_step_id`, must not be `None`")  # noqa: E501

        self._referred_step_id = referred_step_id

    @property
    def referred_test_case_id(self):
        """Gets the referred_test_case_id of this ReferredTestStepFieldValue.  # noqa: E501

        Id of the test case where the referred test step comes  # noqa: E501

        :return: The referred_test_case_id of this ReferredTestStepFieldValue.  # noqa: E501
        :rtype: int
        """
        return self._referred_test_case_id

    @referred_test_case_id.setter
    def referred_test_case_id(self, referred_test_case_id):
        """Sets the referred_test_case_id of this ReferredTestStepFieldValue.

        Id of the test case where the referred test step comes  # noqa: E501

        :param referred_test_case_id: The referred_test_case_id of this ReferredTestStepFieldValue.  # noqa: E501
        :type: int
        """
        if referred_test_case_id is None:
            raise ValueError("Invalid value for `referred_test_case_id`, must not be `None`")  # noqa: E501

        self._referred_test_case_id = referred_test_case_id

    @property
    def value(self):
        """Gets the value of this ReferredTestStepFieldValue.  # noqa: E501

        Id of the Test Step  # noqa: E501

        :return: The value of this ReferredTestStepFieldValue.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ReferredTestStepFieldValue.

        Id of the Test Step  # noqa: E501

        :param value: The value of this ReferredTestStepFieldValue.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(ReferredTestStepFieldValue, dict):
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
        if not isinstance(other, ReferredTestStepFieldValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
