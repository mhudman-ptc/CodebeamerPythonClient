# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tracker_configuration import TrackerConfiguration

class TestTrackerConfiguration(unittest.TestCase):
    """TrackerConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrackerConfiguration:
        """Test TrackerConfiguration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrackerConfiguration`
        """
        model = TrackerConfiguration()
        if include_optional:
            return TrackerConfiguration(
                basic_information = openapi_client.models.tracker_basic_information.TrackerBasicInformation(
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
                    workflow_is_active = True, ),
                fields = [
                    openapi_client.models.tracker_field.TrackerField(
                        aggregation_rule = 'MINIMUM', 
                        choice_option_setting = openapi_client.models.base_tracker_field_choice_option.BaseTrackerFieldChoiceOption(
                            type = '', ), 
                        computed_as = '', 
                        computed_field_references = [
                            openapi_client.models.tracker_field/computed_field_reference.TrackerField.ComputedFieldReference(
                                referred_field_id = 56, 
                                referred_field_tracker_id = 56, 
                                referred_tracker_id = 56, )
                            ], 
                        date_field_settings = openapi_client.models.tracker_field/date_field_settings.TrackerField.DateFieldSettings(
                            display_day = True, 
                            display_month = True, 
                            display_time = True, 
                            display_year = True, ), 
                        default_values_in_statuses = {
                            'key' : ''
                            }, 
                        dependency = openapi_client.models.tracker_field_dependency.TrackerFieldDependency(
                            dependent_field_id = 56, 
                            value_combinations = {
                                'key' : ''
                                }, ), 
                        description = '', 
                        digits = 56, 
                        distribution_rule = 'SET', 
                        global_type_ids = [
                            56
                            ], 
                        height = 56, 
                        hidden = True, 
                        hide_if_formula = '', 
                        hide_if_formula_same_as_field_id = 56, 
                        label = '', 
                        listable = True, 
                        mandatory = True, 
                        mandatory_if_formula = '', 
                        mandatory_if_formula_same_as_field_id = 56, 
                        max_value = '', 
                        min_value = '', 
                        multiple_selection = True, 
                        new_line = True, 
                        omit_merge = True, 
                        omit_suspected_when_change = True, 
                        permission = openapi_client.models.base_tracker_field_permission.BaseTrackerFieldPermission(
                            type = '', ), 
                        position = 56, 
                        propagate_dependencies = True, 
                        propagate_suspect = True, 
                        reference_id = 56, 
                        reversed_suspect = True, 
                        service_desk_field = openapi_client.models.tracker_field/service_desk_field.TrackerField.ServiceDeskField(
                            description = '', 
                            label = '', ), 
                        span = 56, 
                        title = '', 
                        type_id = 56, 
                        union = True, 
                        width = 56, )
                    ]
            )
        else:
            return TrackerConfiguration(
        )
        """

    def testTrackerConfiguration(self):
        """Test TrackerConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
