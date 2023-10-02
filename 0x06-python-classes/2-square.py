#!/usr/bin/python3
"""Define Square"""


class Square:
    """ Initialiase square with defined size, default is 0.
        Size value must be an int, and >= 0."""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
