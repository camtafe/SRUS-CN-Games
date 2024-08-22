class Player:
    def __init__(self, uid: str, name: str):
        # __uid - the numerical user id
        # __name - the name of the player
        self.__uid = uid
        self.__name = name

    def __str__(self):
        # returns the two data variables in the player object in the format of a string
        return f"Player(uid={self.__uid}, name={self.__name})"

    # getters for mangled variables
    @property
    def uid(self):
        # outputs the uid inside the player object
        return self.__uid

    @property
    def name(self):
        # outputs the name inside the player object
        return self.__name
