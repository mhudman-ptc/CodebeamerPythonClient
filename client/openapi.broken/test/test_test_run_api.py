# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.test_run_api import TestRunApi


class TestTestRunApi(unittest.TestCase):
    """TestRunApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TestRunApi()

    def tearDown(self) -> None:
        pass

    def test_create_test_run_for_test_case(self) -> None:
        """Test case for create_test_run_for_test_case

        Create a new test run for test cases or test sets
        """
        pass

    def test_create_test_run_for_test_sets(self) -> None:
        """Test case for create_test_run_for_test_sets

        Create a new test run for test cases or test sets
        """
        pass

    def test_update_test_run_result(self) -> None:
        """Test case for update_test_run_result

        Update result of a Test Run. 
        """
        pass

    def test_upload_automated_test_results(self) -> None:
        """Test case for upload_automated_test_results

        Create a new test run for large number of automated test cases
        """
        pass


if __name__ == '__main__':
    unittest.main()