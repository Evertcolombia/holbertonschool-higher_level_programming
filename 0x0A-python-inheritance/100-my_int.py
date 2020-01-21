#!/usr/bin/python3

class MyInt(int):

    def __eq__(self, other):
        if int(self) == int(other):
            return False
        else:
            return True
