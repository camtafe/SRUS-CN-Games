import unittest
from app.hash_map import PlayerHashMap


class TestCase(unittest.TestCase):
    def setUp(self):
        self.test_map = PlayerHashMap()
        self.test_map.put("testkey", "dirk")
        self.test_map.put("000513", "Mark")
        self.test_map.put("000232", "Eugene")

    def test_hashmap_put_function(self):
        self.assertEqual(str(self.test_map.get("testkey")), "Player(uid=testkey, name=dirk)")

    def test_hashmap_size_function(self):
        self.assertEqual(self.test_map.size(), 3)

    def test_hashmap_get_function(self):
        self.test_map.get("000513")
        self.assertEqual(str(self.test_map.get("000513")), "Player(uid=000513, name=Mark)")

    def test_hashmap_key_remove_function(self):
        self.test_map.remove("000513")
        self.assertEqual(self.test_map.size(), 2)

    def test_hashmap_display_function(self):
        self.test_map.display()
        expected_string = """#############
# Hash Maps #
#############
# Bucket 0  #
#############
Lists:
Empty
#############
# Bucket 1  #
#############
Lists:
Empty
#############
# Bucket 2  #
#############
Lists:
Empty
#############
# Bucket 3  #
#############
Lists:
Empty
#############
# Bucket 4  #
#############
Lists:
Empty
#############
# Bucket 5  #
#############
Lists:
-> Head Tail  Name: Eugene | User ID: 000232

#############
# Bucket 6  #
#############
Lists:
Empty
#############
# Bucket 7  #
#############
Lists:
-> Head  Name: Mark | User ID: 000513
-> Tail  Name: dirk | User ID: testkey

#############
# Bucket 8  #
#############
Lists:
Empty
#############
# Bucket 9  #
#############
Lists:
Empty
"""

        self.assertMultiLineEqual(str(self.test_map.display()), expected_string)
