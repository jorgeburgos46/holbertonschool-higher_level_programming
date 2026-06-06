#!/usr/bin/python3
"""Module for appending text to a UTF-8 encoded file."""


def append_write(filename="", text=""):
    """Append text to filename using UTF-8 and return characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
