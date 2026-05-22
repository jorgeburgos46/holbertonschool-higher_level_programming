#!/usr/bin/python3
"""This module defines a Square class with comparison operators."""


class Square:
    """A class that defines a square with comparison based on area."""

    def __init__(self, size=0):
        """Initializes a Square with a given size, default is 0."""
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with number type and value validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Checks if two squares have equal area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if two squares have different area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Checks if square area is less than other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if square area is less than or equal to other."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Checks if square area is greater than other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if square area is greater than or equal to other."""
        return self.area() >= other.area()
