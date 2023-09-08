#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    msum = 0
    j = -1
    for x in sys.argv:
        j += 1
        if j == 0:
            continue
        msum += int(x)
    print("{:d}".format(msum))
