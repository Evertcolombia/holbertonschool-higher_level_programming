#!/usr/bin/python3
def element_at(my_list, idx):
    len_list = len(my_list) - 1

    if idx < 0:
        return None
    elif idx < len_list:
        for i in range(len_list):
            if i == idx:
                return str(my_list[i])
    else:
        return None
