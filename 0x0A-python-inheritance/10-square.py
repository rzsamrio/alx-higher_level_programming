#!/usr/bin/python3
""" Module contains the Geometry Class: Square """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defines the attributes and methods for a square

    Args:
        size (int): The dimension of the square
    """

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Returns the area of a square object """
        return (self.__size * self.__size)
