#!/usr/bin/python3
"""This module reads the content of a file and prints it to the console."""


with open('my_file_object.txt') as file:
    """Reads the content of 'my_file_object.txt' and prints it."""
    print(file.read())
    """Note: The file is automatically closed after the block is executed due to the use of 'with' statement."""