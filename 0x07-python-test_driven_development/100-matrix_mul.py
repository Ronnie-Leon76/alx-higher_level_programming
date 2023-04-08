#!/usr/bin/python3
"""Matrix Multiplication"""


def matrix_mul(m_a, m_b):
    """
    Function that multiplies two matrices
    Args:
        m_a: first parameter
        m_b: second parameter
    Returns:
        list: matrix
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for i in range(len(m_a)):
        if type(m_a[i]) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(m_a[i]) == 0:
            raise ValueError("m_a can't be empty")
        for j in range(len(m_a[i])):
            if type(m_a[i][j]) is not int and type(m_a[i][j]) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for i in range(len(m_b)):
        if type(m_b[i]) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(m_b[i]) == 0:
            raise ValueError("m_b can't be empty")
        for j in range(len(m_b[i])):
            if type(m_b[i][j]) is not int and type(m_b[i][j]) is not float:
                raise TypeError("m_b should contain only intefers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = [[0 for i in range(len(m_b[0]))] for j in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
