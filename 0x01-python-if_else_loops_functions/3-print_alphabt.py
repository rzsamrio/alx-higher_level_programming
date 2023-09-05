#!/usr/bin/python3
""" Prints some alphabet using ASCII """

for i in range(97, 123):
    if (i == ord('e')) or (i == ord('q')):
        continue
    print("{}".format(chr(i)), end='')
