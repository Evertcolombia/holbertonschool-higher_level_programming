#!/usr/bin/python3


class BaseGeometry:
    """
    Class definition: BaseGeometry
    """
    def area(self):
        """
        Raises:
            Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if type(value) is not int:
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
