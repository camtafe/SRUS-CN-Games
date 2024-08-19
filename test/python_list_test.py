import unittest
from player_list import PlayerList

class TestList(unittest.TestCase):
    def test_empty_list(self):
        list0 = PlayerList()
        self.assertEqual(list0.is_empty(), True)