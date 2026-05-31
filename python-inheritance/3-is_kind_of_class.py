#!/usr/bin/python3
"""Defines a function to check whether an object is an instance of a class or
inherits from that class."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of a_class or of a subclass of a_class."""
    return isinstance(obj, a_class)
