import unittest
from player_list import PlayerList
from player_node import PlayerNode
from player import Player


first_player = Player("000513", "Mark")
second_player = Player("000232", "Eugene")


class TestList(unittest.TestCase):
    def setUp(self):
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
        # create a test node using the test player
        dummy_node = PlayerNode(first_player)
        # insert the test node at the head of the list
        self.test_list.insert_at_head(dummy_node)
        # remove the inserted node from the list
        self.test_list.delete_from_head()
        # check the list is empty post removal
        self.assertTrue(self.test_list.is_empty())

    def test_head_delete_multiple(self):
        # prepare scenario with two nodes via head insertion
        first_node = PlayerNode(first_player)
        second_node = PlayerNode(second_player)
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
        # create test scenario
        dummy_node = PlayerNode(first_player)
        # insert tail end node
        self.test_list.insert_at_tail(dummy_node)
        self.test_list.delete_from_head()
        # check list is empty
        self.assertTrue(self.test_list.is_empty())

    def test_tail_delete_multiple(self):
        # prepare scenario with two nodes via tail insertion
        first_node = PlayerNode(first_player)
        second_node = PlayerNode(second_player)
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
        # prepare scenario with two nodes via tail insertion
        first_node = PlayerNode(first_player)
        second_node = PlayerNode(second_player)
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
        # create test scenario
        dummy_node = PlayerNode(first_player)
        # insert tail end node
        self.test_list.insert_at_tail(dummy_node)
        # delete via player key
        self.test_list.delete_via_key("000513")
        # check list is empty
        self.assertTrue(self.test_list.is_empty())

    def display_test(self):
        # prepare scenario with two nodes put in via head insertion
        first_node = PlayerNode(first_player)
        second_node = PlayerNode(second_player)
        self.test_list.insert_at_head(first_node)
        self.test_list.insert_at_head(second_node)
        # display the lists using both possible functionalities
        # true = forwards from head, tail = backwards from tail
        self.test_list.display_lists()
        self.test_list.display_lists(forward=False)
