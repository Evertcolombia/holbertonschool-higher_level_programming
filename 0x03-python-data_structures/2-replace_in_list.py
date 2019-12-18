#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in range(len(my_list) - 1):
        if (idx == i):
            my_list[i] = element
            return my_list
