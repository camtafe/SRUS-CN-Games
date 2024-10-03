from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode


class PlayerHashMap:
    def __init__(self):
        #
        self.SIZE = 10
        # hashmap
        self.hashmap = [PlayerList() for _ in range(self.SIZE)]

    def put(self, key: str, name: str):
        hash_total = 0
        for char in key:
            hash_total += ord(char)
        bucket = hash_total % self.SIZE
        self.hashmap[bucket].insert_at_head(PlayerNode(Player(key, name)))

    def get(self, key):
        hash_total = 0
        for char in key:
            hash_total += ord(char)
        bucket = hash_total % self.SIZE
        item = self.hashmap[bucket].find_item(key)
        return item

    def remove(self, key):
        hash_total = 0
        for char in key:
            hash_total += ord(char)
        bucket = hash_total % self.SIZE
        self.hashmap[bucket].delete_via_key(key)

    def size(self):
        total_players = 0
        for player_list in self.hashmap:
            total_players += player_list.length()
        print(f"Total Hash Map Size: {total_players}")
        return total_players
