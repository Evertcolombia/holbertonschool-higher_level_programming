#!/usr/bin/python3

import _ctypes

def di(obj_id):
    """ Inverse of id() function. """
    return _ctypes.PyObj_FromPtr(obj_id)

if __name__ == '__main__':
    a = 42
    b = 'answer'
    print(di(0x01560000))
    print(di(id(a)))  # -> 42
    print(di(id(b)))  # -> answer
