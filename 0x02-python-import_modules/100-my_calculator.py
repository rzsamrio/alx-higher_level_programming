#!/usr/bin/python3
"""
    Command line calculator program that handles basic operations
"""


def main():
    """
        Performs basic arithmetic using cla
    """
    import sys

    argv = sys.argv
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operand = ['+', '-', '*', '/']

    for sym in operand:
        if sys.argv[2] == sym:
            op_check = 1
            break
        else:
            op_check = 0
    if op_check == 0:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a1 = int(sys.argv[1])
    a2 = int(sys.argv[3])
    op = sys.argv[2]

    from calculator_1 import add, sub, mul, div
    if op == '+':
        print("{:d} {} {:d} = {:d}".format(a1, op, a2, add(a1, a2)))
    elif op == '-':
        print("{:d} {} {:d} = {:d}".format(a1, op, int(a2), sub(a1, a2)))
    elif op == '*':
        print("{:d} {} {:d} = {:d}".format(a1, op, int(a2), mul(a1, a2)))
    elif op == '/':
        print("{:d} {} {:d} = {:d}".format(a1, op, int(a2), div(a1, a2)))


if __name__ == '__main__':
    main()
