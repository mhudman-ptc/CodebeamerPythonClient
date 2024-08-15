# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.tracker_items_comment_api import TrackerItemsCommentApi


class TestTrackerItemsCommentApi(unittest.TestCase):
    """TrackerItemsCommentApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TrackerItemsCommentApi()

    def tearDown(self) -> None:
        pass

    def test_comment_on_tracker_item(self) -> None:
        """Test case for comment_on_tracker_item

        Comment on a tracker item
        """
        pass

    def test_delete_tracker_item_comment(self) -> None:
        """Test case for delete_tracker_item_comment

        Delete comment of tracker item by id
        """
        pass

    def test_delete_tracker_item_comments(self) -> None:
        """Test case for delete_tracker_item_comments

        Delete comments of tracker item by item id
        """
        pass

    def test_edit_comment_on_tracker_item(self) -> None:
        """Test case for edit_comment_on_tracker_item

        Edit comment on a tracker item
        """
        pass

    def test_get_tracker_item_comment(self) -> None:
        """Test case for get_tracker_item_comment

        Get comment of tracker item by id
        """
        pass

    def test_get_tracker_item_comments(self) -> None:
        """Test case for get_tracker_item_comments

        Get comments of tracker item
        """
        pass

    def test_reply_on_comment_of_tracker_item(self) -> None:
        """Test case for reply_on_comment_of_tracker_item

        Reply on a comment of a tracker item
        """
        pass


if __name__ == '__main__':
    unittest.main()
