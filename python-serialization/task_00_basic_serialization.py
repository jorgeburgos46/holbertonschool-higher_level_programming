#!/usr/bin/env python3
"""Basic JSON serialization helper."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The filename where the JSON should be saved.
    """
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file)


def load_and_deserialize(filename):
    """Load JSON data from a file and deserialize it to a Python dictionary.

    Args:
        filename (str): The filename of the JSON file to load.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)
