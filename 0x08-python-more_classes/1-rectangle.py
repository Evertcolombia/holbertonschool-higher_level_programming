#!/usr/bin/python3
class Rectangle:
    """
    The Rectangle clas create a new object

    Args:
        width (int): integer value of the width
        height (int): integer value of the height

    Attributes:
        width (int): integer value of the width
        height (int): integer value of the height
    """

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ Get width""" 
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
