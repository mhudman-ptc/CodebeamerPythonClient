# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.report_reference_level import ReportReferenceLevel

class TestReportReferenceLevel(unittest.TestCase):
    """ReportReferenceLevel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReportReferenceLevel:
        """Test ReportReferenceLevel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReportReferenceLevel`
        """
        model = ReportReferenceLevel()
        if include_optional:
            return ReportReferenceLevel(
                columns = [
                    openapi_client.models.report_column.ReportColumn(
                        column_index = 0, 
                        column_ref = '12-1', 
                        column_width_percentage = 16.533667, 
                        field = openapi_client.models.field_reference.FieldReference(), 
                        name = 'Status', 
                        type = 'choice', )
                    ],
                downstream_reference_rows = [
                    openapi_client.models.report_referenced_row.ReportReferencedRow()
                    ],
                reference_level = 1,
                upstream_reference_rows = [
                    openapi_client.models.report_referenced_row.ReportReferencedRow()
                    ]
            )
        else:
            return ReportReferenceLevel(
        )
        """

    def testReportReferenceLevel(self):
        """Test ReportReferenceLevel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
