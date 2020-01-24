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
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self):
        self.__width = width

    @height.setter
    def height(self):
        self.__height = height

    @height.setter
    def x(self):
        self.__x = x

    @height.setter
    def y(self):
        self.__y = y
