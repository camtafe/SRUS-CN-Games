import unittest
from app.player import Player

# not sure if setup should be created as it would take same amount of lines
class TestPlayer(unittest.TestCase):
    def test_uid(self):
        # tests the inserted uid is the one inserted
        player = Player("000123", "Eugene Krabs")
        self.assertEqual(player.uid, "000123")

    def test_name(self):
        player = Player("000123", "Eugene Krabs")
        self.assertEqual(player.name, "Eugene Krabs")