#!/usr/bin/python3


class BaseGeometry:
    """
    Class definition: BaseGeometry
    """
    def area(self):
         #res = self.__width * self.height
         #print(res)
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
        #self.area(self)

    def __str__(self):
        a, b = str(self.__width), str(self.__height)
        string = ("[Rectangle] " + a + "/" + b + "\n")
        return string[:-1]
