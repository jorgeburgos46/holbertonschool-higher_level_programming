#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
It validates matrix structure and division value before performing operations.
It handles edge cases like zero division, invalid types, unequal row sizes.
It returns a new matrix with results rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimal places.
    Raises TypeError if matrix is invalid or div is not a number.
    Raises ZeroDivisionError if div is 0.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(msg)
    for row in matrix:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(msg)
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]
