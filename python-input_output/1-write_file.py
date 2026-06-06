#!/usr/bin/python3
"""Write text to a UTF-8 encoded file."""


def write_file(filename="", text=""):
    """Write text to filename using UTF-8.

    Return the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
