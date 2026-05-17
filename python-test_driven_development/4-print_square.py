#!/usr/bin/python3
"""
This module provides a function to print a square with the character #.
It validates the size parameter before printing.
It handles edge cases like negative size, float size, and zero size.
"""


def print_square(size):
    """
    Prints a square with the character #.
    Raises TypeError if size is not an integer.
    Raises ValueError if size is less than 0.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
