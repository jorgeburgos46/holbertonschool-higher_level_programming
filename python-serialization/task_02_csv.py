#!/usr/bin/env python3
"""Convert CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Read a CSV file and write its contents to data.json in JSON format.

    Args:
        csv_filename (str): The path to the CSV file to convert.

    Returns:
        bool: True if conversion succeeded, False on error.
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
        return False
    except (OSError, csv.Error, json.JSONDecodeError):
        return False
