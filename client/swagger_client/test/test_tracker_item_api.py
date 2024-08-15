# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.tracker_item_api import TrackerItemApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTrackerItemApi(unittest.TestCase):
    """TrackerItemApi unit test stubs"""

    def setUp(self):
        self.api = TrackerItemApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_child_to_tracker(self):
        """Test case for add_child_to_tracker

        Add a child item to a tracker item  # noqa: E501
        """
        pass

    def test_add_child_to_tracker_item(self):
        """Test case for add_child_to_tracker_item

        Add a child item to a tracker item  # noqa: E501
        """
        pass

    def test_bulk_update_tracker_item_fields(self):
        """Test case for bulk_update_tracker_item_fields

        Bulk update fields of a tracker item  # noqa: E501
        """
        pass

    def test_check_tracker_item_lock(self):
        """Test case for check_tracker_item_lock

        Check whether a tracker item is locked, and if it is, retrieve the details of the lock  # noqa: E501
        """
        pass

    def test_create_tracker_item(self):
        """Test case for create_tracker_item

        Create a tracker item  # noqa: E501
        """
        pass

    def test_delete_tracker_item(self):
        """Test case for delete_tracker_item

        Move tracker item to trash  # noqa: E501
        """
        pass

    def test_find_tracker_children(self):
        """Test case for find_tracker_children

        Get child items of a tracker item  # noqa: E501
        """
        pass

    def test_find_tracker_item_children(self):
        """Test case for find_tracker_item_children

        Get child items of a tracker item  # noqa: E501
        """
        pass

    def test_find_tracker_items(self):
        """Test case for find_tracker_items

        Get tracker items by cbQL query string  # noqa: E501
        """
        pass

    def test_find_tracker_items_by_cb_ql(self):
        """Test case for find_tracker_items_by_cb_ql

        Get tracker items by cbQL query string  # noqa: E501
        """
        pass

    def test_get_baseline_tracker_item_relations(self):
        """Test case for get_baseline_tracker_item_relations

        Get tracker items related to a tracker item  # noqa: E501
        """
        pass

    def test_get_baseline_tracker_items_relations(self):
        """Test case for get_baseline_tracker_items_relations

        Get tracker items related to some tracker items  # noqa: E501
        """
        pass

    def test_get_choice_options(self):
        """Test case for get_choice_options

        Get the options of a choice field of tracker  # noqa: E501
        """
        pass

    def test_get_item_accessibility(self):
        """Test case for get_item_accessibility

        Get a tracker item fields accessibility  # noqa: E501
        """
        pass

    def test_get_tracker_item(self):
        """Test case for get_tracker_item

        Get basic tracker item  # noqa: E501
        """
        pass

    def test_get_tracker_item_fields(self):
        """Test case for get_tracker_item_fields

        Get fields of a tracker item  # noqa: E501
        """
        pass

    def test_get_tracker_item_history(self):
        """Test case for get_tracker_item_history

        Get tracker item history  # noqa: E501
        """
        pass

    def test_get_tracker_item_reviews(self):
        """Test case for get_tracker_item_reviews

        Get all Tracker Item Reviews for a particular Tracker Item  # noqa: E501
        """
        pass

    def test_get_tracker_item_transitions(self):
        """Test case for get_tracker_item_transitions

        Get available transitions for a tracker item  # noqa: E501
        """
        pass

    def test_lock_tracker_item(self):
        """Test case for lock_tracker_item

        Put a soft lock on a tracker item  # noqa: E501
        """
        pass

    def test_patch_children_of_tracker(self):
        """Test case for patch_children_of_tracker

        Patch the child item list of a tracker item  # noqa: E501
        """
        pass

    def test_patch_children_of_tracker_item(self):
        """Test case for patch_children_of_tracker_item

        Patch the child item list of a tracker item  # noqa: E501
        """
        pass

    def test_replace_children_of_tracker(self):
        """Test case for replace_children_of_tracker

        Reorder the child item list of a tracker  # noqa: E501
        """
        pass

    def test_replace_children_of_tracker_item(self):
        """Test case for replace_children_of_tracker_item

        Replace the child item list of a tracker item  # noqa: E501
        """
        pass

    def test_unlock_tracker_item(self):
        """Test case for unlock_tracker_item

        Unlock a tracker item  # noqa: E501
        """
        pass

    def test_update_custom_field_tracker_item(self):
        """Test case for update_custom_field_tracker_item

        Update fields of a tracker item  # noqa: E501
        """
        pass

    def test_update_table_field_tracker_item(self):
        """Test case for update_table_field_tracker_item

        Update table field of tracker item  # noqa: E501
        """
        pass

    def test_update_tracker_item(self):
        """Test case for update_tracker_item

        Update tracker item  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
