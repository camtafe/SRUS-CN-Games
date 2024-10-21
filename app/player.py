class Player:
    def __init__(self, uid: str, name: str):
        """
        _uid - the numerical user id
        _name - the name of the player
        underscore put at the front of the variable name to prevent potential conflicts
        """
        self._uid = uid
        self._name = name

    def __str__(self):
        # returns the two data variables in the player object in the format of a string
        return f"Player(uid={self._uid}, name={self._name})"

    # getters for mangled variables
    @property
    def uid(self):
        # outputs the uid inside the player object
        return self._uid

    @property
    def name(self):
        # outputs the name inside the player object
        return self._name
