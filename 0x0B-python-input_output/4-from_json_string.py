#!/usr/bin/python3
""" Contains json string converter """


def from_json_string(my_str):
    """ Function loads an object from a json string

    Args:
        my_str (str): object to load

    Return: object
    """

    import json
    return json.loads(my_str)
