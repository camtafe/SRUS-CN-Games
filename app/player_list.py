class PlayerList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def is_empty(self):
        return self.__head is None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

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

    def delete_from_head(self):
        if self.is_empty():
            return None
        node = self.__head
        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None
        else:
            self.__head = self.__head.next
            self.__head.prev = None
            return f"Removed Head: {node}"

    def delete_from_tail(self):
        if self.is_empty():
            return None
        node = self.__tail
        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None
        else:
            self.__tail = self.__tail.prev
            self.__tail.next = None
            return f"Removed Tail: {node}"
