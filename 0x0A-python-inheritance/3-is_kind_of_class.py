#!/usr/bin/python3
""" Return True is is instance
    or if the object is an instance of a class
    args:
        obj: obj
        a_class: a class"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    return False
