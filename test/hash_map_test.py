import unittest
from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player import Player
from app.hash_map import PlayerHashMap


class TestCase(unittest.TestCase):
    def setUp(self):
        self.test_map = PlayerHashMap()

    def test_hash_map_put_function(self):
        self.test_map.put("testkey", "dirk")
        player = Player("testkey", "dirk")
        self.assertEqual(str(self.test_map.get("testkey")), "Player(uid=testkey, name=dirk)")