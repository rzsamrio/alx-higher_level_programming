#!/usr/bin/python3
"""A 2D geometric obbject; a quadilateral of 2 equal parallel sides"""


class Rectangle:
    """Define the rectangle class
    Args:
        width (int): length of the rectangle
        height (int): height of the rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Print the rectangle block with the # character"""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end='')
            if i != self.__height - 1:
                print()
        return ""

    def __repr__(self):
        """Returns the string representation of code creating the instance """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Signals an instance being deleted"""
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
