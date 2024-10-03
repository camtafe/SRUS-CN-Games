import unittest
from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player import Player
from app.hash_map import PlayerHashMap

# dummy/test players and nodes for redundancy purposes
first_player = Player("000513", "Mark")
second_player = Player("000232", "Eugene")
third_player = Player("000747", "Darius")
first_node = PlayerNode(first_player)
second_node = PlayerNode(second_player)
third_node = PlayerNode(third_player)

class TestCase(unittest.TestCase):
    def setUp(self):
        self.test_map = PlayerHashMap()

    def test_hash_map_put_function(self):
        self.test_map.put("testkey", "dirk")
        self.assertEqual(str(self.test_map.get("testkey")), "Player(uid=testkey, name=dirk)")

    def test_hash_map_size_function(self):
        self.test_map.put("000513", "Mark")
        self.test_map.put("000232", "Eugene")
        self.assertEqual(self.test_map.size(), 2)
