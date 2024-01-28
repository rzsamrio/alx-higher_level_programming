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
        """ Update the properties of the object """
        if not args:
            for key in kwargs:
                if key in ["id", "size", "x", "y"]:
                    setattr(self, key, kwargs[key])
            return
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

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
