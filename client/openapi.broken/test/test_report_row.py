# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.report_row import ReportRow

class TestReportRow(unittest.TestCase):
    """ReportRow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReportRow:
        """Test ReportRow
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReportRow`
        """
        model = ReportRow()
        if include_optional:
            return ReportRow(
                cells = [
                    openapi_client.models.report_cell.ReportCell(
                        column_ref = '', 
                        value = 12.32, )
                    ],
                is_real_result = True,
                item_ref = openapi_client.models.report_item_reference.ReportItemReference(
                    item_id = 56, 
                    tracker_id = 56, ),
                outline_level = 56
            )
        else:
            return ReportRow(
        )
        """

    def testReportRow(self):
        """Test ReportRow"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
