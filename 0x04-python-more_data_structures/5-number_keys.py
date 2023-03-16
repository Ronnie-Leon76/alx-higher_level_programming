#!/usr/bin/python3
def number_keys(a_dictionary):
    no_of_keys = 0
    for k, v in a_dictionary.items():
        no_of_keys = no_of_keys + 1
    return no_of_keys
