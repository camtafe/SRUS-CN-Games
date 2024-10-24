from __future__ import annotations
from app.player_node import PlayerNode


class PlayerList:

    _head: None
    _tail: None

    def __init__(self):
        """
        head and tail of the linked list for identification purposes
        _head - the node marked as the head node of the player list
        _tail - the node marked as the tail node of the player list

        the head and tail are protected attributes as displayed by an '_' in their variable name
        so that they are encapsulated but are able to modified by the subclass methods that are designed to alter them
        while maintaining their integrity
        """
        self._head = None
        self._tail = None

    def is_empty(self) -> bool:
        return self._head is None or self._tail is None

    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail

    def insert_at_head(self, node: PlayerNode | None):
        if self.is_empty():
            """
            if the player list is empty, the new node becomes head and tail
            as there is no other nodes to connect itself towards
            """
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def insert_at_tail(self, node: PlayerNode | None):
        if self.is_empty():
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            # the new node points to the current tail as its previous node
            node.prev = self._tail
            # the node then marks itself as the tail
            # the old tail still exists but is no longer designated as the tail
            self._tail = node

    def delete_from_head(self):
        if self.is_empty():
            return None
        node = self._head
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            # original head is removed, head marker set to the next node in line
            self._head = self._head.next
            self._head.prev = None
            return f"Removed Head: {node}"

    def delete_from_tail(self):
        if self.is_empty():
            return None
        node = self._tail
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            # tail marker is set to previous node
            # the original tail is removed
            self._tail = self._tail.prev
            self._tail.next = None
            return f"Removed Tail: {node}"

    def delete_via_key(self, key: str):
        if self.is_empty():
            return
        current_node = self._head
        while current_node is not None:
            # if the identified node has the targeted key, proceed
            if current_node.player.uid == key:
                # removes the node from the head marker if identified as the head
                if current_node == self._head:
                    self.delete_from_head()
                # same but tail
                elif current_node == self._tail:
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
        """
        Cycles through the linked list, displaying the nodes in order
        from head to tail or tail to head depending on if forward bool is true or false

        """
        display = "Lists:\n"
        # if the list is empty simply exit with Empty result
        if self.is_empty():
            return display + "Empty"
        else:
            # the targeted node is set to head if forward remains true as the default
            # otherwise the tail will be selected
            node = self._head if forward else self._tail
            # while there is an identifiable node
            while node is not None:
                # marks the head and tail node if the targeted node is identified as the head or tail
                # otherwise doesn't print anything
                head_display = "Head " if node == self._head else ""
                tail_display = "Tail " if node == self._tail else ""
                # prints each node to the display with a marker if possible
                display += f"-> {head_display}{tail_display} Name: {node.player.name} | User ID: {node.player.uid}\n"
                # moves forward or backward up the chain depending on if forward is true or not
                node = node.next if forward else node.prev
        return display

    def find_item(self, key: str, forward=True):
        """
        Traverses the
        :param key:
        :param forward:
        :return:
        """
        item = None
        if self.is_empty():
            return
        else:
            node = self._head if forward else self._tail
        while node.player.uid is not key and node is not None:
            node = node.next if forward else node.prev
        else:
            return node.player

    def length(self, forward=True):
        """
        Traverses the player list and adds to a counter each time it passes a node that isn't empty.
        """
        size = 0
        if self.is_empty():
            return size
        else:
            node = self._head if forward else self._tail
        while node is not None:
            size += 1
            node = node.next if forward else node.prev
        else:
            return size
