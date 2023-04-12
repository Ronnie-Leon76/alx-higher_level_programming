#!/usr/bin/python3
"""
Module that adds all arguments to a Python list, and then saves to a file"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    try:
        new_list = load_from_json_file("add_item.json")
    except Exception:
        new_list = []
    for i in range(1, len(sys.argv)):
        new_list.append(sys.argv[i])
    save_to_json_file(new_list, "add_item.json")
