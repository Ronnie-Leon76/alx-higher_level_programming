#!/usr/bin/python3
"""Function divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    Args:
        matrix: first parameter
        div: second parameter
    Returns:
        list: matrix
    """
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(col, (int, float)) for row in matrix for col in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for col in row:
            new_elem = round(col / div, 2)
            if round(new_elem, 2) != new_elem:
                raise ValueError("elements must be rounded to 2 dp")
            new_row.append(new_elem)
        new_matrix.append(new_row)

    return new_matrix
