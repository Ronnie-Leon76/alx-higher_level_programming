#!/usr/bin/python3
"""Module checks if an object is an instance of a specified class"""


def is_same_class(obj, a_class):
    """
    function returns true if object is an instance of a specified class
    """
    return (type(obj) == a_class)
