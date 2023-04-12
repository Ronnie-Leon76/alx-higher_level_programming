#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file"""
    with open(filename, 'a') as f:
        return f.write(text)
