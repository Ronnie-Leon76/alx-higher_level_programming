#!/usr/bin/python3
"""Function to read file"""


def read_file(filename=""):
    """Read file function"""
    with open(filename) as f:
        for line in f:
            print(line, end='')
