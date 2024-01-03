#!/usr/bin/python3
""" Divides a Matrix """


def matrix_divided(matrix, div):
    """
    Divides each element of a matrix
        Args: A matrix of floats/integers and the divisor
        Return: Resulting matrix from division
    """
    err_string = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(err_string)
    for x in matrix:
        if type(x) is not list or any(type(a) not in [int, float] for a in x):
            raise TypeError(err_string)

    t_len = len(matrix[0])  # Store the length of the first row
    if any(len(a) != t_len for a in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(x[y]/div, 2) for y in range(len(x))] for x in matrix]
    return result
