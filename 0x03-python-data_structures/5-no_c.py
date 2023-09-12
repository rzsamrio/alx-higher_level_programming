#!/usr/bin/python3
def no_c(my_string):
    """Deletes the cs in a string"""
    string = list(my_string)
    for i, chr in enumerate(string):
        if chr == 'C':
            string[i] = 'c'
    lnum = string.count('c')  # loop num
    while lnum:
        index = string.index('c')
        del(string[index])
        lnum -= 1
    return "".join(string)
