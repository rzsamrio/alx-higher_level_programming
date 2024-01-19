#!/usr/bin/python3
""" Insert doc """

import json


class Base:
    """ The Fundamental property/nature of all class in the Models package """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Init base object """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON form of a list of dictionaries """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """ Insert doc """
        #   with open("{}.json".format(type(
        pass
