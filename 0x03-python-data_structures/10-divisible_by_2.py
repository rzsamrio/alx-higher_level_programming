#!/usr/bin/python3
def divisible_by_2(mylist=[]):
    res = []
    for i in mylist:
        if (i % 2 == 0):
            res.append(True)
        else:
            res.append(False)
    return res
