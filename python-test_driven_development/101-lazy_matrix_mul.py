#!/usr/bin/python3
"""
This module provides a function to multiply two matrices using NumPy.
It uses numpy.matmul for efficient matrix multiplication.
It handles edge cases like empty matrices and incompatible dimensions.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy and returns the result.
    Raises ValueError or TypeError for invalid inputs.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(
                    "m_a should contain only integers or floats")
    for row in m_b:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(
                    "m_b should contain only integers or floats")
    row_size_a = len(m_a[0])
    for row in m_a:
        if len(row) != row_size_a:
            raise TypeError("each row of m_a must be of the same size")
    row_size_b = len(m_b[0])
    for row in m_b:
        if len(row) != row_size_b:
            raise TypeError("each row of m_b must be of the same size")
    if row_size_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return np.matmul(m_a, m_b)
