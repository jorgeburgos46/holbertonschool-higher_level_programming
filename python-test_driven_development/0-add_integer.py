#!/usr/bin/python3
"""
This module provides a function to add two integers.
It handles integers and floats, casting floats to integers before addition.
The function raises TypeError for invalid input types.
It also handles edge cases like None and string inputs.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (cast to int) and returns the result.
    Raises TypeError if a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
