#!/usr/bin/python3
"""
    This is module define the Square class
"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle

    Attributes:
        attr1 (width): width size for rectangle
        attr2 (height): height size for rectangle
        attr3 (x): x cordenade
        attr1 (y): y cordenade

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Validate values

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.y = y
        self.x = x

    @property
    def width(self):
        """
            getter for width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter for width

        """
        self.validation("width", value)
        self.__width = value

    @property
    def height(self):
        """
            getter for height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for height

        """
        self.validation("height", value)
        self.__height = value

    @property
    def x(self):
        """
            getter for x

        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            setter for x

        """
        self.validation("x", value)
        self.__x = value

    @property
    def y(self):
        """
            getter for y

        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            setter for y

        """
        self.validation("y", value)
        self.__y = value

    def validation(self, name, value):
        """
            validate if the arguments can passed to the instance

            Args:
                param1 (name): name of argument
                params (value):  value

        """
        if type(value) is not int:
                raise TypeError("{} must be an integer".format(name))

        if name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
        else:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))

    def area(self):
        """
            calculate area of rectangle

            Args:
                 param1 (cls): class reference
                 param1 (**dictionary): awkward
        """
        return self.__width * self.__height

    def display(self):
        """
            dyplay a rectangle
        """
        w = self.__width
        h = self.__height
        print('\n' * self.__y, end='')
        print((" " * self.__x + "#" * w + '\n') * h, end='')

    def __str__(self):
        """
            strng representation of the  instance
        """
        c_n = __class__.__name__
        a = "[{}] ({}) {}/{} - {}/{}"
        s_i = self.id
        s_x = self.x
        return a.format(c_n, s_i, s_x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
            update value of arguments

            Args:
                 param1 (*args): argc
                 param1 (**kwargs): awkward
        """
        if len(args) > 0 and args is not None:
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
        elif len(kwargs) > 0 and kwargs is not None:
            for k, v in kwargs.items():
                if (k == "id"):
                    self.id = v
                if (k == "width"):
                    self.width = v
                if (k == "height"):
                    self.height = v
                if (k == "x"):
                    self.x = v
                if (k == "y"):
                    self.y = v

    def to_dictionary(self):
        """
            convert to dictionary
        """
        l = ["id", "width", "height", "x", "y"]
        d = {}

        for attr in l:
            a = {attr: getattr(self, attr)}
            d.update(a)
        return d
