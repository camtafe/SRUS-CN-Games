import unittest
from player_list import PlayerList
from player_node import PlayerNode
from player import Player


class TestList(unittest.TestCase):
    def test_empty_list(self):
        empty_list = PlayerList()
        self.assertTrue(empty_list.is_empty())

    def test_filled_list(self):
        filled_list = PlayerList()
        dummy_player = Player("513", "Mark")
        node = PlayerNode(dummy_player)
        filled_list.insert_at_head(node)
        self.assertFalse(filled_list.is_empty())
