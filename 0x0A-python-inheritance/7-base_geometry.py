#!/usr/bin/python3
""" Contains the BaseGemotry class """


class BaseGeometry:
    """ ' I know th plans i have for you ' """

    def area(self):
        raise Exception("area() is not implemented")

    @staticmethod
    def integer_validator(name, value):
        """ Validate an integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
