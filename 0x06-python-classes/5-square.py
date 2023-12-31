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

    @property
    def size(self):
        """ Get and set the true size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Set size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
