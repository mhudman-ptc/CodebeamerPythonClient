# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.attachment_migration_request import AttachmentMigrationRequest

class TestAttachmentMigrationRequest(unittest.TestCase):
    """AttachmentMigrationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttachmentMigrationRequest:
        """Test AttachmentMigrationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttachmentMigrationRequest`
        """
        model = AttachmentMigrationRequest()
        if include_optional:
            return AttachmentMigrationRequest(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = openapi_client.models.user_reference.UserReference(),
                description = '',
                description_format = 'PlainText',
                files = [
                    openapi_client.models.remote_migration_file.RemoteMigrationFile(
                        file_name = 'newFile.txt', 
                        file_path = 'folder/file.txt', 
                        md5sum = 'f6967f92c24a8f3c4849d30c9f17e321', 
                        sha512sum = '2e74ed4b0741e1fbe22d61e165c7c0dc4383a1aa5aa708291e32fff4cb189b9a5dfea7ffca2a22dcca258751cf4ad947c1c34abdf3fa2994219be394fbe40370', )
                    ],
                migration_action = 'MOVE',
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_by = openapi_client.models.user_reference.UserReference(),
                target_item = openapi_client.models.tracker_item_reference.TrackerItemReference()
            )
        else:
            return AttachmentMigrationRequest(
        )
        """

    def testAttachmentMigrationRequest(self):
        """Test AttachmentMigrationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()