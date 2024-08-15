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

class CreateTestRunFromTestSetsRequest(object):
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
        'run_only_accepted_test_cases': 'bool',
        'test_run_model': 'TrackerItem',
        'test_set_refs': 'list[TrackerItemReference]'
    }

    attribute_map = {
        'run_only_accepted_test_cases': 'runOnlyAcceptedTestCases',
        'test_run_model': 'testRunModel',
        'test_set_refs': 'testSetRefs'
    }

    def __init__(self, run_only_accepted_test_cases=False, test_run_model=None, test_set_refs=None):  # noqa: E501
        """CreateTestRunFromTestSetsRequest - a model defined in Swagger"""  # noqa: E501
        self._run_only_accepted_test_cases = None
        self._test_run_model = None
        self._test_set_refs = None
        self.discriminator = None
        if run_only_accepted_test_cases is not None:
            self.run_only_accepted_test_cases = run_only_accepted_test_cases
        if test_run_model is not None:
            self.test_run_model = test_run_model
        if test_set_refs is not None:
            self.test_set_refs = test_set_refs

    @property
    def run_only_accepted_test_cases(self):
        """Gets the run_only_accepted_test_cases of this CreateTestRunFromTestSetsRequest.  # noqa: E501

        Generate Test Runs only from accepted Test Cases.  # noqa: E501

        :return: The run_only_accepted_test_cases of this CreateTestRunFromTestSetsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._run_only_accepted_test_cases

    @run_only_accepted_test_cases.setter
    def run_only_accepted_test_cases(self, run_only_accepted_test_cases):
        """Sets the run_only_accepted_test_cases of this CreateTestRunFromTestSetsRequest.

        Generate Test Runs only from accepted Test Cases.  # noqa: E501

        :param run_only_accepted_test_cases: The run_only_accepted_test_cases of this CreateTestRunFromTestSetsRequest.  # noqa: E501
        :type: bool
        """

        self._run_only_accepted_test_cases = run_only_accepted_test_cases

    @property
    def test_run_model(self):
        """Gets the test_run_model of this CreateTestRunFromTestSetsRequest.  # noqa: E501


        :return: The test_run_model of this CreateTestRunFromTestSetsRequest.  # noqa: E501
        :rtype: TrackerItem
        """
        return self._test_run_model

    @test_run_model.setter
    def test_run_model(self, test_run_model):
        """Sets the test_run_model of this CreateTestRunFromTestSetsRequest.


        :param test_run_model: The test_run_model of this CreateTestRunFromTestSetsRequest.  # noqa: E501
        :type: TrackerItem
        """

        self._test_run_model = test_run_model

    @property
    def test_set_refs(self):
        """Gets the test_set_refs of this CreateTestRunFromTestSetsRequest.  # noqa: E501

        Test set ids to include into the test run. Only the first test set will be considered.  # noqa: E501

        :return: The test_set_refs of this CreateTestRunFromTestSetsRequest.  # noqa: E501
        :rtype: list[TrackerItemReference]
        """
        return self._test_set_refs

    @test_set_refs.setter
    def test_set_refs(self, test_set_refs):
        """Sets the test_set_refs of this CreateTestRunFromTestSetsRequest.

        Test set ids to include into the test run. Only the first test set will be considered.  # noqa: E501

        :param test_set_refs: The test_set_refs of this CreateTestRunFromTestSetsRequest.  # noqa: E501
        :type: list[TrackerItemReference]
        """

        self._test_set_refs = test_set_refs

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
        if issubclass(CreateTestRunFromTestSetsRequest, dict):
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
        if not isinstance(other, CreateTestRunFromTestSetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
