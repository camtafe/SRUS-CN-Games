class PlayerNode:
    def __init__(self, player):
        self._player = player
        self._next = None
        self._prev = None

    # getters and setters of mangled variables for privacy purposes
    @property
    def player(self):
        return self._player

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, node):
        self._prev = node

    @property
    def key(self) -> str:
        return self._player.uid

    # lists the variables inside the player node in string form
    def __str__(self):
        return f"Player Node(Name:{self._player.name}, uid:{self.key})"
