#!/usr/bin/python3
""" Converts a data structure to JSON format """


def class_to_json(obj):
    """ Returns the dictionary format of an object """
    return obj.__dict__
