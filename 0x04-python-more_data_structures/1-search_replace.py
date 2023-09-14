#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = my_list.copy()
    num = n_list.count(search)
    while num:
        idx = n_list.index(search)
        del n_list[idx]
        n_list.insert(idx, replace)
        num -= 1
    return n_list
