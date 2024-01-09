#!/usr/bin/python3
""" This module checks for the possibility of a subclass """


def is_kind_of_class(obj, a_class):
    """ Returns ture if obj is a subclass of a_class
        Else returns false """
    x = 0
    try:
        while(dir(a_class)[x]):
            try:
                dir(obj).index(dir(a_class)[x])
            except ValueError:
                return False
            x += 1
    except IndexError:
        return True
