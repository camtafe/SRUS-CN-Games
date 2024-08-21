class PlayerList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def is_empty(self):
        return self.__head is None

    def insert_at_head(self, node):
        if self.is_empty():
            # empty so new node becomes head and tail
            self.__head = node
            self.__tail = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def insert_at_tail(self, node):
        if self.is_empty():
            # empty so new node becomes head and tail
            self.__head = node
            self.__tail = node
        else:
            # tail marks next node as the new node
            self.__tail.next = node
            # the new node points to the current tail as its previous node
            node.prev = self.__tail
            # the node then marks itself as the tail
            # the old tail still exists but is no longer designated as the tail
            self.__tail = node
