#!/usr/bin/python3

def print_last_digit(number):
    """Prints the last digit of a number"""
    if number < 0:
        number = abs(number)
        last = number % 10
        print("{}".format(last), end="")
        return last
    else:
        last = number % 10
        print("{}".format(last), end="")
        return last
