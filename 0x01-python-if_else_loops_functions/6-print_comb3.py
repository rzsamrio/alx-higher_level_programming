#!/usr/bin/python3
for a in range(8):
    for b in range(a + 1, 10):
        if a == b:
            continue
        print("{}{}".format(a, b), end=", ")
print("{}".format(89))
