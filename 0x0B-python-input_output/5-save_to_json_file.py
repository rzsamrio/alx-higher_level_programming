#!/usr/bin/python3
""" Contains json string converter """


def save_to_json_file(my_obj, filename):
    """ Function writes the JSON equivalent of an object
    To a file.

    Args:
        my_obj (object): object to convert to json
        filename: file to store json

    Return: JSON string
    """

    import json

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
