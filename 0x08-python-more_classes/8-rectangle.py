#!/usr/bin/python3
"""A 2D geometric obbject; a quadilateral of 2 equal parallel sides"""


class Rectangle:
    """Define the rectangle class
    Args:
        width (int): length of the rectangle
        height (int): height of the rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

# Gettr and Settrs
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

# Methods
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
        disp = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.height):
            for j in range(self.width):
                disp += str(self.print_symbol)
            if i != self.height - 1:
                disp += "\n"
        return disp

    def __repr__(self):
        """Returns the string representation of code creating the instance """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Signals an instance being deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compare the sizes of 2 rectangles """

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if (rect_1.area() < rect_2.area()):
            return rect_2
        return rect_1
