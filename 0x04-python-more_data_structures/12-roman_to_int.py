#!/usr/bin/python3
"""
    Args: A string containing the numeral

    Return: Base 10 int
"""


def roman_to_int(roman_string):
    """ Converts roman numerals to base 10 integers """

    if roman_string is None or type(roman_string) is not str:
        return 0

    result = 0
    i = 0
    romans = ("I", 1), ("V", 5), ("X", 10), ("L", 50), \
        ("C", 100), ("D", 500), ("M", 1000)
    conv = [y for num in list(roman_string) for x, y in romans if num == x]
    while (i < len(conv)):
        if i < len(conv) - 1 and conv[i + 1] > conv[i]:
            result = result + conv[i + 1] - conv[i]
            i = i + 2
        else:
            result = result + conv[i]
            i = i + 1
    return result


if __name__ == '__main__':
    a = "MMMCMXCIX"
    print(roman_to_int(a))
