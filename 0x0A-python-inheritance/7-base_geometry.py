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

        if isinstance(self.value, int) == False:
            raise TypeError(self.name + " must be an integer")
        if value < 1:
            raise ValueError(self.name + " must be grather than 0")
