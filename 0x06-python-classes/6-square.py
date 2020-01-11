#!/usr/bin/python3
class Square:

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size  == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for i in range (self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        for num in range(value):
            if num > 2 or type(value) != tuple:
                raise TypeError("position must be a tuple of 2 positive integers")
            elif type(value[num]) != int:
                raise TypeError("position must be a tuple of 2 positive integers")
            elif value[num] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
            else:
                self.__position = value
