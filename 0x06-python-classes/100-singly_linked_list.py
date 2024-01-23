#!/usr/bin/python3
""" This module represents a class Node and a class SinglyLinkedList"""
class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize the Node.

        Args:
            data: The data to store in the node.
            next_node (Node): Reference to the next node in the list.
        """
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initialize the SinglyLinkedList."""
        self.head = None

    def __str__(self):
        """Return a string representation of the linked list."""
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list (increasing order).

        Args:
            value: The value to insert into the list.
        """
        new_node = Node(value)

        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
