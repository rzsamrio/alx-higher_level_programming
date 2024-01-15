#!/usr/bin/python3
""" Module defines the rectangle class """

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
            for prop, val in kwargs.items():
                match prop:
                    case "width":
                        self.width = val
                    case "height":
                        self.height = val
                    case "id":
                        self.id = val
                    case "x":
                        self.x = val
                    case "y":
                        self.y = val
                    case _:
                        pass
            return
        for i, arg in enumerate(args):
            match i:
                case 0:
                    self.id = arg
                case 1:
                    self.width = arg
                case 2:
                    self.height = arg
                case 3:
                    self.x = arg
                case 4:
                    self.y = arg
                case _:
                    pass

    def to_dictionary(self):
        """ Returns a dictionary of Instance's properties """
        return {
            'id': self.id, 'width': self.width, 'height': self.height,
            'x': self.x, 'y': self.y}

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
