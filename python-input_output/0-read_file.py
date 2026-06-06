#!/usr/bin/python3
"""This module reads the content of a file and prints it to the console."""


def read_file(filename=""):
    """Read and print the content of a file."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")


if __name__ == "__main__":
    read_file("my_file_object.txt")
