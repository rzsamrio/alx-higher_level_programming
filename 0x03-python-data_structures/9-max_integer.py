#!/usr/bin/python3
def max_integer(mylist=[]):
    if len(mylist) == 0:
        return None
    for i, num in enumerate(mylist):
        if i == 0:
            max = num
        elif (num > max):
            max = num
    return max
