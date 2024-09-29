import unittest
from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player import Player
from app.hash_map import PlayerHashMap

test_map = PlayerHashMap()
test_map.put("derp", "dirk")

#for i in range(10):
#    print(i)
#    print(test_map.hashmap[i].get_head())

print(test_map.get("derp"))