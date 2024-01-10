#!/usr/bin/python3
""" Module contains the append_write function """


def append_write(filename="", text=""):
    """ Appends a text to file specified.
    Creates a new file if file does not exist

    Args:
         filename (str): The name of the file
         text (str): The text to write/ append

    Return: Number of bytes written"""

    with open(filename, 'a', encoding='utf-8') as f:
        len = f.write(text)
    return len
