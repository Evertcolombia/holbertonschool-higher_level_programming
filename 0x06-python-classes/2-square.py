#!/usr/bin/python3
class Square:
    """
    Class definition: Square

    Attributes:
    __size (int): square size private

    """
    def __init__(self, size=0):
        """
        Args:
            size: swuare size
        """
        self.__size = size

        if type(size) != int:
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >=0")
             
