#!/usr/bin/python3
""" Module contains the write_file function """


def write_file(filename="", text=""):
    """ Writes text to the file described.
    It creates a new file if the file doesn't exist or
    replaces it's contents if it does

    Args:
        filename (str) : name of file to write
        text (str) : text to write

    Return: length of text written
    """

    with open(filename, 'w', encoding='utf-8') as file:
        len = file.write(text)
    return len
