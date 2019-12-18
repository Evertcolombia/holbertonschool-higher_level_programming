#!/usr/bin/python3
def max_integer(my_list=[]):
    tmp = 0
    if len(my_list):
        return None
    tmp = my_list[0]
    for i in my_list:
        if tmp < i:
            tmp = i
    return tmp
