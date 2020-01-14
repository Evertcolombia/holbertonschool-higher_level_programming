#!/usr/bin/python3
class Rectangle:
    """
    Class definition: Rectangle

    Attributes:
    __width (int): Rectangle width  private

    """
    def __init__(self, width=0, height=0):
        """
        Args:
            width: Rectangle  width
            height: Rectangle height
        """
        self.__height = height
        self.__width = width

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string

        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    string += "#"
                if i < (self.height - 1):
                    string += "\n"

            return string
