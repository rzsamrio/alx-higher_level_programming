#!/usr/bin/python3
""" Creates a subclass for the list class """


class MyList(list):
    """ Defines a new method print_sorted that
    prints the sorted version of the list """

    def __init__(self):
        list.__init__(self)

    def print_sorted(self):
        new = list.copy(self)
        new.sort()
        print(new)
