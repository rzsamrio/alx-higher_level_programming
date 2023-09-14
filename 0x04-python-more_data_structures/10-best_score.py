#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if a_dictionary == {}:
        return None
    return max(a_dictionary, key=lambda k: a_dictionary[k])
