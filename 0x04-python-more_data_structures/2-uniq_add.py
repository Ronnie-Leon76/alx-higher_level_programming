#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    total_unique = 0
    for i in unique:
        total_unique = total_unique + i
    return total_unique
