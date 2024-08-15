# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tracker_item_search_request import TrackerItemSearchRequest

class TestTrackerItemSearchRequest(unittest.TestCase):
    """TrackerItemSearchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrackerItemSearchRequest:
        """Test TrackerItemSearchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrackerItemSearchRequest`
        """
        model = TrackerItemSearchRequest()
        if include_optional:
            return TrackerItemSearchRequest(
                baseline_id = 1234,
                page = 1,
                page_size = 25,
                query_string = 'priority='Normal''
            )
        else:
            return TrackerItemSearchRequest(
                query_string = 'priority='Normal'',
        )
        """

    def testTrackerItemSearchRequest(self):
        """Test TrackerItemSearchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()