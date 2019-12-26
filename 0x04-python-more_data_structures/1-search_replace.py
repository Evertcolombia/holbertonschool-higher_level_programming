#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    new_list = list(map(lambda x: x if x != search else replace, new_list))
    return new_list
