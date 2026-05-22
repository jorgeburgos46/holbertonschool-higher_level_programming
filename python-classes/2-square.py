#!/usr/bin/python3
"""Class created square."""


class Square
"""A class that define a square with a private size attributes."""

    def __init__(self, size=0):
    """Initializes a Square with a given size, defacult 0."""
    if not isinstance(size, int):
            raise TypeError("size must be an integer"
    if size < 0:
        raise ValueError("size must be >= 0")
        self.__size = size
