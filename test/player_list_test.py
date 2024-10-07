import unittest
from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player import Player

# dummy/test players and nodes for redundancy purposes
first_player = Player("000513", "Mark")
second_player = Player("000232", "Eugene")
third_player = Player("000747", "Darius")
first_node = PlayerNode(first_player)
second_node = PlayerNode(second_player)
third_node = PlayerNode(third_player)


class TestList(unittest.TestCase):
    def setUp(self):
        # creates a test_list variable that can be used in multiple test cases
        # for redundancy purposes
        self.test_list = PlayerList()

    def test_empty_list(self):
        self.assertTrue(self.test_list.is_empty())

    def test_removal_empty(self):
        empty_list = PlayerList()
        result = empty_list.delete_from_head()
        self.assertIsNone(result)

    def test_head_insert_list(self):
        node = PlayerNode(first_player)
        self.test_list.insert_at_head(node)
        self.assertFalse(self.test_list.is_empty())

    def test_tail_insert_list(self):
        node = PlayerNode(first_player)
        self.test_list.insert_at_tail(node)
        self.assertFalse(self.test_list.is_empty())

    def test_head_delete_single(self):
        # insert the test node at the head of the list
        self.test_list.insert_at_head(first_node)
        # remove the inserted node from the list
        self.test_list.delete_from_head()
        # check the list is empty post removal
        self.assertTrue(self.test_list.is_empty())

    def test_head_delete_multiple(self):
        # prepare scenario with two nodes via head insertion
        self.test_list.insert_at_head(first_node)
        self.test_list.insert_at_head(second_node)
        # archive the old head
        old_head = self.test_list.get_head()
        # remove the head node
        self.test_list.delete_from_head()
        # archive the new head
        new_head = self.test_list.get_head()
        self.assertFalse(self.test_list.is_empty())
        self.assertEqual(new_head, first_node)
        self.assertNotEqual(new_head, old_head)

    def test_tail_delete_single(self):
        # insert tail end node
        self.test_list.insert_at_tail(first_node)
        self.test_list.delete_from_head()
        # check list is empty
        self.assertTrue(self.test_list.is_empty())

    def test_tail_delete_multiple(self):
        # prepare scenario with two nodes via tail insertion
        self.test_list.insert_at_tail(first_node)
        self.test_list.insert_at_tail(second_node)
        # archive the old tail
        old_tail = self.test_list.get_tail()
        # remove the tail node
        self.test_list.delete_from_tail()
        # archive the new tail
        new_tail = self.test_list.get_tail()
        self.assertFalse(self.test_list.is_empty())
        self.assertEqual(new_tail, first_node)
        self.assertNotEqual(new_tail, old_tail)

    def test_delete_node_via_key_multiple(self):
        self.test_list.insert_at_tail(first_node)
        self.test_list.insert_at_tail(second_node)
        # archive the old tail
        old_tail = self.test_list.get_tail()
        # remove the tail node
        self.test_list.delete_via_key("000232")
        # archive the new tail
        new_tail = self.test_list.get_tail()
        self.assertFalse(self.test_list.is_empty())
        self.assertEqual(new_tail, first_node)
        self.assertNotEqual(new_tail, old_tail)

    def test_delete_node_via_key_single(self):
        # insert tail end node
        self.test_list.insert_at_tail(first_node)
        # delete via player key
        self.test_list.delete_via_key("000513")
        # check list is empty
        self.assertTrue(self.test_list.is_empty())

    def test_display_test_multiple(self):
        # prepare scenario with two nodes put in via head insertion
        self.test_list.insert_at_head(first_node)
        self.test_list.insert_at_head(second_node)
        self.test_list.insert_at_tail(third_node)

        #create expected string
        expected_forward_string = """Lists:
-> Head  Name: Eugene | User ID: 000232
-> Name: Mark | User ID: 000513
-> Tail  Name: Darius | User ID: 000747

    """
        expected_backward_string = """Lists:
-> Tail Name: Darius | User ID: 000747
-> Name: Eugene | User ID: 000232
-> Head Name: Mark | User ID: 000513
    
    """

        print(self.test_list.display_lists(forward=False))
        self.assertMultiLineEqual(self.test_list.display_lists(), expected_forward_string)
        self.assertMultiLineEqual(str(self.test_list.display_lists(forward=False)), expected_backward_string)

    def test_display_list_empty(self):
        expected_string = "Lists:\nEmpty"

        self.assertMultiLineEqual(str(self.test_list.display_lists()), expected_string)
