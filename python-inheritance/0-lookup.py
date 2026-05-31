#!/usr/bin/python3
"""Defines a lookup function for object attributes and methods."""


def lookup(obj):
    """Return a sorted list of attributes and methods available for obj."""
    return dir(obj)
