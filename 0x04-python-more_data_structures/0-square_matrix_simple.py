#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_matrix.append([col**2 for col in row])
    return new_matrix
            
