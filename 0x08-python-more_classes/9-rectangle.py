#!/usr/bin/python3
class Rectangle:
    """
    The Rectangle clas create a new object

    Args:
        width (int): integer value of the width
        height (int): integer value of the height

    Attributes:
        width (int): integer value of the width
        height (int): integer value of the height
        number_of_instances (int): integer number of the instances
        print_symbol (str): print with the symbol

    """
    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.__height = height
        self.__width = width

    def area(self):
        """
        Function area

        Formule: width * height = area

        Returns:
            area

        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Function perimeter

        Formula: (width * 2) + (height * 2)

        Returns:
            perimeter

        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)

    @property
    def width(self):
        """ Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """Returns an string simulating the instance"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        else:
            p_s = str(self.print_symbol)
            string = ((p_s * self.__width + "\n") * self.__height)

            return string[:-1]

    def __repr__(self):
        """Returns an stringrepresentation  the instance"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """del object print"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Function static bigger_or_equal

        Args:
            rect_1 (Rectangle): first rectangle to compare
            rect_2 (Rectangle): second rectangle to compare

        Returns:
            biggest rectangle
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
