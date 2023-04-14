#!/usr/bin/python3
"""
Module checks if the object is an instance of a class that inherited
(directly or indirectly)
"""


def inherits_from(obj, a_class):
    """
    function checks if object is an instance of a class that inherited
    (directly or indirectly)
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
