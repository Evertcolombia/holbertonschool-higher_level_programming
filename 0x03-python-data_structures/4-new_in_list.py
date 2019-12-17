#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = []
    if (idx < 0):
        new = my_list.copy()
        return new
    if (idx > len(my_list) - 1):
        new = my_list.copy()
        return new
    for i in range(len(my_list) - 1):
        if (idx == i):
            new = my_list.copy()
            new[i] = element
            return new
