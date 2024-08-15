# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.outline_item_search_result import OutlineItemSearchResult

class TestOutlineItemSearchResult(unittest.TestCase):
    """OutlineItemSearchResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OutlineItemSearchResult:
        """Test OutlineItemSearchResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OutlineItemSearchResult`
        """
        model = OutlineItemSearchResult()
        if include_optional:
            return OutlineItemSearchResult(
                outline_items = [
                    openapi_client.models.outline_item.OutlineItem()
                    ],
                page = 56,
                page_size = 56,
                total = 56
            )
        else:
            return OutlineItemSearchResult(
        )
        """

    def testOutlineItemSearchResult(self):
        """Test OutlineItemSearchResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
