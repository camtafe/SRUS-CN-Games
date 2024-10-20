import unittest
from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player import Player


class TestList(unittest.TestCase):
    def setUp(self):
        self.test_list = PlayerList()
        first_player = Player("000513", "Mark")
        second_player = Player("000232", "Eugene")
        third_player = Player("000747", "Darius")
        self.first_node = PlayerNode(first_player)
        self.second_node = PlayerNode(second_player)
        self.third_node = PlayerNode(third_player)

    def test_empty_list(self):
        self.assertTrue(self.test_list.is_empty())

    def test_removal_empty(self):
        empty_list = PlayerList()
        result = empty_list.delete_from_head()
        self.assertIsNone(result)

    def test_head_insert_list(self):
        self.test_list.insert_at_head(self.first_node)
        self.assertFalse(self.test_list.is_empty())

    def test_tail_insert_list(self):
        self.test_list.insert_at_tail(self.first_node)
        self.assertFalse(self.test_list.is_empty())

    def test_head_delete_single(self):
        self.test_list.insert_at_head(self.first_node)
        self.test_list.delete_from_head()
        self.assertTrue(self.test_list.is_empty())

    def test_head_delete_multiple(self):
        self.test_list.insert_at_head(self.first_node)
        self.test_list.insert_at_head(self.second_node)
        old_head = self.test_list.get_head()
        self.test_list.delete_from_head()
        new_head = self.test_list.get_head()
        self.assertFalse(self.test_list.is_empty())
        self.assertEqual(new_head, self.first_node)
        self.assertNotEqual(new_head, old_head)

    def test_tail_delete_single(self):
        self.test_list.insert_at_tail(self.first_node)
        self.test_list.delete_from_head()
        # check list is empty
        self.assertTrue(self.test_list.is_empty())

    def test_tail_delete_multiple_via_tail(self):
        self.test_list.insert_at_tail(self.first_node)
        self.test_list.insert_at_tail(self.second_node)
        # archive the old tail for test purposes
        old_tail = self.test_list.get_tail()
        # remove the tail node
        self.test_list.delete_from_tail()
        # archive the new tail to compare to confirm change
        new_tail = self.test_list.get_tail()
        self.assertFalse(self.test_list.is_empty())
        self.assertEqual(new_tail, self.first_node)
        self.assertNotEqual(new_tail, old_tail)

    def test_delete_node_via_key_multiple(self):
        self.test_list.insert_at_tail(self.first_node)
        self.test_list.insert_at_tail(self.second_node)
        # archive the old tail
        old_tail = self.test_list.get_tail()
        # remove the tail node
        self.test_list.delete_via_key("000232")
        # archive the new tail to compare to old tail
        new_tail = self.test_list.get_tail()
        self.assertFalse(self.test_list.is_empty())
        self.assertEqual(new_tail, self.first_node)
        self.assertNotEqual(new_tail, old_tail)

    def test_delete_node_via_key_single(self):
        self.test_list.insert_at_tail(self.first_node)
        # delete via player key
        self.test_list.delete_via_key("000513")
        # check list is empty
        self.assertTrue(self.test_list.is_empty())

    def test_display_string_test_multiple_insertions(self):
        self.test_list.insert_at_head(self.first_node)
        self.test_list.insert_at_head(self.second_node)
        self.test_list.insert_at_tail(self.third_node)

        expected_forward_string = """Lists:
-> Head  Name: Eugene | User ID: 000232
->  Name: Mark | User ID: 000513
-> Tail  Name: Darius | User ID: 000747
"""
        expected_backward_string = """Lists:
-> Tail  Name: Darius | User ID: 000747
->  Name: Mark | User ID: 000513
-> Head  Name: Eugene | User ID: 000232
"""

        print(self.test_list.display_lists(forward=False))
        self.assertMultiLineEqual(self.test_list.display_lists(), expected_forward_string)
        self.assertMultiLineEqual(str(self.test_list.display_lists(forward=False)), expected_backward_string)

    def test_display_text_unfilled_list_empty(self):
        expected_string = "Lists:\nEmpty"
        self.assertMultiLineEqual(str(self.test_list.display_lists()), expected_string)
