# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tracker_item_review_export import TrackerItemReviewExport

class TestTrackerItemReviewExport(unittest.TestCase):
    """TrackerItemReviewExport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrackerItemReviewExport:
        """Test TrackerItemReviewExport
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrackerItemReviewExport`
        """
        model = TrackerItemReviewExport()
        if include_optional:
            return TrackerItemReviewExport(
                reviewers = [
                    openapi_client.models.tracker_item_review_vote_export.TrackerItemReviewVoteExport(
                        decision = '', 
                        first_name = '', 
                        last_name = '', 
                        reviewed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        role_name = '', 
                        user_name = '', )
                    ],
                tracker_item_version = 56
            )
        else:
            return TrackerItemReviewExport(
        )
        """

    def testTrackerItemReviewExport(self):
        """Test TrackerItemReviewExport"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
