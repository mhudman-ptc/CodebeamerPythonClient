# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.remote_migration_file import RemoteMigrationFile

class TestRemoteMigrationFile(unittest.TestCase):
    """RemoteMigrationFile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RemoteMigrationFile:
        """Test RemoteMigrationFile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RemoteMigrationFile`
        """
        model = RemoteMigrationFile()
        if include_optional:
            return RemoteMigrationFile(
                file_name = 'newFile.txt',
                file_path = 'folder/file.txt',
                md5sum = 'f6967f92c24a8f3c4849d30c9f17e321',
                sha512sum = '2e74ed4b0741e1fbe22d61e165c7c0dc4383a1aa5aa708291e32fff4cb189b9a5dfea7ffca2a22dcca258751cf4ad947c1c34abdf3fa2994219be394fbe40370'
            )
        else:
            return RemoteMigrationFile(
        )
        """

    def testRemoteMigrationFile(self):
        """Test RemoteMigrationFile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
