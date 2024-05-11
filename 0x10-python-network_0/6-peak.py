#!/usr/bin/python3
""" Technical interview prep:
    Finding the peak value in a list """


def find_peak(list_of_integers=[]):
    """ Function that finds the peak value in a list """
    list_of_integers.sort()
    try:
        return (list_of_integers[-1])
    except IndexError:
        return None
