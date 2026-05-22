#!/usr/bin/python3
"""This module defines a Square class with getter and setter for size."""


class square:
    """A class that defines a square with a private size attribute."""

    def __init__(self, size=0):
        """Initializes a Square with a given size, default is 0."""
        self.size = size

        @property
        def size(self):
            """Retrives the size of the square."""
            return self.__size

        @size.setter
        def size(self, valeu):
            """Sets the size of the square with type and value validation."""
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        def area(self):
            """Return the current square area."""
            return self.__size ** 2

