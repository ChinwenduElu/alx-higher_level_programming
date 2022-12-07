#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_cpy = matrix.copy()
    
    for i in range(len(matrix)):
        matrix_cpy[i] = list(map(lambda x: x**2, matrix[i]))

     return (matrix_cpy)
