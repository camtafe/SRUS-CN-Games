class PlayerList:
    def __init__(self, r=None):
        self.__head = None

    def is_empty(self):
        return self.__head is None
