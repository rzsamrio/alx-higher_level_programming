#!/usr/bin/python3

def islower(c):
    """Checks for lowercase"""
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False


def uppercase(str):
    """ Converts string to uppercase """
    for i in str:
        if islower(i):
            c = chr(ord(i) - 32)
        else:
            c = i
        print("{}".format(c), end="")
    print()
