#!/usr/bin/python3
""" Module returns a list of names defined by an object """


def lookup(obj):
    """Args: object"""
    return dir(obj)
