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
        number_of_instances (int): integer number of the instances
        print_symbol (str): print with the symbol

    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    def area(self):
        """
        Function area

        Formule: width * height = area

        Returns:
            area

        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Function perimeter

        Formula: (width * 2) + (height * 2)

        Returns:
            perimeter

        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)

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
        """Set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """Returns an string simulating the instance"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        else:
            string = (("#" * self.__width + "\n") * self.__height)

            return string[:-1]

    def __repr__(self):
        """Returns an stringre presentation the instance"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))
