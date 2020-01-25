#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.y = y
        self.x = x

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validation("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validation("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validation("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validation("y", value)
        self.__y = value

    def validation(self, name, value):

        if type(value) is not int:
                raise TypeError("{} must be an integer".format(name))

        if name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
        else:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))

    def area(self):
        return self.__width * self.__height

    def display(self):
            w = self.__width
            h = self.__height
            print('\n' * self.__y, end='')
            print((" " * self.__x + "#" * w + '\n') * h, end='')

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format("Rectangle", \
        self.id, self.__width, self.__height, self.__x, self.__y)

    def update(self, *args):
        if len(args) > 0:
            self.id = args[0]
            for i, arg in enumerate(args):
                if (i == 1):
                    self.x = arg
                if (i == 2):
                    self.y = arg
                if (i == 3):
                    self.width = arg
                if (i == 4):
                    self.height = arg
