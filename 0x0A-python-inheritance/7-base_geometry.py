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
        if value <= 0:
            raise ValueError(self.name + " must be grather than 0")
