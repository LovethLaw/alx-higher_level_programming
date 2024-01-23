#!/usr/bin/python3
"""This module defines the class Square with an attribute"""


class Square:
    """This is the class Square

    Attributes:

        size: This is the size of the square

    """
    def __init__(self, size=0):

        self.__size = size

        if not isinstance(size, int):

            raise TypeError("size must be an integer")

        elif size < 0:

            raise ValueError("size must be >= 0")

    @property
    def size(self):

        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):

            raise TypeError("size must be an integer")

        elif value < 0:

            raise ValueError("size must be >= 0")
        else:

            self.__size = value

    def area(self):
        """ calculates the current square area

            Returns:
                The area of the current square
        """
        return self.__size ** 2

    def my_print(self):
        """ prints the squares to stdout """
        if self.__size == 0:

            print()

        for i in range(self.__size):

            for j in range(self.__size):

                print("#", end="")
            print()
