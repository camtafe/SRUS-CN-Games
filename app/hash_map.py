from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode


class PlayerHashMap:
    def __init__(self):
        """
        SIZE - the amount of buckets within the hashmap
        hashmap - the PlayerList data mapped into hashing algorithms for the efficiency
        """
        self.SIZE = 10
        self.hashmap = [PlayerList() for _ in range(self.SIZE)]

    def calculate_hash(self, key: str):
        """
        the hash is calculated by gathering a total amount for each key
        the ordinal of each character of the assigned key of the node is added together
        using the modulus function to assign it to a bucket within the small range
        as the modulus cannot be greater than the divisor there is no issue with size
        """
        hash_total = 0
        for char in key:
            hash_total += ord(char)
        bucket = hash_total % self.SIZE
        return bucket

    def put(self, key: str, name: str):
        bucket = self.calculate_hash(key)
        self.hashmap[bucket].insert_at_head(PlayerNode(Player(key, name)))

    def get(self, key):
        bucket = self.calculate_hash(key)
        item = self.hashmap[bucket].find_item(key)
        return item

    def remove(self, key):
        bucket = self.calculate_hash(key)
        self.hashmap[bucket].delete_via_key(key)

    def size(self):
        total_players = 0
        for player_list in self.hashmap:
            total_players += player_list.length()
        print(f"Total Hash Map Size: {total_players}")
        return total_players

    def display(self):
        display = ""
        display += "#############\n"
        display += "# Hash Maps #\n"

        bucket_amount = 0
        for bucket in self.hashmap:
            display += "#############\n"
            display += f"# Bucket {bucket_amount}  #\n"
            display += "#############\n"
            display += f"{bucket.display_lists()}\n"
            bucket_amount += 1
        print(display)
        return display
