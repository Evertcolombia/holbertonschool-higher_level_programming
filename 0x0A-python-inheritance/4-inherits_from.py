#!/usr/bin/python3
"""Return True f this i  nheritance
   args:
       obj: obj
       a_class: a class"""


def inherits_from(obj, a_class):
    a = type(obj)
    if a != a_class:
        return issubclass(a, a_class)
