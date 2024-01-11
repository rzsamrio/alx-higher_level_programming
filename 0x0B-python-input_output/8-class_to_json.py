#!/usr/bin/python3
""" Converts a data structure to JSON format """


def class_to_json(obj):
    """ Function thst converts """
    import json
    json_str = json.dumps(obj.__dict__)
    return json.loads(json_str)
