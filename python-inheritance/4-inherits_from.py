#!/usr/bin/python3
"""Defines a function that checks if an object inherits from a class."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherits from a_class.

    The object must be an instance of a subclass of a_class, not a_class
    itself.
    """
    return type(obj) is not a_class and isinstance(obj, a_class)
