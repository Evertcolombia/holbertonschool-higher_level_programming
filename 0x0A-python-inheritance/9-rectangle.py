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
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
       return "[Rectangle] " + str(self.__width) + "/" + str(self.__width)
