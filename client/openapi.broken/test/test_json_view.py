# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.json_view import JsonView

class TestJsonView(unittest.TestCase):
    """JsonView unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonView:
        """Test JsonView
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonView`
        """
        model = JsonView()
        if include_optional:
            return JsonView(
                content_type = '',
                var_json = '',
                json_object = openapi_client.models.json_view.JsonView(
                    content_type = '', 
                    json = '', 
                    json_object = openapi_client.models.json_view.JsonView(
                        content_type = '', 
                        json = '', ), )
            )
        else:
            return JsonView(
        )
        """

    def testJsonView(self):
        """Test JsonView"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
