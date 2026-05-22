#!/usr/bin/python3
"""This module defines a Square class with calidation and area method."""

class Square:
    """ A class that define a square with a private size attribute."""

        def __init__(self, size=0):
            """Initializes a Square with a given size, default is 0."""
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be an integer")
            self.__size = size

            def area(self):
                """Return the current square area."""
                return self.__size ** 2
