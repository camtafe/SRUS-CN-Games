class PlayerNode:
    def __init__(self, player):
        self.__player = player
        self.__next = None
        self.__prev = None

    # getter for __player
    @property
    def player(self):
        return self.__player

    # getter for __next
    @property
    def next(self):
        return self.__next

    # getter for __prev
    @property
    def prev(self):
        return self.__prev

    # setter for next
    @next.setter
    def next(self, node):
        self.__next = node

    # setter for prev
    @prev.setter
    def prev(self, node):
        self.__prev = node

    # returns the uid of the player object
    @property
    def key(self) -> str:
        return self.__player.uid

    # lists the variable data inside the player node in string form
    def __str__(self):
        return f"Player Node(Name:{self.__player.name}, uid:{self.key})"
