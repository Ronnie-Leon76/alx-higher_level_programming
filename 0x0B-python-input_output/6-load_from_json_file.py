#!/usr/bin/python3
"""Module that creates an Object from a JSON file"""

import json


def load_from_json_file(filename):
    """function that creates an object from a JSON file"""
    with open(filename) as f:
        read_data = f.read()
    return json.loads(read_data)
