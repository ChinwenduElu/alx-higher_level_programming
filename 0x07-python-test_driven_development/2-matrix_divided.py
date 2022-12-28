#!/usr/bin/python3
"""
Module 2-matrix_divided
Function that divides all elements of a matrix
Must be same size lists of ints or floats
"""


def matrix_divided(matrix, div):
    """
    Returns A new matrix with the result of the division
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    new_matrix = []
    samelen = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(msg)
        if len(lists) != samelen:
            raise TypeError("Each row of the matrix must have the same size")
        newlist = []
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError(msg)
            newlist.append(round(i/div, 2))
            new_matrix.append(newlist)
            return new_matrix
