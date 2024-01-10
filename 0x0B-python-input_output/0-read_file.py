#!/usr/bin/python3
""" Module contains the read_file function """


def read_file(filename=""):
    """ This displays the content of a file on stdout

    Args:
        filename: The name of the file to read. Default = Empty String

    Returns: NA
    """

    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    print(text, end='')
