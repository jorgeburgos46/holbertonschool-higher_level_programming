#!/usr/bin/python3
"""Define a Student class with JSON serialization filtering."""


class Student:
    """Represent a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        If attrs is a list of strings, retrieve only those attributes.
        Otherwise return the full dictionary.
        """
        obj_dict = self.__dict__.copy()
        if isinstance(attrs, list):
            filtered = {}
            for key in attrs:
                if isinstance(key, str) and key in obj_dict:
                    filtered[key] = obj_dict[key]
            return filtered
        return obj_dict
