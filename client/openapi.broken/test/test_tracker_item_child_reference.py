# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tracker_item_child_reference import TrackerItemChildReference

class TestTrackerItemChildReference(unittest.TestCase):
    """TrackerItemChildReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrackerItemChildReference:
        """Test TrackerItemChildReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrackerItemChildReference`
        """
        model = TrackerItemChildReference()
        if include_optional:
            return TrackerItemChildReference(
                index = 0,
                item_reference = openapi_client.models.tracker_item_reference.TrackerItemReference()
            )
        else:
            return TrackerItemChildReference(
                index = 0,
                item_reference = openapi_client.models.tracker_item_reference.TrackerItemReference(),
        )
        """

    def testTrackerItemChildReference(self):
        """Test TrackerItemChildReference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()