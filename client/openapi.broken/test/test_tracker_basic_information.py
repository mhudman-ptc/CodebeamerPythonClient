# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tracker_basic_information import TrackerBasicInformation

class TestTrackerBasicInformation(unittest.TestCase):
    """TrackerBasicInformation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrackerBasicInformation:
        """Test TrackerBasicInformation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrackerBasicInformation`
        """
        model = TrackerBasicInformation()
        if include_optional:
            return TrackerBasicInformation(
                always_use_quick_transitions = True,
                color = '',
                default_layout = 'TABLE',
                description = '',
                hidden = True,
                inbox_id = 56,
                issue_type_id = 56,
                key = '',
                name = '',
                only_workflow_actions_can_create_new_referring_items = True,
                project_id = 56,
                shared_in_working_sets = True,
                show_ancestor_items = True,
                show_descendant_items = True,
                template = True,
                template_id = 56,
                tracker_id = 56,
                workflow_is_active = True
            )
        else:
            return TrackerBasicInformation(
        )
        """

    def testTrackerBasicInformation(self):
        """Test TrackerBasicInformation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()