#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height

        #self.__y = x_y_validation(y, "y")
        #self.__x = x_y_validation(x, "x")
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
        self.__width = validation(width, "width")

    @height.setter
    def height(self):
        self__height = validation(height, "height")

    def validation(self.__width, val=""):
        if type(self) != int:
            raise TypeError("{} must be an integer",format(val))

        if value <= 0:
            raise ValueError("{} must be > 0".format(val))

    #def x_y_validation(self, value, val=""):
     #   if type(value) != int:
      #      raise TypeError("{} must be an integer".format(val))
       # if value < 0:
        #    raise ValueError("{} must be >= 0". format(val))
