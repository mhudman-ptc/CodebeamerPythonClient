# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.choice_options import ChoiceOptions

class TestChoiceOptions(unittest.TestCase):
    """ChoiceOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChoiceOptions:
        """Test ChoiceOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChoiceOptions`
        """
        model = ChoiceOptions()
        if include_optional:
            return ChoiceOptions(
                choice_options = [
                    openapi_client.models.choice_options/choice_option.ChoiceOptions.ChoiceOption(
                        color = '', 
                        default_in_statuses = [
                            56
                            ], 
                        description = '', 
                        id = 56, 
                        meanings = [
                            'OBSOLETE'
                            ], 
                        name = '', 
                        restricted_to_statuses = [
                            56
                            ], )
                    ]
            )
        else:
            return ChoiceOptions(
        )
        """

    def testChoiceOptions(self):
        """Test ChoiceOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
