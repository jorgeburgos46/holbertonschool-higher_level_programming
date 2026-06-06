#!/usr/bin/python3
"""Create an object from JSON stored in a file."""

import json


def load_from_json_file(filename):
    """Load and return the Python object represented by JSON in filename."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
