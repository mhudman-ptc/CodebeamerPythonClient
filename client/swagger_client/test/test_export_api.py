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
from swagger_client.api.export_api import ExportApi  # noqa: E501
from swagger_client.rest import ApiException


class TestExportApi(unittest.TestCase):
    """ExportApi unit test stubs"""

    def setUp(self):
        self.api = ExportApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_batch_get_tracker_item_reviews(self):
        """Test case for batch_get_tracker_item_reviews

        Get tracker item reviews by a list of tracker item IDs  # noqa: E501
        """
        pass

    def test_export(self):
        """Test case for export

        Exports the specified project to a zip file  # noqa: E501
        """
        pass

    def test_export_to_word(self):
        """Test case for export_to_word

        Exports items to Word  # noqa: E501
        """
        pass

    def test_get_tracker_items(self):
        """Test case for get_tracker_items

        Get tracker items  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
