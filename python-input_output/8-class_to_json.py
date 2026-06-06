#!/usr/bin/python3
"""Return a dictionary description for JSON serialization of an object."""


def class_to_json(obj):
    """Return the dictionary representation of obj for JSON serialization."""
    return obj.__dict__.copy()
