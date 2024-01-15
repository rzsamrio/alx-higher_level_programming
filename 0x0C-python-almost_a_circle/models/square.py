#!/usr/bin/python3
""" Insert doc """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ The Square Class

    Args:
        size (int): Square dimension
        x: abscissa position in space
        y: oordinate position in space
        id: Unique identifier of object
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize the square object """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ String representation of Instance """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ Update the properties of Instance """
        if not args:
            for prop, val in kwargs.items():
                match prop:
                    case "size":
                        self.size = val
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
                    self.size = arg
                case 2:
                    self.x = arg
                case 3:
                    self.y = arg
                case _:
                    pass

    def to_dictionary(self):
        """ Return a dictionary of Instance properties """
        return {
            'id': self.id, 'size': self.size,
            'x': self.x, 'y': self.y}

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
