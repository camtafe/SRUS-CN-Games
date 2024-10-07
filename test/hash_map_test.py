import unittest
from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player import Player
from app.hash_map import PlayerHashMap


class TestCase(unittest.TestCase):
    def setUp(self):
        self.test_map = PlayerHashMap()

    def test_hashmap_put_function(self):
        self.test_map.put("testkey", "dirk")
        self.assertEqual(str(self.test_map.get("testkey")), "Player(uid=testkey, name=dirk)")

    def test_hashmap_size_function(self):
        self.test_map.put("000513", "Mark")
        self.test_map.put("000232", "Eugene")
        self.assertEqual(self.test_map.size(), 2)

    def test_hashmap_get_function(self):
        self.test_map.put("000513", "Mark")
        self.test_map.get("000513")
        self.assertEqual(str(self.test_map.get("000513")), "Player(uid=000513, name=Mark)")

    def test_hashmap_remove_function(self):
        # adds two keys to the hashmap, making the theoretical size 2
        self.test_map.put("000513", "Mark")
        self.test_map.put("000232", "Eugene")
        self.test_map.remove("000513")
        # removes a single key, making the size 1 to test the remove function is working
        self.assertEqual(self.test_map.size(), 1)

    def test_hashmap_display_function(self):
        self.test_map.put("000513", "Mark")
        self.test_map.put("000232", "Eugene")
        self.test_map.display()
        expected_string = """#############
# Hash Maps #
#############
# Bucket 0  #
#############
None
#############
# Bucket 1  #
#############
None
#############
# Bucket 2  #
#############
None
#############
# Bucket 3  #
#############
None
#############
# Bucket 4  #
#############
None
#############
# Bucket 5  #
#############
Lists:
-> Head Tail  Name: Eugene | User ID: 000232

#############
# Bucket 6  #
#############
None
#############
# Bucket 7  #
#############
Lists:
-> Head Tail  Name: Mark | User ID: 000513

#############
# Bucket 8  #
#############
None
#############
# Bucket 9  #
#############
None
"""
        self.maxDiff = None
        self.assertMultiLineEqual(str(self.test_map.display()), expected_string)
