#!/usr/bin/python3
""" Contains json string converter """


def to_json_string(my_obj):
    """ Function converts an object to a json string

    Args:
        my_obj (object): object to convert

    Retrurn: JSON string
    """

    import json
    return json.dumps(my_obj)
