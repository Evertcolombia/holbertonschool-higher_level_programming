#!/usr/bin/python3
"""Return false is obj is same type
    of a_class(argument)   
    arguments:
        obj: obj
        a_class: a class
"""


def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    return False
