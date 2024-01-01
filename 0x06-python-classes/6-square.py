#!/usr/bin/python3
""" Square: A 2 dimensional shape that can be used to perform greometric
    operations on """


class Square:
    """ Performs the basic operations of a square
    Args:
        size (int): the dimensions of square object"""

    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(x) is not int or x < 0 for x in position):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """ Calculates the Area of the square object"""
        return self.__size * self.__size

    def my_print(self):
        """ Print the square using # characters """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print()

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

    @property
    def position(self):
        """ The position setter """
        return self.__position

    @position.setter
    def position(self, value):
        """ Set position"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(x) is not int or x < 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
