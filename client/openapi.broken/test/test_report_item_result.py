# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.report_item_result import ReportItemResult

class TestReportItemResult(unittest.TestCase):
    """ReportItemResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReportItemResult:
        """Test ReportItemResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReportItemResult`
        """
        model = ReportItemResult()
        if include_optional:
            return ReportItemResult(
                items = [
                    openapi_client.models.report_item.ReportItem(
                        is_real_result = True, 
                        item = openapi_client.models.tracker_item.TrackerItem(
                            accrued_millis = 56, 
                            areas = [
                                openapi_client.models.abstract_reference.AbstractReference(
                                    id = 0, 
                                    name = '', )
                                ], 
                            assigned_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            assigned_to = [
                                openapi_client.models.abstract_reference.AbstractReference(
                                    id = 0, 
                                    name = '', )
                                ], 
                            categories = [
                                
                                ], 
                            children = [
                                openapi_client.models.tracker_item_reference.TrackerItemReference()
                                ], 
                            closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            comments = [
                                openapi_client.models.comment_reference.CommentReference()
                                ], 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            created_by = openapi_client.models.user_reference.UserReference(), 
                            custom_fields = [
                                openapi_client.models.abstract_field_value.AbstractFieldValue(
                                    field_id = 56, 
                                    name = '', 
                                    shared_field_name = '', 
                                    shared_field_names = [
                                        ''
                                        ], 
                                    type = '', )
                                ], 
                            description = '', 
                            description_format = 'PlainText', 
                            end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            estimated_millis = 56, 
                            formality = , 
                            id = 0, 
                            modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            modified_by = openapi_client.models.user_reference.UserReference(), 
                            name = '', 
                            ordinal = 56, 
                            owners = [
                                
                                ], 
                            parent = openapi_client.models.tracker_item_reference.TrackerItemReference(), 
                            platforms = [
                                
                                ], 
                            priority = , 
                            release_method = , 
                            resolutions = [
                                
                                ], 
                            severities = [
                                
                                ], 
                            spent_millis = 56, 
                            start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            status = , 
                            story_points = 56, 
                            subjects = [
                                
                                ], 
                            tags = [
                                openapi_client.models.label.Label(
                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    hidden = True, 
                                    id = 0, 
                                    name = '', 
                                    private_label = True, )
                                ], 
                            teams = [
                                
                                ], 
                            tracker = openapi_client.models.tracker_reference.TrackerReference(), 
                            type_name = '', 
                            version = 56, 
                            versions = [
                                
                                ], ), 
                        outline_level = 56, )
                    ],
                page = 56,
                page_size = 56,
                total = 56
            )
        else:
            return ReportItemResult(
        )
        """

    def testReportItemResult(self):
        """Test ReportItemResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
