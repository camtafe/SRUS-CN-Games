import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):
    def test_uid(self):
        player = Player("000123", "Eugene Krabs")
        self.assertEqual(player.uid, "000123")

    def test_name(self):
        player = Player("000123", "Eugene Krabs")
        self.assertEqual(player.name, "Eugene Krabs")