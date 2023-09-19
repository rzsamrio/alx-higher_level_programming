#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 != 0:
        z = i - 32
    else:
        z = i
    print("{}".format(chr(z)), end="")
