#!/usr/bin/python3
""" Module contains:
    Function text_indentation: Prints Individual sentences from a large text
    """


def text_indentation(text):
    """ Args: Large text """

    if type(text) is not str:
        raise TypeError("text must be a string")
    set = 0
    for i, char in enumerate(text):
        if set == 0 and char != ' ':
            c = i
            set = 1
        if char == '.' or char == '?' or char == ':':
            print(text[c:i + 1] + "\n")
            set = 0
