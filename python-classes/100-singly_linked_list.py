#!/usr/bin/python3
"""This module defines Node and SinglyLinkedList classes."""


class Node:
    """A class that defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a Node with data and next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data with integer validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node with Node or None validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list."""

    def __init__(self):
        """Initializes an empty SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """Returns string representation of the list."""
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip("\n")

    def sorted_insert(self, value):
        """Inserts a new Node in correct sorted position in increasing order."""
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head
        while current.next_node is not None:
            if value < current.next_node.data:
                break
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node
