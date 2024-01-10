#!/usr/bin/python3
""" Contains the load_from_json_file function """


def load_from_json_file(filename):
    """ Returns the object representation of a json string
    From a file

    Args:
        filename (str): Name of file to read json data

    Return: Python object """

    import json
    with open(filename, 'r', encoding='utf-8') as f:
        json_obj = json.load(f)
    return json_obj
