#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = []
    if (idx < 0):
        return my_list
    if (idx > len(my_list)):
        return my_list
    new = my_list.copy()
    for i in range(len(my_list) - 1):
        if (idx == i):
            new[i] = element
    return new
