# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.batch_get_tracker_item_reviews_request import BatchGetTrackerItemReviewsRequest

class TestBatchGetTrackerItemReviewsRequest(unittest.TestCase):
    """BatchGetTrackerItemReviewsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BatchGetTrackerItemReviewsRequest:
        """Test BatchGetTrackerItemReviewsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BatchGetTrackerItemReviewsRequest`
        """
        model = BatchGetTrackerItemReviewsRequest()
        if include_optional:
            return BatchGetTrackerItemReviewsRequest(
                baseline_id = 56,
                item_ids = [
                    56
                    ]
            )
        else:
            return BatchGetTrackerItemReviewsRequest(
        )
        """

    def testBatchGetTrackerItemReviewsRequest(self):
        """Test BatchGetTrackerItemReviewsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
