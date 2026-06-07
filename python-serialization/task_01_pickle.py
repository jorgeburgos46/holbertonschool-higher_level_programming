#!/usr/bin/env python3
"""Pickle-based serialization for a custom object."""

import pickle


class CustomObject:
    """A simple custom object that can be pickled."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in the required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object instance to a pickle file."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (OSError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a CustomObject instance from a pickle file."""
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            if isinstance(obj, cls):
                return obj
        except (OSError, pickle.UnpicklingError, EOFError):
            return None
        return None
