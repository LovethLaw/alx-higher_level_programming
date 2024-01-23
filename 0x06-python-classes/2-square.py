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
