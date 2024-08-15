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

class AutomatedTestCaseRunResult(object):
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
        'conclusion': 'str',
        'description': 'str',
        'group_name': 'str',
        'name': 'str',
        'result': 'str',
        'run_time': 'int'
    }

    attribute_map = {
        'conclusion': 'conclusion',
        'description': 'description',
        'group_name': 'groupName',
        'name': 'name',
        'result': 'result',
        'run_time': 'runTime'
    }

    def __init__(self, conclusion=None, description=None, group_name=None, name=None, result=None, run_time=None):  # noqa: E501
        """AutomatedTestCaseRunResult - a model defined in Swagger"""  # noqa: E501
        self._conclusion = None
        self._description = None
        self._group_name = None
        self._name = None
        self._result = None
        self._run_time = None
        self.discriminator = None
        if conclusion is not None:
            self.conclusion = conclusion
        if description is not None:
            self.description = description
        if group_name is not None:
            self.group_name = group_name
        self.name = name
        self.result = result
        if run_time is not None:
            self.run_time = run_time

    @property
    def conclusion(self):
        """Gets the conclusion of this AutomatedTestCaseRunResult.  # noqa: E501

        Optional Test Case Run conclusion  # noqa: E501

        :return: The conclusion of this AutomatedTestCaseRunResult.  # noqa: E501
        :rtype: str
        """
        return self._conclusion

    @conclusion.setter
    def conclusion(self, conclusion):
        """Sets the conclusion of this AutomatedTestCaseRunResult.

        Optional Test Case Run conclusion  # noqa: E501

        :param conclusion: The conclusion of this AutomatedTestCaseRunResult.  # noqa: E501
        :type: str
        """

        self._conclusion = conclusion

    @property
    def description(self):
        """Gets the description of this AutomatedTestCaseRunResult.  # noqa: E501

        Description of the Test Case  # noqa: E501

        :return: The description of this AutomatedTestCaseRunResult.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AutomatedTestCaseRunResult.

        Description of the Test Case  # noqa: E501

        :param description: The description of this AutomatedTestCaseRunResult.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def group_name(self):
        """Gets the group_name of this AutomatedTestCaseRunResult.  # noqa: E501

        Group name of the Test Case  # noqa: E501

        :return: The group_name of this AutomatedTestCaseRunResult.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this AutomatedTestCaseRunResult.

        Group name of the Test Case  # noqa: E501

        :param group_name: The group_name of this AutomatedTestCaseRunResult.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def name(self):
        """Gets the name of this AutomatedTestCaseRunResult.  # noqa: E501

        Name of the Test Case  # noqa: E501

        :return: The name of this AutomatedTestCaseRunResult.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AutomatedTestCaseRunResult.

        Name of the Test Case  # noqa: E501

        :param name: The name of this AutomatedTestCaseRunResult.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def result(self):
        """Gets the result of this AutomatedTestCaseRunResult.  # noqa: E501

        Result of the test case  # noqa: E501

        :return: The result of this AutomatedTestCaseRunResult.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this AutomatedTestCaseRunResult.

        Result of the test case  # noqa: E501

        :param result: The result of this AutomatedTestCaseRunResult.  # noqa: E501
        :type: str
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501
        allowed_values = ["PASSED", "FAILED", "BLOCKED", "NOT_APPLICABLE"]  # noqa: E501
        if result not in allowed_values:
            raise ValueError(
                "Invalid value for `result` ({0}), must be one of {1}"  # noqa: E501
                .format(result, allowed_values)
            )

        self._result = result

    @property
    def run_time(self):
        """Gets the run_time of this AutomatedTestCaseRunResult.  # noqa: E501

        Optional runtime in seconds  # noqa: E501

        :return: The run_time of this AutomatedTestCaseRunResult.  # noqa: E501
        :rtype: int
        """
        return self._run_time

    @run_time.setter
    def run_time(self, run_time):
        """Sets the run_time of this AutomatedTestCaseRunResult.

        Optional runtime in seconds  # noqa: E501

        :param run_time: The run_time of this AutomatedTestCaseRunResult.  # noqa: E501
        :type: int
        """

        self._run_time = run_time

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
        if issubclass(AutomatedTestCaseRunResult, dict):
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
        if not isinstance(other, AutomatedTestCaseRunResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
