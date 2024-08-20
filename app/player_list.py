class PlayerList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def is_empty(self):
        return self.__head is None

    def insert_at_head(self, node):
        if self.is_empty:
            # empty so new node becomes head and tail
            self.__head = node
            self.__tail = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node
