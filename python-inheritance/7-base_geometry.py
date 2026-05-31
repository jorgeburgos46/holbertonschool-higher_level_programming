#!/usr/bin/python3
"""Module that defines BaseGeometry class."""


class BaseGeometry:
    """Class with area and integer_validator methods."""

    def area(self):
        """Raise Exception - not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
