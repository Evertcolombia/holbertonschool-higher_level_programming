#!/usr/bin/python3

class MyInt(int):

    def __eq__(self, other):
        if type(self) is type(other):
            return False
        else:
            return True
