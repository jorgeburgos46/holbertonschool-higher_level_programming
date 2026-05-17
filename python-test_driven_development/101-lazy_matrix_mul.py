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
    return np.matmul(m_a, m_b)
