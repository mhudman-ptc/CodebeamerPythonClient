# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.automated_test_case_run_result import AutomatedTestCaseRunResult

class TestAutomatedTestCaseRunResult(unittest.TestCase):
    """AutomatedTestCaseRunResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AutomatedTestCaseRunResult:
        """Test AutomatedTestCaseRunResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AutomatedTestCaseRunResult`
        """
        model = AutomatedTestCaseRunResult()
        if include_optional:
            return AutomatedTestCaseRunResult(
                conclusion = '',
                description = '',
                group_name = '',
                name = '',
                result = 'PASSED',
                run_time = 56
            )
        else:
            return AutomatedTestCaseRunResult(
                name = '',
                result = 'PASSED',
        )
        """

    def testAutomatedTestCaseRunResult(self):
        """Test AutomatedTestCaseRunResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
