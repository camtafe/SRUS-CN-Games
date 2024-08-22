class PlayerNode:
    def __init__(self, player):
        self.__player = player
        self.__next = None
        self.__prev = None

    # getters and setters of mangled variables for privacy purposes
    @property
    def player(self):
        return self.__player

    @property
    def next(self):
        return self.__next

    @property
    def prev(self):
        return self.__prev

    @next.setter
    def next(self, node):
        self.__next = node

    @prev.setter
    def prev(self, node):
        self.__prev = node

    @property
    def key(self) -> str:
        return self.__player.uid

    # lists the variables inside the player node in string form
    def __str__(self):
        return f"Player Node(Name:{self.__player.name}, uid:{self.key})"
