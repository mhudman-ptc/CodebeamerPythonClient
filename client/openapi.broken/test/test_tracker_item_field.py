# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tracker_item_field import TrackerItemField

class TestTrackerItemField(unittest.TestCase):
    """TrackerItemField unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrackerItemField:
        """Test TrackerItemField
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrackerItemField`
        """
        model = TrackerItemField()
        if include_optional:
            return TrackerItemField(
                editable_fields = [
                    openapi_client.models.abstract_field_value.AbstractFieldValue(
                        field_id = 56, 
                        name = '', 
                        shared_field_name = '', 
                        shared_field_names = [
                            ''
                            ], 
                        type = '', )
                    ],
                editable_table_fields = [
                    openapi_client.models.table_field_value.TableFieldValue()
                    ],
                read_only_fields = [
                    openapi_client.models.abstract_field_value.AbstractFieldValue(
                        field_id = 56, 
                        name = '', 
                        shared_field_name = '', 
                        shared_field_names = [
                            ''
                            ], 
                        type = '', )
                    ],
                read_only_table_fields = [
                    openapi_client.models.table_field_value.TableFieldValue()
                    ]
            )
        else:
            return TrackerItemField(
        )
        """

    def testTrackerItemField(self):
        """Test TrackerItemField"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
