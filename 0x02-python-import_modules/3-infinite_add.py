#!/usr/bin/python3
import sys
sum = 0
j = -1
for x in sys.argv:
    j += 1
    if j == 0:
        continue
    sum += int(x)
print("{:d}".format(sum))
