import unittest
from player_list import PlayerList
from player_node import PlayerNode
from player import Player


class TestList(unittest.TestCase):
    def test_empty_list(self):
        empty_list = PlayerList()
        self.assertTrue(empty_list.is_empty())

    def test_removal_empty(self):
        empty_list = PlayerList()
        result = empty_list.delete_from_head()
        self.assertIsNone(result)

    def test_head_insert_list(self):
        test_list = PlayerList()
        dummy_player = Player("000513", "Mark")
        node = PlayerNode(dummy_player)
        test_list.insert_at_head(node)
        self.assertFalse(test_list.is_empty())

    def test_tail_insert_list(self):
        test_list = PlayerList()
        dummy_player = Player("000513", "Mark")
        node = PlayerNode(dummy_player)
        test_list.insert_at_tail(node)
        self.assertFalse(test_list.is_empty())

    def test_head_delete_single(self):
        # create a list
        test_list = PlayerList()
        # create a test player
        dummy_player = Player("000513", "Mark")
        # create a test node using the test player
        dummy_node = PlayerNode(dummy_player)
        # insert the test node at the head of the list
        test_list.insert_at_head(dummy_node)
        # remove the inserted node from the list
        test_list.delete_from_head()
        # makes sure the list is empty post removal
        self.assertTrue(test_list.is_empty())

    def test_head_delete_multiple(self):
        # prepare scenario with two nodes put in via head insertion
        test_list = PlayerList()
        first_player = Player("000513", "Mark")
        second_player = Player("000232", "Eugene")
        first_node = PlayerNode(first_player)
        second_node = PlayerNode(second_player)
        test_list.insert_at_head(first_node)
        test_list.insert_at_head(second_node)
        # archive the old head
        old_head = test_list.get_head()
        # remove the head node
        test_list.delete_from_head()
        # archive the new head
        new_head = test_list.get_head()
        self.assertFalse(test_list.is_empty())
        self.assertEqual(new_head, first_node)
        self.assertNotEqual(new_head, old_head)

    def test_tail_delete_single(self):
        # create test scenario
        test_list = PlayerList()
        dummy_player = Player("000513", "Mark")
        dummy_node = PlayerNode(dummy_player)
        # insert tail end node
        test_list.insert_at_tail(dummy_node)
        test_list.delete_from_head()
        self.assertTrue(test_list.is_empty())

    def test_tail_delete_multiple(self):
        # prepare scenario with two nodes put in via tail insertion
        test_list = PlayerList()
        first_player = Player("000513", "Mark")
        second_player = Player("000232", "Eugene")
        first_node = PlayerNode(first_player)
        second_node = PlayerNode(second_player)
        test_list.insert_at_tail(first_node)
        test_list.insert_at_tail(second_node)
        # archive the old tail
        old_tail = test_list.get_tail()
        # remove the tail node
        test_list.delete_from_tail()
        # archive the new tail
        new_tail = test_list.get_tail()
        self.assertFalse(test_list.is_empty())
        self.assertEqual(new_tail, first_node)
        self.assertNotEqual(new_tail, old_tail)


