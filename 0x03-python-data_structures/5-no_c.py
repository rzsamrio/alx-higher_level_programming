#!/usr/bin/python3
def no_c(my_string):
    """Deletes the cs in a string"""
    string = list(my_string)
    for i, a in enumerate(string):
        if a == 'c' or a == 'C':
            del(string[i])
    return "".join(string)
