#!/usr/bin/python3
""" Print the arguments and number of arguments given"""
if __name__ == '__main__':
    import sys
    arg_len = len(sys.argv) - 1
    if arg_len == 0:
        print("{:d} arguments.".format(arg_len))
    elif arg_len == 1:
        print("{:d} argument:".format(arg_len))
    else:
        print("{:d} arguments:".format(arg_len))
    j = -1
    for arg in sys.argv:
        j += 1
        if j == 0:
            continue
        print("{:d}: {}".format(j, arg))
