# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tracker_item_choice_field import TrackerItemChoiceField

class TestTrackerItemChoiceField(unittest.TestCase):
    """TrackerItemChoiceField unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrackerItemChoiceField:
        """Test TrackerItemChoiceField
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrackerItemChoiceField`
        """
        model = TrackerItemChoiceField()
        if include_optional:
            return TrackerItemChoiceField(
                multiple_values = True,
                reference_type = ''
            )
        else:
            return TrackerItemChoiceField(
        )
        """

    def testTrackerItemChoiceField(self):
        """Test TrackerItemChoiceField"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()