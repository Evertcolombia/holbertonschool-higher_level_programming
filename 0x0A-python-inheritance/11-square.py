#!/usr/bin/python3

class BaseGeometry:
    """
    Class definition: BaseGeometry
    """
    def area(self):
         pass

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if type(self.value) != int:
            raise TypeError(self.name + " must be an integer")
        if value < 1:
            raise ValueError(self.name + " must be grather than 0")


class Rectangle(BaseGeometry):
    """
    Subclass defintion: Rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        st = ("[Rectangle] " + str(self.__width) + "/" + str(self.__height) + "\n")
        return st[:-1]


class Square(Rectangle):

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        a = str(self.__size)
        st = ("[Rectangle] " + a + "/" + a + "\n")
        return st[:-1]

