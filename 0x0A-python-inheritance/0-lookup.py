#!/usr/bin/python3
"""Returns: attributes and methods of
   the obj argument in list form"""

def lookup(obj):
    a = list(dir(obj))
    return a
