#!/usr/bin/python3
""" Contains the student class """


class Student:
    """ Struct describes the a student

    Args:
        first_name: First name of student
        last_name: last name of student
        age: age of student

    Return: NA"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns the dictionary form of the data structure """
        import json

        json_str = json.dumps(self.__dict__)
        json_dict = json.loads(json_str)
        if attrs is None:
            return json_dict

        for key in list(json_dict):
            if key not in attrs:
                del json_dict[key]
        update_str = json.dumps(json_dict)
        return json.loads(update_str)
