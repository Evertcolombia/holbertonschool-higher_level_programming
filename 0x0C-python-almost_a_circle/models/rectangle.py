#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__y = y
        self.__x = x

    @property
    def width(self):
        print("@property.width class method called")
        return self.__width

    @property
    def height(self):
        print("@property.height class method called")
        return self.__height

    @width.setter
    def width(self):
        print("@width.setter clas method called")
        self.__width = width

    @height.setter
    def height(self):
        print("@height.setter clas method called")
        self.__height = height
