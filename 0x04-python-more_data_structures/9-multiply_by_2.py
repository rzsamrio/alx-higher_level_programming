#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return {x: a_dictionary.get(x)*2 for x in a_dictionary}
