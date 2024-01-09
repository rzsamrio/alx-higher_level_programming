#!/usr/bin/python3
""" Contains the is_same_class method """


def is_same_class(obj, a_class):
    """ Checks if instance is an object of a class """
    if type(obj) is a_class:
        return True
    return False
