#!/usr/bin/python3
"""
    This is module define the Square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Rectangle

         Attributes:
             attr1 (width): width size for rectangle
             attr2 (height): height size for rectangle
             attr3 (x): x cordenade
             attr1 (y): y cordenade

    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Validate values
        calling the  super function to use the init method for
        the rectangle class

        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            strng representation of the  instance
        """
        a = "[Square] ({}) {}/{} - {}"
        s = self.id
        return a.format(s, self.x, self.y, self.width)

    @property
    def size(self):
        """
           getter for size

        """
        return self.width

    @size.setter
    def size(self, value):
        """
            setter for size
        """
        self.validation("width", value)
        self.width = value
        self.height = value

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
                    self.size = arg
                if (i == 2):
                    self.x = arg
                if (i == 3):
                    self.y = arg

        elif len(kwargs) > 0 and kwargs is not None:
            for k, v in kwargs.items():
                if (k == "id"):
                    self.id = v
                if (k == "size"):
                    self.size = v
                if (k == "x"):
                    self.x = v
                if (k == "y"):
                    self.y = v

    def to_dictionary(self):
        """
            convert to dictionary
        """
        l = ["id", "size", "x", "y"]
        d = {}

        for attr in l:
            a = {attr: getattr(self, attr)}
            d.update(a)
        return d
