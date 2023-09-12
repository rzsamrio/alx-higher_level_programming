#!/usr/bin/python3
def max_integer(mylist=[]):
    if len(mylist) == 0:
        return None
    for i, num in enumerate(mylist):
        if i == 0:
            tmax = num
        elif (num > tmax):
            tmax = num
    return tmax
