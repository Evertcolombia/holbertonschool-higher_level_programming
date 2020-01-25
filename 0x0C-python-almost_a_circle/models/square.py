#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format( \
        self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.validation("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
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
        l = ["id", "size", "x", "y"]
        d = {}

        for attr in l:
            a = {attr: getattr(self, attr)}
            d.update(a)
        return d
