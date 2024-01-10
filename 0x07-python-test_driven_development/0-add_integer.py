#!/usr/bin/python3
""" Performs arithmetic on integers """


def add_integer(a, b=98):
    """ Function calculates the sum of 2 integers
    Args: 2 integers or floats
    Return: The sum as a rounded integer """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
