# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.abstract_tracker_item_reference import AbstractTrackerItemReference

class TestAbstractTrackerItemReference(unittest.TestCase):
    """AbstractTrackerItemReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AbstractTrackerItemReference:
        """Test AbstractTrackerItemReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AbstractTrackerItemReference`
        """
        model = AbstractTrackerItemReference()
        if include_optional:
            return AbstractTrackerItemReference(
                id = 12142,
                item_revision = openapi_client.models.tracker_item_revision.TrackerItemRevision(
                    id = 56, 
                    version = 56, ),
                type = 'DownstreamTrackerItemReference'
            )
        else:
            return AbstractTrackerItemReference(
        )
        """

    def testAbstractTrackerItemReference(self):
        """Test AbstractTrackerItemReference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
