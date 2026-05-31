#!/usr/bin/python3
"""Defines a MyList class that extends list with sorted printing."""


class MyList(list):
    """Represents a list with an additional sorted print capability."""

    def print_sorted(self):
        """Print the list elements in ascending order without modifying it."""
        print(sorted(self))
