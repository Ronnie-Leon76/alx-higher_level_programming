#!/usr/bin/python3
"""Function prints first and last name"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints first name and last name
    Args:
        first_name: first parameter
        last_name: second parameter
    Returns:
        Nothing
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
