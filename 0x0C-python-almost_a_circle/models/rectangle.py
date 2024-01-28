#!/usr/bin/python3
""" Module defines the rectangle sub-class """
from models.base import Base


class Rectangle(Base):
    """ Define a rectangle object
    and perform operations suited for the object

    Args:
        width (int): Width of the rectangle
        height (int): Height of the rectangle
        x (int): Defines the position of object on abscissa
        y (int): Defines the position of object on ordinate

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init Rectangle object """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """ Returns the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ Prints the rectangle object """
        for step in range(self.y):
            print()
        for i in range(self.height):
            for step in range(self.x):
                print(' ', end='')
            for i in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """ Return a string representation of the class """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y,
            self.width, self.height)

    def update(self, *args, **kwargs):
        """ Update the properties of the object """
        if not args:
            for key in kwargs:
                if key in ["id", "width", "height", "x", "y"]:
                    setattr(self, key, kwargs[key])
            return
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

    def to_dictionary(self):
        """ Returns a dictionary of Instance's properties """
        return {
            'id': self.id, 'width': self.width, 'height': self.height,
            'x': self.x, 'y': self.y}

    @property
    def width(self):
        """ Get the width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Get height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set height property """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Get the x property """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set the x property """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Get the y property """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set the y property """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
