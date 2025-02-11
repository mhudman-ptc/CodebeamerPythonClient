# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.tracker_items_attachment_api import TrackerItemsAttachmentApi


class TestTrackerItemsAttachmentApi(unittest.TestCase):
    """TrackerItemsAttachmentApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TrackerItemsAttachmentApi()

    def tearDown(self) -> None:
        pass

    def test_delete_tracker_item_attachment(self) -> None:
        """Test case for delete_tracker_item_attachment

        Delete attachment of tracker item by id
        """
        pass

    def test_delete_tracker_item_attachments(self) -> None:
        """Test case for delete_tracker_item_attachments

        Delete attachments of tracker item
        """
        pass

    def test_get_tracker_item_attachment(self) -> None:
        """Test case for get_tracker_item_attachment

        Get attachment of tracker item by id
        """
        pass

    def test_get_tracker_item_attachment_content(self) -> None:
        """Test case for get_tracker_item_attachment_content

        Get content of an attachment of tracker item by id
        """
        pass

    def test_get_tracker_item_attachment_contents(self) -> None:
        """Test case for get_tracker_item_attachment_contents

        Get attachments of a tracker item
        """
        pass

    def test_get_tracker_item_attachments(self) -> None:
        """Test case for get_tracker_item_attachments

        Get attachments of tracker item
        """
        pass

    def test_get_tracker_items_attachment_contents(self) -> None:
        """Test case for get_tracker_items_attachment_contents

        Get attachments of tracker items matching the extension or mime type filters
        """
        pass

    def test_update_attachment_of_tracker_item(self) -> None:
        """Test case for update_attachment_of_tracker_item

        Update content of attachment of tracker item
        """
        pass

    def test_upload_tracker_item_attachment(self) -> None:
        """Test case for upload_tracker_item_attachment

        Upload an attachment to a tracker item
        """
        pass


if __name__ == '__main__':
    unittest.main()
