#!/usr/bin/env python3
"""Module that defines CountedIterator class."""


class CountedIterator:
    """Iterator that keeps track of how many items have been iterated."""

    def __init__(self, iterable):
        """Initialize with an iterable and set counter to 0."""
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the number of items iterated so far."""
        return self.count

    def __next__(self):
        """Fetch next item and increment counter."""
        item = next(self.iterator)
        self.count += 1
        return item

    def __iter__(self):
        """Return the iterator itself."""
        return self
