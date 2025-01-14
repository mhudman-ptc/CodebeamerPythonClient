# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.export_api import ExportApi


class TestExportApi(unittest.TestCase):
    """ExportApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ExportApi()

    def tearDown(self) -> None:
        pass

    def test_batch_get_tracker_item_reviews(self) -> None:
        """Test case for batch_get_tracker_item_reviews

        Get tracker item reviews by a list of tracker item IDs
        """
        pass

    def test_export(self) -> None:
        """Test case for export

        Exports the specified project to a zip file
        """
        pass

    def test_export_to_word(self) -> None:
        """Test case for export_to_word

        Exports items to Word
        """
        pass

    def test_get_tracker_items(self) -> None:
        """Test case for get_tracker_items

        Get tracker items
        """
        pass


if __name__ == '__main__':
    unittest.main()
