#!/usr/bin/python3
def divisible_by_2(mylist=[]):
    res = []
    for i in mylist:
        res.append(i % 2 == 0)
    return res
