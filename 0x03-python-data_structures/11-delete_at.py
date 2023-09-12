#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes at element of a list at idx"""
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        del(my_list[idx])
        return my_list
