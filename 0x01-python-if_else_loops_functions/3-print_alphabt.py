#!/usr/bin/python3
""" Prints some alphabet using ASCII """

for i in range(97, 123):
    match i:
        case 101 | 113:
            continue
    print("{}".format(chr(i)), end='')
