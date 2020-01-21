#!/usr/bin/python3


class MyInt(int):

    def __ne__(self, other):
        if int(self) != int(other):
            return False
        return True

    def __eq__(self, other):
        if int(self) == int(other):
            return False
        return True
