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
from swagger_client.api.working_set_api import WorkingSetApi  # noqa: E501
from swagger_client.rest import ApiException


class TestWorkingSetApi(unittest.TestCase):
    """WorkingSetApi unit test stubs"""

    def setUp(self):
        self.api = WorkingSetApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_items_mapping_in_working_set(self):
        """Test case for get_items_mapping_in_working_set

        Maps Tracker Items in Working-Set  # noqa: E501
        """
        pass

    def test_get_tracker_working_sets(self):
        """Test case for get_tracker_working_sets

        Lists Working-Sets  # noqa: E501
        """
        pass

    def test_get_working_set_information(self):
        """Test case for get_working_set_information

        Working-Set information  # noqa: E501
        """
        pass

    def test_get_working_set_trackers(self):
        """Test case for get_working_set_trackers

         Lists the trackers in a Working-Set  # noqa: E501
        """
        pass

    def test_list_working_sets_of_project(self):
        """Test case for list_working_sets_of_project

        Project level Working-Sets information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()