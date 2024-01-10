#!/usr/bin/python3
""" Contains the inherit_from function """


def inherits_from(obj, a_class):
    """ Checks if the object is a subclass, and only a subclass of
    the class spcified.

    Args:
        obj (object) : Instance of a class
        a_class (type/class) : Class to compare with

    Return: Boolean
    """

    obj_class = obj.__class__
    return obj_class is not a_class and issubclass(obj_class, a_class)
