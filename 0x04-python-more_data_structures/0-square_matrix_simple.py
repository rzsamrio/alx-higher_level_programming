#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ Squares a matrix """
    square = []
    for x in matrix:
        tmp = [x[i]**2 for i in range(len(x))]
        square.append(tmp)
    return square
