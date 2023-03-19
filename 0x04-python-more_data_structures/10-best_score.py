#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = 0
    key_value = ''
    if a_dictionary is None:
        return None
    else:
        for k, v in a_dictionary.items():
            if v > max_value:
                max_value = v
                key_value = k
        return key_value
