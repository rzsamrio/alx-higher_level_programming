#!/usr/bin/python3
def main():
    """ Prints the sum of two variables """
    from add_0 import add
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))


if __name__ == "__main__":
    main()
