#!/usr/bin/python3
class MyList(list):
    """class My list
    inherits from list class"""
    def print_sorted(self):
        print(sorted(self))
