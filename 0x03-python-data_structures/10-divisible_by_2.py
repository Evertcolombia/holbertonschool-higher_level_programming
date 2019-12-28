#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    new = []
    for i in range(len(my_list)):
        if (my_list[i] % 2) == 0:
            new.insert(i, True)
        else:
            new.insert(i, False)
    return new
