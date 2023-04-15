#!/usr/bin/python3
"""Pascal's triangle of n function"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal's
    triangle of n
    """
    pascal_list = []
    if n <= 0:
        return pascal_list
    else:
        for i in range(n):
            row = [1]
            for j in range(1, i):
                row.append(pascal_list[i-1][j-1] + pascal_list[i-1][j])
            if i > 0:
                row.append(1)
            pascal_list.append(row)
        return pascal_list
