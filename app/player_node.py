class PlayerNode:
    def __init__(self, player):
        """
        _player - the player object that is encapsulated inside the node with all its data
        _next - the next player node in front of the current node
        _prev - the previous player node behind the current node
        """
        self._player = player
        self._next = None
        self._prev = None

    """
    getters and setters of protected variables, this is so they are not accessed directly but are accessible
    via the subclasses 
    """
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

    def __str__(self):
        """
        lists the variables inside the player node in string form
        """
        return f"Player Node(Name:{self._player.name}, uid:{self.key})"
