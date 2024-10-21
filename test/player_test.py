import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("000123", "Eugene Krabs")
    def test_uid(self):
        self.assertEqual(self.player.uid, "000123")

    def test_name(self):
        self.assertEqual(self.player.name, "Eugene Krabs")