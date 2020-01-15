#!/usr/bin/python3
class Rectangle:
    """
    Class definition: Rectangle

    Attributes:
    __width (int): Rectangle width  private

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Args:
            width: Rectangle  width
            height: Rectangle height
        """
        type(self).number_of_instances += 1
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
            p_s = str(self.print_symbol)
            string = ((p_s * self.__width + "\n") * self.__height)

            return string[:-1]

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
