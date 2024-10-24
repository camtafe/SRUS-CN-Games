import unittest
from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player import Player


class TestList(unittest.TestCase):
    def setUp(self):
        """
        Creates a common test data format for all the player list tests
        Ensures each test has a fresh PlayerList and PlayerNode instances while reducing repetition
        """
        self.test_list = PlayerList()
        first_player = Player("000513", "Mark")
        second_player = Player("000232", "Eugene")
        third_player = Player("000747", "Darius")
        self.first_node = PlayerNode(first_player)
        self.second_node = PlayerNode(second_player)
        self.third_node = PlayerNode(third_player)

    def test_empty_list_with_no_insertions(self):
        self.assertTrue(self.test_list.is_empty())

    def test_removal_empty_is_none(self):
        result = self.test_list.delete_from_head()
        self.assertIsNone(result)

    def test_head_insert_list_isnt_empty(self):
        self.test_list.insert_at_head(self.first_node)
        self.assertFalse(self.test_list.is_empty())

    def test_tail_insert_list_isnt_empty(self):
        self.test_list.insert_at_tail(self.first_node)
        self.assertFalse(self.test_list.is_empty())

    def test_head_delete_single_is_empty(self):
        self.test_list.insert_at_head(self.first_node)
        self.test_list.delete_from_head()
        self.assertTrue(self.test_list.is_empty())

    def test_tail_delete_single_is_empty(self):
        self.test_list.insert_at_tail(self.first_node)
        self.test_list.delete_from_head()
        # check list is empty
        self.assertTrue(self.test_list.is_empty())

    def test_head_delete_multiple(self):
        """
        creates and archives an old and new head to compare to each other
        for the sake of proving the head has changed via deleting through the use of the
        deleting the head in a multinode situation
        """
        self.test_list.insert_at_head(self.first_node)
        self.test_list.insert_at_head(self.second_node)

        old_head = self.test_list.get_head()
        self.test_list.delete_from_head()
        new_head = self.test_list.get_head()

        self.assertFalse(self.test_list.is_empty())
        self.assertEqual(new_head, self.first_node)
        self.assertNotEqual(new_head, old_head)


    def test_tail_delete_multiple_via_tail(self):
        self.test_list.insert_at_tail(self.first_node)
        self.test_list.insert_at_tail(self.second_node)

        old_tail = self.test_list.get_tail()
        self.test_list.delete_from_tail()
        new_tail = self.test_list.get_tail()

        self.assertFalse(self.test_list.is_empty())
        self.assertEqual(new_tail, self.first_node)
        self.assertNotEqual(new_tail, old_tail)

    def test_delete_node_via_key_multiple(self):
        """
        testing the same situation as prior but using the delete key method
        """
        self.test_list.insert_at_tail(self.first_node)
        self.test_list.insert_at_tail(self.second_node)
        old_tail = self.test_list.get_tail()
        self.test_list.delete_via_key("000232")
        new_tail = self.test_list.get_tail()
        self.assertFalse(self.test_list.is_empty())
        self.assertEqual(new_tail, self.first_node)
        self.assertNotEqual(new_tail, old_tail)

    def test_delete_node_via_key_single(self):
        self.test_list.insert_at_tail(self.first_node)
        self.test_list.delete_via_key("000513")
        self.assertTrue(self.test_list.is_empty())

    def test_display_string_test_multiple_insertions(self):
        """
        Tests that the insertions of the nodes in order are displayed correctly when ordered from
        Head to Tail or Tail to Head based on the display_lists() method
        """
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
