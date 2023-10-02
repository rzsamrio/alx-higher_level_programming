#!/usr/bin/python3
""" Square: A 2 dimensional shape that can be used to perform greometric
    operations on"""


class Square:
    """ Performs the basic operations of a square
    Args:
        size (int): the dimensions of square object"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Calculates the Area of the square object"""
        return self.__size * self.__size
