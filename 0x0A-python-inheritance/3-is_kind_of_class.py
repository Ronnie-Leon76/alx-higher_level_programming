#!/usr/bin/python3
"""
Module that checks if an object is an instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    function that checks if an object is an instance of a specified class
    """
    return (isinstance(obj, a_class))
