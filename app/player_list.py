class PlayerList:
    def __init__(self):
        # head and tail of the linked list for identification purposes
        self.__head = None
        self.__tail = None

    def is_empty(self):
        # returns if the list is empty or not via checking head is empty
        return self.__head is None

    # getters for head and tail
    # @property was giving me errors, I'm not sure why
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
            # exits if no head to remove
            return None
        node = self.__head
        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None
        else:
            # head marker set to the next node in line
            # original head is removed
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
            # tail marker is set to previous node
            # the original tail is removed
            self.__tail = self.__tail.prev
            self.__tail.next = None
            return f"Removed Tail: {node}"

    def delete_via_key(self, key: str):
        if self.is_empty():
            return
        current_node = self.__head
        while current_node is not None:
            # if the identified node has the targeted key, proceed
            if current_node.player.uid == key:
                # removes the node from the head marker if identified as the head
                if current_node == self.__head:
                    self.delete_from_head()
                # same but tail
                elif current_node == self.__tail:
                    self.delete_from_tail()
                else:
                    # connect the pointers of the nodes around the removed to each other
                    # prevents the chain from breaking
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                return
            # continue to traverse until the node is None
            current_node = current_node.next

    def display_lists(self, forward=True):
        display = "Lists:\n"
        # if the list is empty simply exit with Empty result
        if self.is_empty():
            display += "Empty"
            return
        else:
            # the targeted node is set to head if forward remains true as the default
            # otherwise the tail will be selected
            node = self.__head if forward else self.__tail
            # while there is an identifiable node
            while node is not None:
                # marks the head and tail node if the targeted node is identified as the head or tail
                # otherwise doesn't print anything
                head_display = "Head " if node == self.__head else ""
                tail_display = "Tail " if node == self.__tail else ""
                # prints each node to the display with a marker if possible
                display += f"-> {head_display}{tail_display} Name: {node.player.name} | User ID: {node.player.uid}\n"
                # moves forward or backward up the chain depending on if forward is true or not
                node = node.next if forward else node.prev
        return display

    def find_item(self, key: str, forward=True):
        item = None
        if self.is_empty():
            return
        else:
            node = self.__head if forward else self.__tail
        while node.player.uid is not key and node is not None:
            node = node.next if forward else node.prev
        else:
            return node.player

    def length(self, forward=True):
        size = 0
        if self.is_empty():
            return size
        else:
            node = self.__head if forward else self.__tail
        while node is not None:
            size += 1
            node = node.next if forward else node.prev
        else:
            return size
