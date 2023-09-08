#!/usr/bin/python3
def main():
    """Prints the result of basic operations of args a and b """
    import calculator_1
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, calculator_1.add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, calculator_1.sub(a, b)))
    print("{:d} + {:d} = {:d}".format(a, b, calculator_1.mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, calculator_1.div(a, b)))


if __name__ == '__main__':
    main()
