# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.test_run_api import TestRunApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTestRunApi(unittest.TestCase):
    """TestRunApi unit test stubs"""

    def setUp(self):
        self.api = TestRunApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_test_run_for_test_case(self):
        """Test case for create_test_run_for_test_case

        Create a new test run for test cases or test sets  # noqa: E501
        """
        pass

    def test_create_test_run_for_test_sets(self):
        """Test case for create_test_run_for_test_sets

        Create a new test run for test cases or test sets  # noqa: E501
        """
        pass

    def test_update_test_run_result(self):
        """Test case for update_test_run_result

        Update result of a Test Run.   # noqa: E501
        """
        pass

    def test_upload_automated_test_results(self):
        """Test case for upload_automated_test_results

        Create a new test run for large number of automated test cases  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
